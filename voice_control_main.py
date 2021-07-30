from voice_recog_module import *

if __name__ == "__main__":
    a = pythonhub()
    # a.move_servo_with_voice()
    a.starting()
    while True:
        a.hello("Friday")