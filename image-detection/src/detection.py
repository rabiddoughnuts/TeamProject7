from ultralytics import YOLO
import sys
import os


def main():

    directory = sys.argv[1]

    directory = os.path.abspath(directory)

    weights = './runs/detect/train/weights/best.pt'

    model = YOLO(weights)

    for file in os.listdir(directory):
        
        filename = os.path.join(directory, file)
        # print(filename)
        result = model(filename)
        
        boxes = result[0].boxes.xyxy

        detected_images = len(boxes) != 0
        print(detected_images)
        

    # results = model('examples/testMe.jpeg')

    # results[0].save("results.png")


if __name__ == "__main__":
    main()
