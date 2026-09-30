# CV Object Detection

A standalone computer vision project with the eventual goal of feeding detection results into
an Automated Object detection and avoidance robot.

## Built so far

- Basic webcam capture and live display loop (OpenCV, `cv2.VideoCapture`)
- Object detection in pictures has been implemented
- Object detection from a video
- Pretrained object detection (YOLO via `ultralytics`) on live webcam feed
  
## In progress

- Classical color/contour-based object detection (`cv2.inRange`, &#x20; `cv2.findContours`) — the same "find a colored blob" logic already.
- Fine tuning YOLOv8 by annotating for specific objects and purposes

## Related project

[automated-obstacle-avoider](https://github.com/hishamnawaz/automated-obstacle-avoider.git) — the Webots simulation this will eventually connect to.

