import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

#plt shows the image in the form of RGB
"""plt.imshow(img)
plt.show()"""

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#BGR to HSV
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)
 
#BGR to LAB
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

#BGR
plt.imshow(rgb)
plt.show()



cv.waitKey(0)