from tkinter import Frame
import cv2

# Load the cascade
# face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/python/Opencv/haarcascade_frontalface_default.xml') # for linux
face_cascade = cv2.CascadeClassifier('C:/user/pysuk/Opencv/haarcascade_frontalface_default.xml') # for wondow

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 25)

print(cap.get(cv2.CAP_PROP_FPS))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

center = "Center"
right = "Right"
left = "left"
up = "Go Up"
down = "Go Down"

while True:
    # Read the frame
    success, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if x >= 380:
            cv2.putText(img, right, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)
        elif x <= 260:
            cv2.putText(img, left, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)
        elif x < 380 and x > 260:
            if y >= 300:
                cv2.putText(img, center, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)
                cv2.putText(img, down, (50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)

            elif y <= 180:
                cv2.putText(img, center, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)
                cv2.putText(img, up, (50, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)

            else:
                cv2.putText(img, center, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 2)
    # Display
    cv2.imshow('face_recognition', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()