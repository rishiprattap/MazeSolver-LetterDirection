from camera import *

from victim_detector import *

from serial_mega import *

from servo import *

while True:

    frame=get_frame()

    victims=detect(frame)

    if len(victims)>0:
        stop_robot()

        letter=victims[0]

        send_victim(letter)

        drop_kit()

        go_robot()