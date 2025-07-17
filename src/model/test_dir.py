import os
from ultralytics import YOLO 

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
model = YOLO("runs/...")

target_dir = os.path.join(root, "data/")

img_ls = []

for f in os.listdir(target_dir):
    if(f.endswith(".png")):
        img_ls.append(f)

result = model(img_ls)

index = 0
total = len(img_ls)

while True:

