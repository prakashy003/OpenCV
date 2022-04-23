import cv2 as cv

img= cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.2):
#image, video, and live video
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)

    dimesions = (width,height)

    return cv.resize(frame, dimesions, interpolation=cv.INTER_AREA)

#Rescaling image
resized_img=rescaleFrame(img)
cv.imshow('resized cat', resized_img)

#Rescaling video
capture=cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame= capture.read()

    frame_resized= rescaleFrame(frame)
    cv.imshow('Dog', frame)
    cv.imshow('video_resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


#Rescaling live videos(webcam)
"""
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
"""

capture.release()
cv.destroyAllWindows()