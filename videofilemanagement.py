import cv2 as cv
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
detectionvideo=cv.VideoCapture("objectdetectiondata.mp4")
while detectionvideo.isOpened():
    ret, frame= detectionvideo.read()
    if not ret:
        print("Unable to read video file")
        break
    result=model(frame)
    cv.imshow("Object detection", result[0].plot())
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
detectionvideo.release()
cv.destroyAllWindows()