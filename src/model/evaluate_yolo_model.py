import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# === 基本設定 ===
MODEL_PATH = "/root/cilabproj_2025/runs/detect/lung_tumor_model_ver2.1_100/weights/best.pt"
DATA_YAML = "data.yaml"
TRAIN_IMAGES_DIR = os.path.join("..", "..", "data", "train", "images")
VAL_IMAGES_DIR = "/root/cilabproj_2025/data/val"
CONF_THRESHOLD = 0.3

# === 載入模型 ===
model = YOLO(MODEL_PATH)

# === 計算訓練與驗證集評估指標 ===
train_metrics = model.val(data=DATA_YAML, split="train")
val_metrics = model.val(data=DATA_YAML, split="val")

# === 輸出評估指標（修正版） ===
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

# === 模型預測驗證集 ===
results = model(val_images)

# === 混淆矩陣資料收集 ===
y_true = []
y_pred = []

for result in results:
    # 真實標註
    label_path = result.path.replace("images", "labels").replace(".png", ".txt")
    if os.path.exists(label_path):
        with open(label_path, "r") as f:
            for line in f:
                cls_id = int(line.strip().split()[0])
                y_true.append(cls_id)

    # 預測類別
    for box in result.boxes:
        pred_cls = int(box.cls[0])
        y_pred.append(pred_cls)

# === 混淆矩陣繪製 ===
if y_true and y_pred:
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.names)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix (Validation Set)")
    plt.show()
else:
    print("⚠️ 混淆矩陣資料不足，無法生成。")

# === Precision-Recall 曲線 ===
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

