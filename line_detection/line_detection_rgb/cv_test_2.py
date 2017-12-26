#!/usr/bin/env python
import cv2
import numpy as np

image = cv2.imread('solidWhiteCurve.jpg')

mark = np.copy(image)

blue_threshold=200
green_threshold=200
red_threshold=200

bgr_threshold=[blue_threshold,green_threshold,red_threshold]

thresholds=(image[:,:,0]<bgr_threshold[0])|(image[:,:,1]<bgr_threshold[1])|(image[:,:,2]<bgr_threshold[2])
mark[thresholds]=[0,0,0]

cv2.imshow('white',mark)
cv2.imshow('result',image)



cv2.waitKey(0)
