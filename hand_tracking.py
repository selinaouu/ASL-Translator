import cv2 #opencv suscessfully installed
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils #this will help us draw out the hands
mp_holistic = mp.solutions.holistic
mp_hands=mp.solutions.hands


feed_capture=cv2.VideoCapture(0) #we only have a single camera

while feed_capture.isOpened():
    ret,frame=feed_capture.read()

    #this is the hand tracking model
    colored_frame=cv2.cvtColor( frame,cv2.COLOR_BGR2RGB)
    res= mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7,min_tracking_confidence=0.5).process(colored_frame)

    #these are the finger annotations
    frame=cv2.cvtColor(colored_frame,cv2.COLOR_RGB2BGR)
    if( res.multi_hand_landmarks):#checking if there are any hands(so we know if we need to put anotations)
        for hand_landmark in res.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmark,connections=mp_hands.HAND_CONNECTIONS)


    cv2.imshow("camera feed",frame)
    if cv2.waitKey(1) == 27:
        break
feed_capture.release()

