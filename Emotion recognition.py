import cv2
import numpy as np 
from keras.preprocessing import image
from keras.models import model_from_json
import os

#loading the model
model_json = open("model.json", "r")
model_json = model_json.read()
model = model_from_json(model_json)
model.load_weights("model.h5")

#detecting emotion through webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation = cv2.INTER_AREA)
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis = 0)
        img_pixels /= 255
        predictions = model.predict(img_pixels)
        max_index = np.argmax(predictions[0])
        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        emotion = emotions[max_index]
        cv2.putText(frame, emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

#detecting emotion through selfie camera
cap1 = cv2.VideoCapture(0)
while True:
    ret, frame1 = cap1.read()
    frame1 = cv2.flip(frame1, 1)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    faces1 = face_cascade.detectMultiScale(gray1, 1.3, 5)
    for (x,y,w,h) in faces1:
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray1 = gray1[y:y+h, x:x+w]
        roi_gray1 = cv2.resize(roi_gray1, (48, 48), interpolation = cv2.INTER_AREA)
        img_pixels1 = image.img_to_array(roi_gray1)
        img_pixels1 = np.expand_dims(img_pixels1, axis = 0)
        img_pixels1 /= 255
        predictions1 = model.predict(img_pixels1)
        max_index1 = np.argmax(predictions1[0])
        emotions1 = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        emotion1 = emotions1[max_index1]
        cv2.putText(frame1, emotion1, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow('frame1', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()
