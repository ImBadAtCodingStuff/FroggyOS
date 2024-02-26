from gpiozero import Servo
from time import sleep

def turn_angle(angle, servo = Servo(17)):
        servo.value = angle


