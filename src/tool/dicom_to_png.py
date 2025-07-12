import os
import pydicom
from tqdm import tqdm
import numpy as np
from PIL import Image

input_folder = r"C:\Users\wu096\OneDrive桌面資料集\manifest-1608669183333\Lung-PET-CT-Dx"
output_folder = r"C:\Users\wu096\OneDrive桌面轉好的圖"

for dirpath, dirnames, filenames in tqdm(list(os.walk(input_folder)), desc=":rocket: 正在處理中"):
    for filename in filenames:
        if filename.endswith(".dcm"):
            dcm_path = os.path.join(dirpath, filename)

            try:
                ds = pydicom.dcmread(dcm_path)
                img = ds.pixel_array.astype(np.float32)

                img -= np.min(img)
                if np.max(img) != 0:
                    img /= np.max(img)
                img *= 255.0
                img = img.astype(np.uint8)

                relative_path = os.path.relpath(dirpath, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, filename.replace(".dcm", ".png"))
                Image.fromarray(img).save(output_path)

                print(":white_check_mark: 已轉換：", output_path)

            except Exception as e:
                print(":warning: 發生錯誤：", dcm_path)
                print("   ➤", e)

print("\n:tada: 全部轉換完成！PNG 儲存在：", output_folder)
