import cv2
import time


cap = cv2.VideoCapture(0)
frame_test=0


if not cap.isOpened():
    raise RuntimeError("Camera not accessible")
fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS:", fps)
sampleEveryFrame=int(fps)
while True:
    ret, frame = cap.read()
    if not ret:
        break   

    frame_test+=1

    if frame_test % (sampleEveryFrame//6) !=0:
        continue
    
    cv2.imshow("Camera Test", frame)
    print(frame.shape,end="\r")
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()




