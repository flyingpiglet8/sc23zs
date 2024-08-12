#This script is used to check if the name and number of label files and image 
# files in a YOLO format dataset are one-to-one correspondence. 
# It is used to check the quality of YOLO dataset.

import os
def get_filenames_without_extension(directory, extensions):
    return set(os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith(extensions))

def find_mismatched_files(image_dir, text_dir):
    image_files = get_filenames_without_extension(image_dir, ('.jpg', '.jpeg', '.png'))
    text_files = get_filenames_without_extension(text_dir, '.txt')
    
    images_without_texts = image_files - text_files
    texts_without_images = text_files - image_files
    
    return images_without_texts, texts_without_images

image_directory = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB_Detection_balance/images'
text_directory = '/Users/piglet/Desktop/Project_Code/RAFDB/workspace/RAFDB_Detection_balance/labels'

images_without_texts, texts_without_images = find_mismatched_files(image_directory, text_directory)

if not images_without_texts and not texts_without_images:
    print("All images and txt files correspond one to one.")
else:
    if images_without_texts:
        print("There is no image corresponding to the txt file:")
        for image in images_without_texts:
            print(image)

    if texts_without_images:
        print("\nThere is no txt file that corresponds to the image:")
        for text in texts_without_images:
            print(text)