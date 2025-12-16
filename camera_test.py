import cv2
import time


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    raise RuntimeError("Camera not accessible")

while True:
    ret, frame = cap.read()
    if not ret:
        break   
    cv2.imshow("Camera Test", frame)
    print(frame.shape,end="\r")
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()





