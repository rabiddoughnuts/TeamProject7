from ultralytics import YOLO
import sys
import os


def main():
    
    images_with_death_star_detected = {}

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
            confidence_scores = result[0].boxes.conf
            best_conf = max(confidence_scores)
            
            print(f"Best confidence for {file}: {best_conf}")
            
            # store the name and the result type to use later
            images_with_death_star_detected[(filename, result[0])] = best_conf

    sorted_images = sorted(images_with_death_star_detected.items(), key=lambda x: x[1], reverse=True)

    top_10_images = sorted_images[:10] # last 10, goes from lower conf -> high conf

    # horrible iterator im sorry
    for prefix_index, ((image_path, result), conf) in enumerate(top_10_images):
        # file = os.path.basename(image_path)
        # prefix = str(prefix_index).zfill(2)
        new_path = os.path.join(output_dir, f"{prefix_index}.jpg")
        
        result.save(new_path)
        print(f"Saved {new_path} with confidence: {conf}")


if __name__ == "__main__":
    main()
