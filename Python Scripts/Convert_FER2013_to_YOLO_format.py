# This part of the code is used to convert the FER2013 dataset into a 
# format usable by YOLO. After the conversion, 
# the dataset can be split using the "Dataset_Splitting_YOLOformat.py" script.

import os
import pandas as pd
import numpy as np
from PIL import Image

csv_file = '/Users/piglet/Desktop/Project_Code/FER2013/fer2013.csv'
output_dir = '/Users/piglet/Desktop/Project_Code/FER2013/YOLO'
images_dir = os.path.join(output_dir, 'images')
labels_dir = os.path.join(output_dir, 'labels')

os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

data = pd.read_csv(csv_file)

labels_map = {
    0: 'angry',
    1: 'disgust',
    2: 'fear',
    3: 'happy',
    4: 'sad',
    5: 'surprise',
    6: 'neutral'
}

for index, row in data.iterrows():
    pixels = np.array(row['pixels'].split(), dtype=np.uint8)
    emotion = int(row['emotion'])
    
    img = pixels.reshape(48, 48)
    img = Image.fromarray(img)
    img_filename = f"{index}.jpg"
    img_path = os.path.join(images_dir, img_filename)
    img.save(img_path)
    
    label_filename = f"{index}.txt"
    label_path = os.path.join(labels_dir, label_filename)
    
    x_center = 0.5
    y_center = 0.5
    width = 1.0
    height = 1.0
    
    with open(label_path, 'w') as f:
        f.write(f"{emotion} {x_center} {y_center} {width} {height}")