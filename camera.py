from picamera2 import Picamera2

from config import *

camera = Picamera2()

config = camera.create_preview_configuration(
    main={
        "size": (CAMERA_WIDTH, CAMERA_HEIGHT)
    }
)

camera.configure(config)

camera.start()

def get_frame():
    return camera.capture_array()