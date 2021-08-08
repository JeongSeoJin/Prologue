from time import sleep
import RPi.GPIO as GPIO

DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 13
# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14,15,18)
GPIO.setup(MODE, GPIO.OUT)
resolution = {'Full': (0, 0, 0),
'Half':(1, 0, 0),
'1/4':(0, 1, 0),
'1/8':(1, 1, 0),
'1/16':(0, 0, 1),
'1/32':(1, 0, 1)}

GPIO.output(MODE, resolution['1/16'])
step_count = SPR * 16
delay = .0208 / 16
# delay = .005 / 16
# delay = .04 / 16

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)

# GPIO.cleanup()