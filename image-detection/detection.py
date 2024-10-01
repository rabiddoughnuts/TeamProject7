from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')

results = model('testMe.jpeg')

results[0].save("results.png")
