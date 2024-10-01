from ultralytics import YOLO

model = YOLO('yolov8n.pt') # default pre trained  

model.train(
    data='./roboflow/data.yaml',    
    epochs=5,   
    imgsz=640,             
    batch=16,              
    workers=4              
)

model.val()

model.export(format='onnx') 
