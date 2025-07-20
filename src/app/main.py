import os
import shutil

save_number = 0

root = __file__
input_img_temp = os.path.join(root, "input_img_temp")
output_img_temp = os.path.join(root, "output_img_temp")

os.makedirs(output_img_temp, exist_ok=True)
os.makedirs(input_img_temp, exist_ok=True)

def transfer():

    return

def upload_img(path):
    
    obj = os.path.basename(path)
    ext = os.path.splitext(obj)[1].lower()

    if ext not in [".png", ".jpg"]:
        return "its not img"
    
    con = True

    for file in os.listdir(input_img_temp):
        if (os.path.basename(file) == os.path.basename(path)):
            con = False
            break

    if con:
        return

    shutil.copyfile(path, os.path.join(output_img_temp, os.path.basename(path))) 
    transfer()
    return

def upload_dir(path):

    for file in os.listdir(path):
        upload_img(file)
    
    transfer()
    return 

def main():
    
    #finish
    shutil.rmtree(input_img_temp)
    shutil.rmtree(output_img_temp)

    return

if __name__ == "__main__":
    main()
