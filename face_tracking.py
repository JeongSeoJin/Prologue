from __future__ import division

import cv2
from tkinter import Frame
# from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


######################=======Servo Setting======###########################
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 530  # Max pulse length out of 4096


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(50)

##############################################################################


#######################========Opencv Setting========#########################

# Load the cascade
face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/python/Opencv/haarcascade_frontalface_default.xml') # for linux
# face_cascade = cv2.CascadeClassifier('C:/user/pysuk/Opencv/haarcascade_frontalface_default.xml') # for wondow

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
right = "Go Right"
left = "Go left"
up = "Go Up"
down = "Go Down"

color_deep_dark = (255, 255, 255)
color_dark = (100, 100, 100)
  
# Line thickness of 5 px
thickness = 2
start_point = (320, 0)
end_point = (320, 480)



servo1_mid = 350
servo2_mid = 350

pwm.set_pwm(0, 0, servo1_mid)
pwm.set_pwm(1, 0, servo2_mid)
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

        # cv2.line(img, (x + int(w/2), y), (x + int(w/2), y + h), color_dark, thickness)

        face_center_x = (x + int(w/2))
        face_center_y = (y + int(w/2))

        center_x = 320
        center_y = 240


        if  face_center_x < center_x:
            servo1_mid += 7

        elif  face_center_x > center_x:
            servo1_mid -= 7

        if face_center_y > center_y:
            servo2_mid += 7

        elif face_center_y < center_y:
            servo2_mid -= 7


        # servo1_mid = (int((x/2)+(w/2)))
        # servo2_mid = (int((y/2)+(w/2)))
    pwm.set_pwm(0, 0, servo1_mid)
    pwm.set_pwm(1, 0, servo2_mid)
    # Display

    # Display
    cv2.imshow('face_recognition', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        pwm.set_pwm(0, 0, 350)
        pwm.set_pwm(1, 0, 350)
        break
        
# Release the VideoCapture object
cap.release()