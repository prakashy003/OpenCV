import cv2 as cv
import numpy as np

img= cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

blank= np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

"""blur=cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny=cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)"""

#threshold of the image
#if the intensity of a pixel is less than 125 then its set to black whereas above 125, set to white(255).
ret, thresh= cv.threshold(gray, 125, 255,cv.THRESH_BINARY)
cv.imshow("threshold", thresh)

# contours, hirarchies= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contour(s) found!')

contours, hirarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

#draw contours in a blank img
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn',blank)



cv.waitKey(0)