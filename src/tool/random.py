import os
import shutil
import random

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

img_dir = os.path.join(root, "data/")
txt_dir = os.path.join(root, "data/")

image = os.listdir(os.path.join(img_dir, "all"))
random.shuffle(image)

ratio = 0.8
spilt_idx = int(len(image) * ratio)

train = image[:spilt_idx]
val = image[spilt_idx:]

for obj in train:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(img_dir, "train", obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(txt_dir, "train", obj.replace(".png", ".txt")))

for obj in val:
    shutil.copyfile(os.path.join(img_dir, "all", obj), os.path.join(img_dir, "val", obj))
    shutil.copyfile(os.path.join(txt_dir, "all", obj.replace(".png", ".txt")), os.path.join(txt_dir, "val", obj.replace(".png", ".txt")))
