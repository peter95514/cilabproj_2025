from ultralytics import YOLO
import os
from ultralytics.utils import cv2

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

model = YOLO(os.path.join(root, "runs/"))

results = model(os.path.join(root, "data/"))

save_path = os.path.join(root, "data/output_temp_pre")
os.makedirs(save_path, exist_ok=True)

cv2.imwrite(os.path.join(save_path, ".png"), results[0].plot())
