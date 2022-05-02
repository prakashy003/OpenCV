import cv2 as cv
from matplotlib import image

img=cv.imread('Resources/Photos/group 1.jpg')
# cv.imshow('A Group',img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade= cv.CascadeClassifier('Face detection/haar_face.xml')

faces = haar_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces detected: {len(faces)}')

for a,b,c,d in faces:
    cv.rectangle(img, (a,b), (a+c,b+d), (0,255,0),thickness=2)
cv.imshow("Face Detected", img)
cv.waitKey(0)