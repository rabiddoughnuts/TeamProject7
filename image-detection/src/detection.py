from ultralytics import YOLO
import sys
import os
import shutil


def main():

    directory = sys.argv[1]

    directory = os.path.abspath(directory)

    weights = './runs/detect/train/weights/best.pt'

    model = YOLO(weights)

    for i, file in enumerate(os.listdir(directory)):
        
        filename = os.path.join(directory, file)
        # print(filename)
        result = model(filename)
        
        
        
        
        
        boxes = result[0].boxes.xyxy

        detected_death_star = len(boxes) != 0
        print(detected_death_star)
        
        if detected_death_star:
            # this may need to like do the cropping n stuff here. but for now, this works
            new_path = os.path.join("./out", file)
            print(new_path)
            
            result[0].save(new_path)
            # new_path = os.path.join("./out", file)
            # shutil.copyfile(filename, new_path)
        

    # results = model('examples/testMe.jpeg')

    # results[0].save("results.png")


if __name__ == "__main__":
    main()
