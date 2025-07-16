from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data = "data.yaml",
        epochs = 70,
        imgsz = 512,
        batch = 16
    )

    model.val()

if __name__ == "__main__":
    main()
