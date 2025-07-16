import os
import shutil
import random

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

img_dir = os.path.join(root, "data/")
txt_dir = os.path.join(root, "data/")

txt_train_dir = os.path.join(root, "data/txt", "train")
txt_val_dir = os.path.join(root, "data/txt", "val")
img_train_dir = os.path.join(root, "data/img", "train")
img_val_dir = os.path.join(root, "data/img", "val")

os.makedirs(img_train_dir, exist_ok= True)
os.makedirs(img_val_dir, exist_ok= True)
os.makedirs(txt_train_dir, exist_ok= True)
os.makedirs(txt_val_dir, exist_ok= True)

image = os.listdir(os.path.join(img_dir, "all"))
random.shuffle(image)

ratio = 0.8
spilt_idx = int(len(image) * ratio)

train = image[:spilt_idx]
val = image[spilt_idx:]

for obj in train:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(img_train_dir, obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(txt_train_dir, obj.replace(".png", ".txt")))

for obj in val:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(img_val_dir, obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(txt_val_dir, obj.replace(".png", ".txt")))
