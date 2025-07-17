import os

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

target_dir = os.path.join(root, "data/")

obj = []
for f in os.listdir(target_dir):
    if f.endswith(".txt"):
        if (os.path.getsize(f) == 0):
            os.remove(f.replace(".txt", ".png"))
            print("remove: ", f)
            os.remove(f)
