from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "data.yaml",
        epochs = 150,
        imgsz = 512,
        batch = 32,
        device = 0,  # 明確指定用外顯
        workers = 8,
        optimizer = "Adam",
        cache = "disk",
        name = "lung_tumor_model_ver3.1_150_32_else"
    )

    model.val()

if __name__ == "__main__":
    main()
