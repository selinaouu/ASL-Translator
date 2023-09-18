import cv2 #opencv suscessfully installed

import os

DATA_DIRECTORY='./data'

#if not os.listdir(DATA_DIRECTORY):
    #os.makedirs(DATA_DIRECTORY)

class_num=3
dataset_size=100


feed_capture=cv2.VideoCapture(0) #we only have a single camera
for j in range(class_num):
    if(not os.path.exists(os.path.join(DATA_DIRECTORY,str(j)))):
        os.makedirs(os.path.join(DATA_DIRECTORY,str(j)))

    finished=False

    while True:
        ret,frame=feed_capture.read()
        cv2.putText(frame, "If you're ready, please press Q:",(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 0, 0),1,cv2.LINE_AA)
        cv2.imshow("camera feed",frame)
        if cv2.waitKey(25) == ord('q'):
            break
# for this proj, im going to be taking the landmarks of each image and classifying the landmarks
    count=0

    while count<dataset_size:
        ret,frame=feed_capture.read()
        cv2.imshow("camera feed",frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIRECTORY, str(j), '{}.jpg'.format(count)), frame)
        count+=1

feed_capture.release()
cv2.destroyAllWindows()

