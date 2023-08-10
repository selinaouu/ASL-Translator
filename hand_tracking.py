import cv2 #opencv suscessfully installed
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils #this will help us draw out the hands
mp_holistic = mp.solutions.holistic

feed_capture=cv2.VideoCapture(0) #we only have a single camera

while feed_capture.isOpened():
    ret,frame=feed_capture.read()
    cv2.imshow("camera feed",frame)
    if cv2.waitKey(1) == 27:
        break
feed_capture.release()


print(cv2.__version__)