import cv2 as cv

img= cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.2):
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)

    dimesions = (width,height)

    return cv.resize(frame, dimesions, interpolation=cv.INTER_AREA)
    
cv.waitKey(0)
