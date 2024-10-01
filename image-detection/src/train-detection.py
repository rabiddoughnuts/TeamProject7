from ultralytics import YOLO
import sys

model = YOLO('yolov8n.pt')  # default pre trained
epochs = int(sys.argv[1])

model.train(
    data='./roboflow/data.yaml',
    epochs=epochs,
    imgsz=640,
    batch=16,
    workers=4
)

model.val()

model.export(format='onnx')
