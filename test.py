import cv2
import time

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise RuntimeError("Camera not accessible")

    # Optional. Ask for a stable size
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            time.sleep(0.05)
            continue

        cv2.imshow("camera", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
