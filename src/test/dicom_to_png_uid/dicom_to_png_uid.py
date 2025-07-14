import os
import pydicom
import numpy as np
from PIL import Image

def convert_dicom_to_png_with_uid(input_root, output_root):
    count = 0
    for root, dirs, files in os.walk(input_root):
        for file in files:
            if file.endswith(".dcm"):
                try:
                    dcm_path = os.path.join(root, file)
                    ds = pydicom.dcmread(dcm_path)

                    # 用 UID 當檔名
                    uid = ds.SOPInstanceUID

                    # 影像轉換與標準化
                    img = ds.pixel_array.astype(np.float32)
                    img -= np.min(img)
                    img /= np.max(img)
                    img *= 255.0
                    img = img.astype(np.uint8)

                    # 保留原始資料夾結構
                    relative_path = os.path.relpath(root, input_root)
                    output_folder = os.path.join(output_root, relative_path)
                    os.makedirs(output_folder, exist_ok=True)

                    output_path = os.path.join(output_folder, f"{uid}.png")
                    Image.fromarray(img).save(output_path)
                    count += 1
                except Exception as e:
                    print(f"⚠️ 無法處理 {file}: {e}")
    print(f"✅ 成功轉換 {count} 張 DICOM → PNG")

# ✅ 修改成你自己的路徑
input_root = r"C:\Users\wu096\OneDrive\桌面\資料集\manifest-1608669183333\Lung-PET-CT-Dx"
output_root = r"C:\Users\wu096\OneDrive\桌面\轉好的圖"

# ✅ 執行轉檔
convert_dicom_to_png_with_uid(input_root, output_root)

