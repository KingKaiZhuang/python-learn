import cv2 
import numpy as np
import random

img = cv2.imread('test1.jpg')
# print(img.shape)

# img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
# cv2.imshow('img',img)
# cv2.waitKey(0)

# img = np.empty((300,300,3),np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

newimg = img[:150,200:400]

cv2.imshow('img',img)
cv2.imshow('newimg',newimg)
cv2.waitKey(0)