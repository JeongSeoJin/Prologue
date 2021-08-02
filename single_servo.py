import RPi.GPIO as GPIO
from time import sleep 

servoPin          = 12 
SERVO_MAX_DUTY    = 12   
SERVO_MIN_DUTY    = 3   

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(servoPin, GPIO.OUT) 

servo = GPIO.PWM(servoPin, 50)  
servo.start(0)  

def setServoPos(degree):

  if degree > 180:
    degree = 180


  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)

  print("Degree: {} to {}(Duty)".format(degree, duty))

  servo.ChangeDutyCycle(duty)


if __name__ == "__main__":  

  # setServoPos(5)
  # sleep(1)
 
  # setServoPos(90)
  # sleep(1)

  # setServoPos(175)
  # sleep(1)
  while True:
    value = int(input(" Degree : "))

    if value == 9:
      value = 180
      setServoPos(value)

    if value == 0:
      value = 0
      setServoPos(value)

  servo.stop()

  GPIO.cleanup()