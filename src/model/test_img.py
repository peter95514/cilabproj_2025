from ultralytics import YOLO
import os
import cv2

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
img_name = os.path.join(root, "data/all/1.3.6.1.4.1.14519.5.2.1.6655.2359.101411016698781974352422695665.png")

model = YOLO(os.path.join(root, "runs/detect/lung_tumor_model_ver2.1_100/weights/best.pt"))

results = model(img_name)
result = results[0].plot()

output_path = os.path.join(root, "data/output_pre_img")
os.makedirs(output_path, exist_ok=True)

cv2.imwrite(os.path.join(output_path, os.path.basename(img_name)), result)
