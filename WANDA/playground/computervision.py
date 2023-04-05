import cv2 as eyes
import numpy as np

def face_detection():
    detection = eyes.CascadeClassifier('D:/ProgramData/cascadeclassifier/haarcascade_frontalface_default.xml')
    #Image Location
    img = eyes.imread('image location')

    #Converting image
    gray = eyes.cvtColor(img,eyes.COLOR_BGR2GRAY)

    #Detecting Face
    faces = face_detection.detectMultiScale(gray, 1.3, 5)

    #Drawing Rectangle
    for (x,y,w,h) in faces:
        img = eyes.rectangle(img,(x,y),(x+w, y+h),(255,0,0),3)
    eyes.imwrite('Face.jpg', img)
