import cv2 as cv
#lyrics = cv.imread('f2.png')

#cv.imshow('Song',lyrics)

capture= cv.VideoCapture('meme.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Meme', frame)
cv.waitKey(0)