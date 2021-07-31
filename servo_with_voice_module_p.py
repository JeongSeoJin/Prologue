import os
import pyttsx3
import speech_recognition as sr
import sys
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


class pythonhub:
    def takeCommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            r.pause_threshold = 0.7
            audio = r.listen(source)
            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language="en-in")

                print("the query is printed='" + Query + "'")
            except Exception as e:
                print(e)
                print("Say that again sir")
                return "None"

        return Query

    def pat(self, answer):
        self.speak("{}".format(answer))
        print(answer)

    def commands(self, sentences):
        print(sentences)
        self.speak("{}".format(sentences))
        take = self.takeCommands()
        choice = take
        if "shut down" in choice:
            self.pat("Ok, shut down the system")
            self.shutdown()
        
        if "show my list" in choice:
            self.pat("show your lists in the current directory")
            # os.system("dir")

        if "rotate my servo"   in choice:
            self.move_servo_with_voice()


    def speak(self, audio):            
        engine = pyttsx3.init()
        # voices = engine.getProperty('voices')
        # engine.setProperty('voice', voices[1].id)
        newVoiceRate = 145
        engine.setProperty('rate',newVoiceRate)
        engine.say(audio)
        engine.runAndWait()

    def shutting_system(self, answer, answer2):
        self.speak("do u want to switch off the computer sir")
        take = self.takeCommands()
        choice = take
        if answer in choice:
            print("Shutting dowm the computer")
            self.speak("Shutting the computer")
            os.system("dir")
        if answer2 in choice:
            print("Thank u sir")
            self.speak("Thank u sir")

    def move_servo_with_voice(self):
        self.pat("only speak the degrees")
        degree_value = self.takeCommands()
        print("you rotated your servo to {}".format(degree_value))
        setServoPos(int(degree_value))

    def starting(self):
        self.speak("Friday has been activated")

    def hello(self, answer):
        take = self.takeCommands()
        choice = take
        if answer in choice:
            self.commands("yes sir")
            
    
    def shutdown(self):
        self.speak("Friday has been unactivated")
        sys.exit()


# if __name__ == "__main__":
#     a = pythonhub()
#     # a.shutting_system("shut down", "no")
#     a.move_servo_with_voice()
