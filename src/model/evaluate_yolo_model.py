import os
import csv
import matplotlib.pyplot as plt
from ultralytics import YOLO

# === 基本設定 ===
MODEL_PATH = "/root/cilabproj_2025/runs/detect/lung_tumor_model_ver3.1_150_32_else/weights/best.pt"
DATA_YAML = "data.yaml"
VAL_IMAGES_DIR = "/root/cilabproj_2025/data/val"
CONF_THRESHOLD = 0.3

# === 載入模型 ===
model = YOLO(MODEL_PATH)

# === 計算訓練與驗證集評估指標 ===
train_metrics = model.val(data=DATA_YAML, split="train")
val_metrics = model.val(data=DATA_YAML, split="val")

# === 輸出評估指標 ===
def print_metrics(name, metrics):
    mp, mr, map50, map = metrics.box.mean_results()
    f1 = 2 * (mp * mr) / (mp + mr + 1e-6)

    print(f"\n📊 [{name} Set Evaluation]")
    print(f"Precision:      {mp:.4f}")
    print(f"Recall:         {mr:.4f}")
    print(f"mAP@0.5:        {map50:.4f}")
    print(f"mAP@0.5:0.95:   {map:.4f}")
    print(f"F1-score:       {f1:.4f}")

print_metrics("Train", train_metrics)
print_metrics("Validation", val_metrics)

# === 載入驗證集圖片清單 ===
def load_images_from_dir(img_dir):
    return [os.path.join(img_dir, f) for f in os.listdir(img_dir) if f.endswith(".png")]

val_images = load_images_from_dir(VAL_IMAGES_DIR)

# === 模型預測驗證集（stream=True 省記憶體）===
results = list(model(val_images, stream=True))

# === 低信心預測分析 ===
print("\n🧐 低信心預測框 (Confidence < 0.3):")
for result in results:
    for box in result.boxes:
        conf = box.conf[0].item()
        if conf < CONF_THRESHOLD:
            cls = int(box.cls[0])
            print(f"[{os.path.basename(result.path)}] Class: {model.names[cls]}, Confidence: {conf:.2f}")

# === 儲存預測結果至 CSV ===
csv_file = "results/yolo_predictions.csv"
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Image", "Class", "Confidence", "X1", "Y1", "X2", "Y2"])
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = box.conf[0].item()
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            writer.writerow([os.path.basename(result.path), model.names[cls], conf, x1, y1, x2, y2])

print(f"\n✅ 已將預測結果儲存至 {csv_file}")

# === PR Curve ===
if hasattr(val_metrics.box, "pr_curves"):
    pr_curves = val_metrics.box.pr_curves
    plt.figure()
    for i, curve in enumerate(pr_curves):
        if curve.shape[1] >= 2:
            precision = curve[:, 0]
            recall = curve[:, 1]
            plt.plot(recall, precision, label=f"{model.names[i]}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title("Precision-Recall Curve")
    plt.grid(True)
    plt.legend()
    plt.show()
else:
    print("⚠️ 無法產生 PR 曲線：`pr_curves` 不存在。")

