import os
import pydicom
import numpy as np
from PIL import Image

# 設定資料夾路徑（這邊用 os.walk 遞迴處理）
input_root = r"C:\Users\wu096\OneDrive\桌面\資料集\manifest-1608669183333\Lung-PET-CT-Dx"
output_root = r"C:\Users\wu096\OneDrive\桌面\轉好的圖_UID命名"

for root, dirs, files in os.walk(input_root):
    print(dirs)
    for file in files:
        if file.endswith(".dcm"):
            dcm_path = os.path.join(root, file)
            ds = pydicom.dcmread(dcm_path)

            # 取得 UID 當檔名
            uid = ds.SOPInstanceUID
            
            # 轉成影像並標準化
            img = ds.pixel_array.astype(np.float32)
            img -= np.min(img)
            img /= np.max(img)
            img *= 255.0
            img = img.astype(np.uint8)

            # 儲存路徑（按照原始資料夾階層儲存）
            relative_path = os.path.relpath(root, input_root)
            output_folder = os.path.join(output_root, relative_path)
            os.makedirs(output_folder, exist_ok=True)

            output_path = os.path.join(output_folder, f"{uid}.png")
            Image.fromarray(img).save(output_path)

print("✅ 所有 DICOM 已轉為以 UID 命名的 PNG 檔")

