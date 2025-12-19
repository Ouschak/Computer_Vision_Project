import cv2 as cv
import threading
import time

class CameraTracker:
    def __init__(self, index=0, width=640, height=480, debug=False):
        self.index = index
        self.width = width
        self.height = height
        self.debug = debug

        self.cap = None
        self.thread = None
        self.stop_event = threading.Event()

        self.latest_frame_ts = None

    def start(self):
        if self.thread and self.thread.is_alive():
            return

        self.stop_event.clear()
        self.thread = threading.Thread(target=self._loop, daemon=True)
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        if self.thread:
            self.thread.join(timeout=2)
        self._release()

    def _open_camera(self):
        cap = cv.VideoCapture(self.index)
        if not cap.isOpened():
            raise RuntimeError("Camera not accessible")

        cap.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)
        return cap

    def _release(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        if self.debug:
            cv.destroyAllWindows()

    def _loop(self):
        try:
            self.cap = self._open_camera()
            while not self.stop_event.is_set():
                ret, frame = self.cap.read()
                if not ret or frame is None:
                    continue

                self.latest_frame_ts = time.monotonic()

                if self.debug:
                    cv.imshow("camera_debug", frame)
                    cv.waitKey(1)
        finally:
            self._release()

if __name__ == "__main__":
    tracker=CameraTracker()
    tracker.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        tracker.stop()

