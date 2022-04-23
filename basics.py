import cv2 as cv

img=cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

#converting to grayscale
"""gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)"""

#blur
blur= cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blur)

#edge cascade
# canny= cv.Canny(img, 125,175)
# cv.imshow('Canny Edges', canny)

canny= cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

#dilating the image
dilated_img=cv.dilate(canny, (5,5), iterations=3)
cv.imshow('Dilated Image', dilated_img)

#eroding
eroded_img= cv.erode(dilated_img, (5,5), iterations=3)
cv.imshow('Eroded Image', eroded_img)

#resize
resized_img= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', resized_img)

#cropping
cropped_img= img[50:200, 200:400]
cv.imshow('Cropped Image', cropped_img)

cv.waitKey(0)