from ultralytics import YOLO

# Load a small pretrained YOLO model
model = YOLO("yolo11n.pt")

# Train the model
results = model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    device=0,
    workers=0
)

print("Training completed!")