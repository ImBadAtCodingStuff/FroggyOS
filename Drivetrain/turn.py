from gpiozero import Servo
from time import sleep

servo = Servo(17)

def turn_angle(angle, servo = servo):
        if angle > 1:
                angle = 1
        if angle < -1:
                angle = -1
        servo.value = angle
        
def turn_reset(servo = servo):
        servo.value = 0
        


