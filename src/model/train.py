from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "data.yaml",
        epochs = 100,
        imgsz = 512,
        batch = 32,
        name="lung_tumor_model_ver2.1_100"
    )

    model.val()

if __name__ == "__main__":
    main()
