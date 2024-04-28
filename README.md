# ASL-Translator
## About 
This repository contains a American Sign Language(ASL) translator, written in Python.

## What it does
This ASL translator uses OpenCV, Mediapipe, and ScikitLearn to provide the translation of sign language. You're able to train a custom model using the data collecting feature(through photos taken), which then you can create datasets from to use for model training! For training, the model uses a Random Forest Classifier that learns patterns from the features extracted from the hand gestures and makes predictions based on those patterns. By iteratively training and refining the model with collected data, the translator becomes more accurate and capable of recognizing a wide range of sign language gestures.

## Key Features
- Data Collection
- Dataset creation
- Feature Extraction

## Tech Stack
- Python
- OpenCV
- Mediapipe
- ScikitLearn
