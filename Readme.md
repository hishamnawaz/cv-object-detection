# CV Object Detection



A standalone computer vision project with the eventual goal of feeding detection results into

an Automated Object detection and avoidance robot.



## Built so far

- Basic webcam capture and live display loop (OpenCV, `cv2.VideoCapture`)
- Object detection in pictures has been implemented 



## In progress

- Classical color/contour-based object detection (`cv2.inRange`, &#x20; `cv2.findContours`) — the same "find a colored blob" logic already.
- Object detection from a video
  

## Planned

- Pretrained object detection (YOLO via `ultralytics`) on live webcam feed
- Fine tuning YOLOv8 by annotating for specific objects and purposes


## Eventual integration point

Once detection is reliable here, port the detection function into the

Webots robot controller — feeding it `camera.getImage()` frames instead

of webcam frames — so detected objects can influence the robot's PID

steering target instead of a fixed waypoint list.



## Related project

[automated-obstacle-avoider](https://github.com/Hisham-1-Blip/automated-obstacle-avoider.git) —

the Webots simulation this will eventually connect to.

