#this is where post processing of the images to create the data we need to train the classifier
import mediapipe as mp
import cv2
import os
import matplotlib.pyplot as plt

DATA_DIRECTORY='./data'

for dir in os.listdir(DATA_DIRECTORY):# gets all the files from the DATA_DIRECTORY directory
    for imgPath in os.listdir(os.path.join(DATA_DIRECTORY,dir)):
        img= cv2.imread(os.path.join(DATA_DIRECTORY,dir,imgPath))#loads a specific image
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        plt.figure()
        plt.imshow(img_rgb)
plt.show()