import logging
import threading
import time

import cv2


class CameraTracker:
    def __init__(self, index=0, width=640, height=480, debug=False):
        self.index = index
        self.width = width
        self.height = height
        self.debug = debug

        self.latest_frame = None
        self.latest_frame_ts = None

        self.cap = None
        self.thread = None
        self.stop_event = threading.Event()

        self.log = logging.getLogger(self.__class__.__name__)

    def start(self):
        if self.thread and self.thread.is_alive():
            self.log.info("Camera already running")
            return

        self.stop_event.clear()
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()
        self.log.info("Camera thread started")

    def stop(self):
        self.log.info("Camera stop requested")
        self.stop_event.set()

        if self.thread:
            self.thread.join(timeout=2.0)
            self.log.info("Camera thread stopped")

    def get_latest_frame(self):
        frame = self.latest_frame
        ts = self.latest_frame_ts

        if frame is None:
            return None, None

        return ts, frame.copy()

    def _open_camera(self):
        self.log.info("Opening camera index=%s", self.index)
        cap = cv2.VideoCapture(self.index)

        if not cap.isOpened():
            self.log.error("Camera not accessible")
            raise RuntimeError("Camera not accessible")

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.log.info("Camera opened (%sx%s)", self.width, self.height)
        return cap

    def _release(self):
        if self.cap:
            self.log.info("Releasing camera")
            self.cap.release()
            self.cap = None

        if self.debug:
            self.log.info("Destroying OpenCV windows")
            cv2.destroyAllWindows()

    def _loop(self):
        self.log.info("Camera loop entered")

        try:
            self.cap = self._open_camera()

            while not self.stop_event.is_set():
                ret, frame = self.cap.read()

                if not ret or frame is None:
                    self.log.warning("Failed to read frame")
                    time.sleep(0.05)
                    continue

                self.latest_frame = frame
                self.latest_frame_ts = time.monotonic()

                if self.debug:
                    cv2.imshow("camera_debug", frame)
                    cv2.waitKey(1)

        except Exception:
            self.log.exception("Camera loop crashed")

        finally:
            self._release()
            self.log.info("Camera loop exited")
