import time
import Adafruit_PCA9685

servo = Adafruit_PCA9685.PCA9685()
servo_min = 150
servo_max = 550

def map(value, min_angle, max_angle, min_pulse, max_pulse):
	angle_range = max_angle - min_angle
	pulse_range = max_angle - min_pulse
	scale_factor = float(angle_range)/float(pulse_range)
	return min_pulse+(value/scale_factor)

def set_angle(channel, angle):
	pulse = int(map(angle, 0, 180, servo_min, servo_max))
	servo.set_pwm(channel, 0, pulse)

servo.set_pwm_freq(60)

while True:
	set_angle(0, 90)
	time.sleep(1)
	set_angle(1, 90)
	time.sleep(1)
	set_angle(2, 90)
	time.sleep(1)
	set_angle(3, 90)
	time.sleep(1)
	set_angle(4, 90)
	time.sleep(1)
	set_angle(5, 90)
	print("they are in 90 degrees")
	time.sleep(1)

	set_angle(0, 180)
	time.sleep(1)
	set_angle(1, 180)
	time.sleep(1)
	set_angle(2, 180)
	time.sleep(1)
	set_angle(3, 180)
	time.sleep(1)
	set_angle(4, 180)
	time.sleep(1)
	set_angle(5, 180)
	print("they are in 180 degrees")
	time.sleep(1)

	set_angle(0, 0)
	time.sleep(1)
	set_angle(1, 0)
	time.sleep(1)
	set_angle(2, 0)
	time.sleep(1)
	set_angle(2, 0)
	time.sleep(1)
	set_angle(4, 0)
	time.sleep(1)
	set_angle(5, 0)
	print("they are in 0 degrees")
	time.sleep(1)