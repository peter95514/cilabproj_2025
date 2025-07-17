from ultralytics import YOLO
import os
import cv2

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
img_name = os.path.join(root, "data/all/images.jpg")

model = YOLO(os.path.join(root, "runs/detect/lung_tumor_model_ver2.02/weights/best.pt"))

results = model(img_name)
result = results[0].plot()

output_path = os.path.join(root, "data/output_pre_img")
os.makedirs(output_path, exist_ok=True)

cv2.imwrite(os.path.join(output_path, os.path.basename(img_name)), result)
