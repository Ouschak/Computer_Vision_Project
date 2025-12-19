import logging
import threading
import time

import cv2


class CameraTracker:

    #debug flag is temporary variable until UI is implemented 
    def __init__(self, index=0, width=640, height=480, debug=False):
        self.index = index
        self.width = width
        self.height = height
        self.debug = debug

        self.cap = None
        self.thread = None
        self.stop_event = threading.Event()

        self.latest_frame_ts = None

        self.log = logging.getLogger(self.__class__.__name__)

    def start(self):
        if self.thread and self.thread.is_alive():
            self.log.info("start() called but tracker is already running")
            return

        self.stop_event.clear()
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()
        self.log.info("Camera thread started")

    def stop(self):
        self.log.info("Stop requested")
        self.stop_event.set()

        if self.thread:
            self.thread.join()  # keep it simple: wait until it ends
            self.log.info("Camera thread stopped")

    def _open_camera(self):
        self.log.info("Opening camera index=%s", self.index)

        cap = cv2.VideoCapture(self.index)
        if not cap.isOpened():
            self.log.error("Camera not accessible (index=%s)", self.index)
            raise RuntimeError("Camera not accessible")

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self.log.info("Camera opened (requested %sx%s)", self.width, self.height)
        return cap

    def _release(self):
        if self.cap is not None:
            self.log.info("Releasing camera")
            self.cap.release()
            self.cap = None

        if self.debug:
            cv2.destroyAllWindows()

    def _loop(self):

        try:
            self.cap = self._open_camera()
            self.log.info("Reading frames... (press 'q' in the window to stop if debug=True)")

            while not self.stop_event.is_set():
                ret, frame = self.cap.read()

                if not ret or frame is None:
                    self.log.warning("Failed to read frame (will retry)")
                    time.sleep(0.05)
                    continue

                self.latest_frame_ts = time.monotonic()

                if self.debug:
                    cv2.imshow("camera_debug", frame)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("q"):
                        self.log.info("Pressed 'q' -> stopping")
                        self.stop_event.set()
                        break
        except Exception:
            self.log.exception("Camera loop crashed")
        finally:
            self._release()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log")

        ]

    )

    tracker = CameraTracker()
    tracker.start()

    try:
        while not tracker.stop_event.is_set():
            time.sleep(0.1)
    except KeyboardInterrupt:
        tracker.stop()