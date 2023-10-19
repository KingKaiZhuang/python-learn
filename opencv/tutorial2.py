import cv2
import numpy as np

# B G R

img = cv2.imread('colorcolor.jpg')
# print(img.shape)

# 製作綠色圖片
# img = np.empty((300,300,3),np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row, col] = [0,255,0]

newImg = img[:150,:200]

cv2.imshow('img',img)
cv2.imshow('newImg',newImg)
cv2.waitKey(0)