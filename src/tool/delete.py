import os

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

target_dir = os.path.join(root, "data/all")

obj = []
for f in os.listdir(target_dir):
    if f.endswith(".txt"):
        txt_path = os.path.join(target_dir, f)
        if (os.path.getsize(txt_path) == 0):
            os.remove(os.path.join(target_dir, f.replace(".txt", ".png")))
            print("remove: ", f)
            os.remove(os.path.join(txt_path))
