\# CV Object Detection



A standalone computer vision project with the eventual goal of feeding detection results into

an Automated Object detection and avoidance robot.



\## Why this is a separate repo

Classical CV and object detection are being learned and tested on live

webcam input first, outside simulation, for fast iteration. Once the

detection logic is solid, it gets ported into the Webots controller to

replace the robot's current placeholder camera code.



\## Built so far

\- Basic webcam capture and live display loop (OpenCV, `cv2.VideoCapture`)



\## In progress

\- Classical color/contour-based object detection (`cv2.inRange`,

&#x20; `cv2.findContours`) — the same "find a colored blob" logic already

&#x20; prototyped in the Webots robot's camera code, done properly here



\## Planned

\- Pretrained object detection (YOLO via `ultralytics`) on live webcam feed

\- Optional: a small CNN trained from scratch on a custom toy dataset



\## Eventual integration point

Once detection is reliable here, port the detection function into the

Webots robot controller — feeding it `camera.getImage()` frames instead

of webcam frames — so detected objects can influence the robot's PID

steering target instead of a fixed waypoint list.



\## Related project

\[automated-obstacle-avoider](link-to-that-repo-once-you-have-it) —

the Webots simulation this will eventually connect to.

