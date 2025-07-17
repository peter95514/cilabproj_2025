from ultralytics import YOLO
import os

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model = YOLO(os.path.join(root, "runs/detect/lung_tumor_model_ver1.05/weights/best.pt"))

results = model(os.path.join(root, "data/all/1.3.6.1.4.1.14519.5.2.1.6655.2359.112545118683956537398940148278.png"))
results[0].plot()
