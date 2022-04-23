import cv2 as cv
import numpy as np

img=cv.imread('Resources/Photos/park.jpg')

cv.imshow('Boston', img)

#translation
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


"""
x--> Right
y--> Down
-x--> Left
-y--> Up
"""   

translated_img= translate(img,-100,100)
cv.imshow('Translated Image', translated_img)

#rotation
def rotate(img, angle, rotPoint=None):
    (height,width)= img.shape[0:2]
    dimensions= (width,height)

    if rotPoint is None:
        rotPoint= (width//2, height//2)
    
    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)

    return cv.warpAffine(img, rotMat, dimensions)

rotated_img= rotate(img, 45)
cv.imshow('Rotated Image', rotated_img)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#flipping
flip= cv.flip(img, 1)
cv.imshow('Flipped Image', flip)

#cropping
cropped=img[200:400, 300:400]
cv.imshow('Cropped Image', cropped)

 
cv.waitKey(0)