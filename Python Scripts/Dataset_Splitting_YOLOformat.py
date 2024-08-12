import os
import shutil
import random

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def move_files(file_list, src_img_dir, src_lbl_dir, dst_img_dir, dst_lbl_dir):
    for file in file_list:
        img_path = os.path.join(src_img_dir, file)
        lbl_path = os.path.join(src_lbl_dir, file.replace('.jpg', '.txt').replace('.png', '.txt'))

        if os.path.exists(img_path) and os.path.exists(lbl_path):
            shutil.move(img_path, dst_img_dir)
            shutil.move(lbl_path, dst_lbl_dir)

# Change the rate
def split_dataset(img_dir, lbl_dir, train_ratio=0.7, valid_ratio=0.2, test_ratio=0.1):
    images = [f for f in os.listdir(img_dir) if f.endswith(('.jpg', '.png'))]
    random.shuffle(images)

    total_count = len(images)
    train_count = int(total_count * train_ratio)
    valid_count = int(total_count * valid_ratio)

    train_files = images[:train_count]
    valid_files = images[train_count:train_count + valid_count]
    test_files = images[train_count + valid_count:]

    return train_files, valid_files, test_files

def main():
    img_dir = '/Users/piglet/Desktop/Project_Code/A/images'
    lbl_dir = '/Users/piglet/Desktop/Project_Code/A/labels'

    train_img_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/train/images'
    train_lbl_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/train/labels'
    valid_img_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/valid/images'
    valid_lbl_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/valid/labels'
    test_img_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/test/images'
    test_lbl_dir = '/Users/piglet/Desktop/Project_Code/expression(343)/test/labels'

    create_dir(train_img_dir)
    create_dir(train_lbl_dir)
    create_dir(valid_img_dir)
    create_dir(valid_lbl_dir)
    create_dir(test_img_dir)
    create_dir(test_lbl_dir)

    train_files, valid_files, test_files = split_dataset(img_dir, lbl_dir)

    move_files(train_files, img_dir, lbl_dir, train_img_dir, train_lbl_dir)
    move_files(valid_files, img_dir, lbl_dir, valid_img_dir, valid_lbl_dir)
    move_files(test_files, img_dir, lbl_dir, test_img_dir, test_lbl_dir)

    print("Dataset Splitting is complete!")

if __name__ == '__main__':
    main()
