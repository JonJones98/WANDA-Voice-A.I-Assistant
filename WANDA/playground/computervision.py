import cv2
import numpy as np
import sys
import face_recognition as fr
for x in sys.argv:
     print ("Argument: ", x)


def face_detection():
    cascPath = sys.argv[0]
    faceCasade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)
    while True:
        #Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCasade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        #Draw a rectangle around the faces
        #for( x, y, w, h) in faces:
        #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
face_detection()


