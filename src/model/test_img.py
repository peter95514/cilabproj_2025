from ultralytics import YOLO
import os

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model = YOLO(os.path.join(root, "runs/"))

results = model(os.path.join(root, "data/"))
results[0].plot()
