import os
import shutil
import random

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

img_dir = os.path.join(root, "data/")
txt_dir = os.path.join(root, "data/")

train_dir = os.path.join(root, "data", "train")
val_dir = os.path.join(root, "data", "val")

os.makedirs(val_dir, exist_ok= True)
os.makedirs(train_dir, exist_ok= True)

image = [f for f in os.listdir(os.path.join(img_dir, "all")) if f.endswith(".png")]
random.shuffle(image)

ratio = 0.8
spilt_idx = int(len(image) * ratio)

train = image[:spilt_idx]
val = image[spilt_idx:]

for obj in train:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(train_dir, obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(train_dir, obj.replace(".png", ".txt")))

for obj in val:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(val_dir, obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(val_dir, obj.replace(".png", ".txt")))
