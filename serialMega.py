import serial

from config import *

mega = serial.Serial(
    MEGA_PORT,
    BAUDRATE,
    timeout=0.1
)

def stop_robot():
    mega.write(b"STOP\n")

def go_robot():
    mega.write(b"GO\n")

def send_victim(letter):
    mega.write((letter+"\n").encode())