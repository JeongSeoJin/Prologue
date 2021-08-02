from __future__ import division
import time
import tkinter
# Import the PCA9685 module.
import Adafruit_PCA9685


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


window=tkinter.Tk()
window.title("ROBOT ARM CONTROLLER")
window.geometry("640x400+100+100")
window.resizable(False, False)

def select(self):
    value="servo : "+str(scale.get())
    label.config(text=value)
    pwm.set_pwm(1, 0, scale.get())


var=tkinter.IntVar()

scale=tkinter.Scale(window, variable=var, command=select, orient="vertical", showvalue=False, tickinterval=150, to=550, length=100)
scale.pack()
label=tkinter.Label(window, text="servo1 : 0")
label.pack()

window.mainloop()

# from tkinter import *
# from typing import List

# master = Tk()
# #First Scale
# sc=Scale(master, from_=0, to=100,orient=VERTICAL) 
# sc.pack() 

# value = "servo : "+str(sc.get())
# label.config(text=value)

# label=Tk.Label(master, text="servo1 : 0")
# label.pack()

# mainloop()