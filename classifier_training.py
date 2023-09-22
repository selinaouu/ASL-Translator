import mediapipe as mp
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

data_dict=pickle.load(open('./data.pickle','rb'))
#print(data_dict.keys())
#print(data_dict.values())

data=np.asarray(data_dict['data'])
labels=np.asarray(data_dict['labels'])

#splitting data into two sets: training set, test set

#we are keeping 20% of the data for testing, we shuffle the data to prevent biases in data, we keep the same proportions
x_train,x_test,y_train,y_test=train_test_split(data,labels,test_size=0.2,shuffle=True,stratify=labels)

model=RandomForestClassifier()
model.fit(x_train,y_train)
y_predict=model.predict(x_test)
total_score=accuracy_score(y_predict,y_test)
print("{}% of models were trained correctly".format(total_score*100))

o=open('model.p','wb')
pickle.dump({'model':model},o)
o.close()