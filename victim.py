from ultralytics import YOLO

from config import *

model = YOLO("model/best.pt")

def detect(frame):

    results = model(
        frame,
        conf=CONFIDENCE,
        verbose=False
    )

    victims=[]

    for r in results:

        for box in r.boxes:

            cls=int(box.cls)

            label=model.names[cls]

            victims.append(label)

    return victims