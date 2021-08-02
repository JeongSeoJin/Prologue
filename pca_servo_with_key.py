from __future__ import division
import time
import tkinter
# Import the PCA9685 module.
import Adafruit_PCA9685
from tkinter import *

# Uncomment to enable debug output.
#import logging

#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_mid = 350
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

root = Tk()
root.title("Robot Arm Controller")
root.geometry("200x400")

a = 350
def keyPressed(event):
    global a
    # 키보드 문자하나 출력
    print(event.char)

    if event.char == "q":
        a += 3
    elif event.char == "a":
        a -= 3

    if event.char == "Q":
        a += 10
    elif event.char == "A":
        a -= 10

    if a < 150:
        a = 150
    elif a > 550:
        a = 550
    print("This is a value of variable : {}".format(a))
    print("servo value : {}".format(a))
    pwm.set_pwm(1, 0, a)
    value="servo : "+str(a)
    label.config(text=value)


# print("This is a value of outside : {}".format(a))
label=tkinter.Label(root, text="servo : 0")
label.pack()
 
frame = Frame(root, width=100, height=100)
# Key 이벤트 바인딩
frame.bind('<Key>', keyPressed) 
frame.place(x=0, y=0)
 
# 키보드 포커를 갖게 한다
frame.focus_set()

root.mainloop()

