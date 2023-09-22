#this is where post processing of the images to create the data we need to train the classifier
import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt
import pickle

DATA_DIRECTORY='./data'

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

training_data=[]
labels=[]

hands=mp_hands.Hands(static_image_mode=True,min_detection_confidence=0.3)

for dir in os.listdir(DATA_DIRECTORY):# gets all the files from the DATA_DIRECTORY directory
    for imgPath in os.listdir(os.path.join(DATA_DIRECTORY,dir)):
        data_aux=[]
        img= cv2.imread(os.path.join(DATA_DIRECTORY,dir,imgPath))#loads a specific image
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        results=hands.process(img_rgb)#processes an RGB image and returns the hand landmarks and handedness (left v.s. right hand) of each detected hand
        if results.multi_hand_landmarks:
            for h_landmarks in results.multi_hand_landmarks:#taking landmarks and creating array for data processing
                for i in range(len(h_landmarks.landmark)):
                    #print(h_landmarks.landmark[i])
                    x=h_landmarks.landmark[i].x
                    y=h_landmarks.landmark[i].y
                    z=h_landmarks.landmark[i].z
                    data_aux.append(x)
                    data_aux.append(y)
            training_data.append(data_aux)
            labels.append(dir)
o=open('data.pickle','wb')
pickle.dump({'data':training_data,'labels':labels},o)
o.close()
                # mp_drawing.draw_landmarks(
                #     img_rgb,
                #     h_landmarks,
                #     mp_hands.HAND_CONNECTIONS,
                #     mp_drawing_styles.get_default_hand_landmarks_style(),
                #     mp_drawing_styles.get_default_hand_connections_style()
                # ) this shows the landmarks
                

