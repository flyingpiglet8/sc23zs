# This script selects categories with insufficient amounts of YOLO data to achieve data 
# balance across the entire dataset by iteratively augmenting them with multiple data 
# augmentation methods. TARGET-COUNT is the target number of categories per category, 
# which is generally determined by the category with the largest number in this dataset.
import cv2
import os
from glob import glob
from tqdm import tqdm
import shutil
import albumentations as A

emotions = ['surprise', 'fear', 'disgust', 'happiness', 'sadness', 'anger', 'neutral']
TARGET_COUNT = 8000
IMAGE_DIR = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB-detection(images+labels)/original'
LABEL_DIR = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB-detection(images+labels)/RAFDB_all_labels'
AUGMENTED_IMAGE_DIR = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB_Detection_balance/images'
AUGMENTED_LABEL_DIR = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB_Detection_balance/labels'

os.makedirs(AUGMENTED_IMAGE_DIR, exist_ok=True)
os.makedirs(AUGMENTED_LABEL_DIR, exist_ok=True)

image_files = glob(os.path.join(IMAGE_DIR, '*.jpg'))
label_files = glob(os.path.join(LABEL_DIR, '*.txt'))

category_counts = {emotion: 0 for emotion in emotions}
single_category_files = {emotion: [] for emotion in emotions}

for label_file in label_files:
    with open(label_file, 'r') as file:
        lines = file.readlines()
        if len(lines) == 1:
            category_idx = int(lines[0].split()[0])
            category = emotions[category_idx]
            image_file = label_file.replace(LABEL_DIR, IMAGE_DIR).replace('.txt', '.jpg')
            single_category_files[category].append((image_file, label_file))
        for line in lines:
            category_idx = int(line.split()[0])
            category = emotions[category_idx]
            category_counts[category] += 1
print("Initial category counts:")
for category, count in category_counts.items():
    print(f"{category}: {count} instances")

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    # A.VerticalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.HueSaturationValue(p=0.5),
    A.Rotate(limit=(5,10), p=0.5),
    A.CLAHE(clip_limit=2.0, tile_grid_size=(8, 8), p=0.5)  
])

for image_file in image_files:
    shutil.copy(image_file, AUGMENTED_IMAGE_DIR)

for label_file in label_files:
    shutil.copy(label_file, AUGMENTED_LABEL_DIR)

total_augmentations_needed = sum(max(0, TARGET_COUNT - count) for count in category_counts.values())

print("\nStarting data augmentation...")
with tqdm(total=total_augmentations_needed, unit=' instances') as pbar:
    for category, files in single_category_files.items():
        while category_counts[category] < TARGET_COUNT:
            for image_file, label_file in files:
                if category_counts[category] >= TARGET_COUNT:
                    break
                image = cv2.imread(image_file)
                augmented = transform(image=image)
                augmented_image = augmented['image']
                base_name = os.path.basename(image_file)
                augmented_image_file = os.path.join(AUGMENTED_IMAGE_DIR, f'{category}_{category_counts[category]}_{base_name}')
                augmented_label_file = os.path.join(AUGMENTED_LABEL_DIR, f'{category}_{category_counts[category]}_{os.path.basename(label_file)}')
                cv2.imwrite(augmented_image_file, augmented_image)
                shutil.copy(label_file, augmented_label_file)
                category_counts[category] += 1
                pbar.update(1)

print("\nAugmented category counts:")
for category, count in category_counts.items():
    print(f"{category}: {count} instances")

print("\nData augmentation completed!")
