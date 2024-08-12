# This script is used to convert the RAF-DB dataset into a format for YOLO target detection.
#  Note that the conversion requires the use of RAF-DB face alignment label files 
# and that some of the positioning labels need to be manually homebrewed after the conversion is complete.
import os
from PIL import Image

with open('/Users/piglet/Desktop/Project_Code/RAFDB/list_patition_label.txt', 'r') as f:
    lines = f.readlines()

image_label_dict = {}
for line in lines:
    parts = line.strip().split()
    image_name = parts[0]
    label = int(parts[1]) - 1 
    image_label_dict[image_name] = label

image_folder = '/Users/piglet/Desktop/Project_Code/RAFDB/original'  
boundingbox_folder = '/Users/piglet/Desktop/Project_Code/RAFDB/boundingbox'
output_folder = '/Users/piglet/Desktop/Project_Code/RAFDB/YOLO_OB_labels_3'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for image_name, label in image_label_dict.items():
    image_path = os.path.join(image_folder, image_name)
    boundingbox_file = os.path.join(boundingbox_folder, image_name.replace('.jpg', '_boundingbox.txt'))
    
    if os.path.exists(image_path) and os.path.exists(boundingbox_file):
        with Image.open(image_path) as img:
            image_width, image_height = img.size
        with open(boundingbox_file, 'r') as f:
            bbox = f.readline().strip().split()
            x_min, y_min, x_max, y_max = map(float, bbox)
            cx = (x_min + x_max) / 2.0
            cy = (y_min + y_max) / 2.0
            w = x_max - x_min
            h = y_max - y_min
            cx /= image_width
            cy /= image_height
            w /= image_width
            h /= image_height
            yolo_label = f"{label} {cx:.8f} {cy:.8f} {w:.8f} {h:.8f}\n"
            output_file = os.path.join(output_folder, image_name.replace('.jpg', '.txt'))
            with open(output_file, 'w') as out_f: 
                out_f.write(yolo_label)
    
        print(f"Processed {image_name}: {yolo_label.strip()}")
    else:
        print(f"File not found: {image_path} or {boundingbox_file}")

print("YOLO format label files have been generated.")