import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def findPen(img):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower = np.array([106,147,0])
    upper = np.array([179,255,254])

    mask = cv2.inRange(hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    findContour(img)
    cv2.imshow('result',result)

def findContour(img):
    contours, hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),4)
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt,True)
            vertices = cv2.approxPolyDP(cnt,peri * 0.02,True)
            x,y,w,h = cv2.boundingRect(vertices)

while True:
    ret,frame = cap.read()
    if ret:
        imgContour = frame.copy()
        cv2.imshow('video',frame)
        findPen(frame)
        cv2.imshow('contour',imgContour)
    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break
    cv2.waitKey(10)

