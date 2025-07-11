#DCM轉PNG
import os
import pydicom
print(":white_check_mark: pydicom is installed and working!")

import numpy as np
from PIL import Image

#設定資料夾路徑
input_folder = r"讀取資料夾路徑(DCM檔)"
output_folder = r"輸出資料夾路徑(PNG檔)"

#建立輸出資料夾（如果不存在）
os.makedirs(output_folder, exist_ok=True)

#處理每一個 DICOM 檔案
for filename in os.listdir(input_folder):
    if filename.endswith(".dcm"):
        dcm_path = os.path.join(input_folder, filename)
        ds = pydicom.dcmread(dcm_path)

        # 抓出像素資料並標準化
        img = ds.pixel_array.astype(np.float32)
        img -= np.min(img)
        img /= np.max(img)
        img *= 255.0
        img = img.astype(np.uint8)

        # 儲存為 PNG
        img_pil = Image.fromarray(img)
        output_path = os.path.join(output_folder, filename.replace(".dcm", ".png"))
        img_pil.save(output_path)

print(":white_check_mark: 轉換完成！PNG 儲存在：", output_folder)
