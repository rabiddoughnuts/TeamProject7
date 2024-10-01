from ultralytics import YOLO

model = YOLO('yolov8n.pt') # default pre trained  

model.train(
    data='./data.yaml',    
    epochs=50,            
    imgsz=640,             
    batch=16,              
    workers=4              
)

model.val()

model.export(format='onnx') 
