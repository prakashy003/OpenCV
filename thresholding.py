import cv2 as cv
from cv2 import threshold

img= cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple thresholding
threshold, thresh_inv= cv.threshold(gray, 150, 255,cv.THRESH_BINARY_INV)
cv.imshow("Simple threshold Inverse", thresh_inv)

threshold, thresh= cv.threshold(gray, 150, 255,cv.THRESH_BINARY)
cv.imshow("Simple threshold Inverse", thresh)

#Adaptive thresholding
adap_thresh=cv.adaptiveThreshold(gray,255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Threshold', adap_thresh) 

cv.waitKey(0)