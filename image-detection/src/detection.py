from ultralytics import YOLO


def main():
    model = YOLO('./runs/detect/train/weights/best.pt')

    results = model('examples/testMe.jpeg')

    results[0].save("results.png")
    

if __name__ == "__main__":
    main()