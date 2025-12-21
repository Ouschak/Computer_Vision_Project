import logging


import time

from backend.trackers.CameraTracker import CameraTracker
from backend.vision.looking_sensor import LookingSensor
import cv2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
)

log = logging.getLogger("lab")


def main():
    TIMEOUT = 1.0
    total_fps_processed = 0

    last_seen = None  # when camera last produced a frame
    last_processed_ts = None  # when vision last processed a frame

    cam = CameraTracker()
    vision = LookingSensor()

    cam.start()
    try:
        while True:
            frame_ts, frame = cam.get_latest_frame()

            if frame is not None:
                now = time.monotonic()

                # defend against rare None ts
                if frame_ts is None:
                    frame_ts = now

                last_seen = frame_ts

                # process only NEW frames
                if last_processed_ts is None or frame_ts > last_processed_ts:
                    result = vision.process_frame(frame)
                    print(result, flush=True)
                    total_fps_processed += 1
                    last_processed_ts = frame_ts
                    cv2.imshow("vision_debug", frame)
                    cv2.waitKey(1)

                time.sleep(0.05)  # FPS PROCESSING
                continue

            # no frame
            if last_seen is not None and (time.monotonic() - last_seen) > TIMEOUT:
                print("No frames for 1 second. Exiting.")
                break

            time.sleep(0.05)

    finally:
        cam.stop()
        log.info("total_fps_processed are %s", total_fps_processed)


if __name__ == "__main__":
    main()
