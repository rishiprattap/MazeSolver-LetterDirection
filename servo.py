from gpiozero import AngularServo
from time import sleep

from config import *

servo = AngularServo(
    SERVO_PIN,
    min_angle=-90,
    max_angle=90
)

def drop_kit():

    servo.angle = 60

    sleep(DROP_TIME)

    servo.angle = -60

    sleep(DROP_TIME)

    servo.angle = 0