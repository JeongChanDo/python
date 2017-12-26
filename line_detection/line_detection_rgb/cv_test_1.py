#!/usr/bin/env python

import cv2

image = cv2.imread('solidWhiteCurve.jpg')

cv2.imshow('result',image)
cv2.waitKey(0)
