# import os
import pyttsx3
import speech_recognition as sr
# import sys

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

                print("the query is printed='", Query, "'")
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
        if choice in "shut down":
            self.pat("Ok, shutting down")
            self.shutdown()
        
        if choice in "show my list":
            self.pat("show your lists in the current directory")
            # os.system("dir")

    def speak(self, audio):            
        engine = pyttsx3.init("sapi5")
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
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
        self.speak("Speak the degree that you want to rotate to your servo")
        take = self.takeCommands()
        print("Servo has steered to {} degree".format(take))

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


# if __name__ == "__main__":
#     a = pythonhub()
#     # a.move_servo_with_voice()
#     a.starting()
#     while True:
#         a.hello("Friday")