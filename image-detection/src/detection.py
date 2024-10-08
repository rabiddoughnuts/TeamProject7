from ultralytics import YOLO
import sys
import os
import shutil


def main():

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    weights = './runs/detect/train/weights/best.pt'

    model = YOLO(weights)
    
    prefix_index = 0

    for i, file in enumerate(os.listdir(input_dir)):
        
        
        filename = os.path.join(input_dir, file)
        # print(filename)
        result = model(filename)
        
        boxes = result[0].boxes.xyxy

        detected_death_star = len(boxes) != 0
        
        
        
        if detected_death_star:
            
            prefix = str(prefix_index).zfill(2)
            prefix_index += 1
            
            # this may need to like do the cropping n stuff here. but for now, this works
            new_path = os.path.join(output_dir, f"{prefix}-{file}")
            print(result[0].boxes.conf)
            
            result[0].save(new_path)
            # new_path = os.path.join("./out", file)
            # shutil.copyfile(filename, new_path)
        

    # results = model('examples/testMe.jpeg')

    # results[0].save("results.png")


if __name__ == "__main__":
    main()
