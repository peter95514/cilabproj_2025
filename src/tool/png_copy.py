import os
import shutil
source_dir = r"C:\Users\wu096\OneDrive\桌面\DICOM_UID"
output_dir = r"\\wsl.localhost\Ubuntu-22.04\root\cilabproj_2025\data\png_temp_1"

os.makedirs(output_dir, exist_ok=True)

def first_dir(path):
    subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    if not subfolders:
        return None
    # 根據名稱排序後取第一個
    subfolders.sort()
    return os.path.join(path, subfolders[0])

def throw():

    for sub_dir_1 in os.listdir(source_dir):
        sub_1_path = os.path.join(source_dir, sub_dir_1)
        print(sub_dir_1)

        for sub_dir_2 in os.listdir(sub_1_path):
            sub_2_path = os.path.join(sub_1_path, sub_dir_2)

            temp_path = first_dir(sub_2_path)
            for file in os.listdir(temp_path):
                src_path = os.path.join(temp_path, file)
                dst_path = os.path.join(output_dir, file)
                shutil.move(src_path, dst_path)
throw()
