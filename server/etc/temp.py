#!/usr/bin/env python
import cv2
import numpy as np

img = cv2.imread('tmp.jpg',0)

cv2.imshow('result',img)
print(img)

print("shape : " +str(img.shape))
print("type : " + str(img.type()))
cv2.waitKey(10000)
