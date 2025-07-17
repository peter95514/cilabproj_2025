from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "data.yaml",
        epochs = 50,
        imgsz = 512,
        batch = 16,
        name="lung_tumor_model_ver2.0"
    )

    model.val()

if __name__ == "__main__":
    main()
