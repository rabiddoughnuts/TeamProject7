import cv2
import numpy as np
import sys
import os

# https://github.com/ChristophRahn/red-circle-detection/blob/master/red-circle-detection.py
def detect_red_circle(image_path):
    image = cv2.imread(image_path)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

    red_mask = cv2.bitwise_or(mask1, mask2)

    masked_image = cv2.bitwise_and(image, image, mask=red_mask)

    gray_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 2)

    circles = cv2.HoughCircles(blurred_image, cv2.HOUGH_GRADIENT, dp=1.2, minDist=50,
                               param1=100, param2=30, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        x, y, r = circles[0]
        return (x, y, r)
    else:
        return None


def crop_circle(image, x, y, r):
    top_left_x = max(0, x - r)
    top_left_y = max(0, y - r)
    bottom_right_x = min(image.shape[1], x + r)
    bottom_right_y = min(image.shape[0], y + r)

    cropped_image = image[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

    return cropped_image


def main():
    
    # paths should have already been resolved
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    
    files = [file for file in os.listdir(in_dir) if file.endswith(".jpg")] # think we only need to support png files?
    
    file_index = 0
    for file in files:
        full_path = os.path.join(in_dir, file)
        result = detect_red_circle(full_path)

        if result:
            x, y, r = result
            print(f"Red circle found at (x: {x}, y: {y}) with radius {r}")

            image = cv2.imread(full_path)

            cropped_image = crop_circle(image, x, y, r)

            path_of_cropped = os.path.join(out_dir, f"{file_index}-file.png")
            file_index += 1
            
            print(f"Path to cropped: {path_of_cropped}")
            cv2.imwrite(path_of_cropped, cropped_image)
            print(f"Cropped image saved to {out_dir}")  
        else:
            print("No red circle detected in img.")

if __name__ == "__main__":
    main()
