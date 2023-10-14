import cv2
import numpy as np

kernel = np.ones((3,3),np.uint8)

img = cv2.imread('test1.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img,(7,7),0)
canny = cv2.Canny(img,100,150)
dilate = cv2.dilate(canny,kernel,iterations=1)
erode = cv2.erode(dilate,kernel,iterations=1)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)