import albumentations as A
import cv2
import os
import yaml
import pybboxes as pbx


with open("contants.yaml", 'r') as stream:
    CONSTANTS = yaml.safe_load(stream)


def is_image_by_extension(file_name):
    """
    Check if the given file has a recognized image extension.

    Args:
        file_name (str): Name of the file.

    Returns:
        bool: True if the file has a recognized image extension, False otherwise.

    """
    # List of common image extensions
    image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'webp']
    # Get the file extension
    file_extension = file_name.lower().split('.')[-1]
    # Check if the file has a recognized image extension
    return file_extension in image_extensions


def get_inp_data(img_file):
    """
    Get input data for image processing.

    Args:
        img_file (str): Name of the input image file.

    Returns:
        tuple: A tuple containing the image, ground truth bounding boxes, and augmented file name.

    """
    file_name = os.path.splitext(img_file)[0]
    aug_file_name = f"{file_name}_{CONSTANTS['transformed_file_name']}"
    image = cv2.imread(os.path.join(CONSTANTS["inp_img_pth"], img_file))
    lab_pth = os.path.join(CONSTANTS["inp_lab_pth"], f"{file_name}.txt")
    gt_bboxes = get_bboxes_list(lab_pth, CONSTANTS['CLASSES'])
    return image, gt_bboxes, aug_file_name


def get_album_bb_list(yolo_bbox, class_names):
    """
    Extracts bounding box information for a single object from YOLO format.

    Args:
        yolo_bbox (str): YOLO format string representing bounding box information.
        class_names (list): List of class names corresponding to class numbers.

    Returns:
        list: A list containing [x_center, y_center, width, height, class_name].
    """
    str_bbox_list = yolo_bbox.split()
    class_number = int(str_bbox_list[0])
    class_name = class_names[class_number]
    bbox_values = list(map(float, str_bbox_list[1:]))
    album_bb = bbox_values + [class_name]
    return album_bb


def get_album_bb_lists(yolo_str_labels, classes):
    """
    Extracts bounding box information for multiple objects from YOLO format.

    Args:
        yolo_str_labels (str): YOLO format string containing bounding box information for multiple objects.
        classes (list): List of class names corresponding to class numbers.

    Returns:
        list: A list of lists, each containing [x_center, y_center, width, height, class_name].
    """
    album_bb_lists = []
    yolo_list_labels = yolo_str_labels.split('\n')
    for yolo_str_label in yolo_list_labels:
        if yolo_str_label:
            album_bb_list = get_album_bb_list(yolo_str_label, classes)
            album_bb_lists.append(album_bb_list)
    return album_bb_lists


def get_bboxes_list(inp_lab_pth, classes):
    """
    Reads YOLO format labels from a file and returns bounding box information.

    Args:
        inp_lab_pth (str): Path to the YOLO format labels file.
        classes (list): List of class names corresponding to class numbers.

    Returns:
        list: A list of lists, each containing [x_center, y_center, width, height, class_name].
    """
    yolo_str_labels = open(inp_lab_pth, "r").read()

    if not yolo_str_labels:
        print("No object")
        return []

    lines = [line.strip() for line in yolo_str_labels.split("\n") if line.strip()]
    album_bb_lists = get_album_bb_lists("\n".join(lines), classes) if len(lines) > 1 else [get_album_bb_list("\n".join(lines), classes)]

    return album_bb_lists


def single_obj_bb_yolo_conversion(transformed_bboxes, class_names):
    """
    Convert bounding boxes for a single object to YOLO format.

    Parameters:
    - transformed_bboxes (list): Bounding box coordinates and class name.
    - class_names (list): List of class names.

    Returns:
    - list: Bounding box coordinates in YOLO format.
    """
    if transformed_bboxes:
        class_num = class_names.index(transformed_bboxes[-1])
        bboxes = list(transformed_bboxes)[:-1]
        bboxes.insert(0, class_num)
    else:
        bboxes = []
    return bboxes


def multi_obj_bb_yolo_conversion(aug_labs, class_names):
    """
    Convert bounding boxes for multiple objects to YOLO format.

    Parameters:
    - aug_labs (list): List of bounding box coordinates and class names.
    - class_names (list): List of class names.

    Returns:
    - list: List of bounding box coordinates in YOLO format for each object.
    """
    yolo_labels = [single_obj_bb_yolo_conversion(aug_lab, class_names) for aug_lab in aug_labs]
    return yolo_labels


def save_aug_lab(transformed_bboxes, lab_pth, lab_name):
    """
    Save augmented bounding boxes to a label file.

    Args:
        transformed_bboxes (list): List of augmented bounding boxes.
        lab_pth (str): Path to the output label directory.
        lab_name (str): Name of the label file.

    """
    lab_out_pth = os.path.join(lab_pth, lab_name)
    with open(lab_out_pth, 'w') as output:
        for bbox in transformed_bboxes:
            updated_bbox = str(bbox).replace(',', ' ').replace('[', '').replace(']', '')
            output.write(updated_bbox + '\n')


def save_aug_image(transformed_image, out_img_pth, img_name):
    """
    Save augmented image to an output directory.

    Args:
        transformed_image (numpy.ndarray): Augmented image.
        out_img_pth (str): Path to the output image directory.
        img_name (str): Name of the image file.

    """
    out_img_path = os.path.join(out_img_pth, img_name)
    cv2.imwrite(out_img_path, transformed_image)


def draw_yolo(image, labels, file_name):
    """
    Draw bounding boxes on an image based on YOLO format.

    Args:
        image (numpy.ndarray): Input image.
        labels (list): List of bounding boxes in YOLO format.

    """
    H, W = image.shape[:2]
    for label in labels:
        yolo_normalized = label[1:]
        box_voc = pbx.convert_bbox(tuple(yolo_normalized), from_type="yolo", to_type="voc", image_size=(W, H))
        cv2.rectangle(image, (box_voc[0], box_voc[1]),
                      (box_voc[2], box_voc[3]), (0, 0, 255), 1)
    cv2.imwrite(f"bb_image/{file_name}.png", image)
    # cv2.imshow(f"{file_name}.png", image)
    # cv2.waitKey(0)


def has_negative_element(lst):
    """
    Check if the given list contains any negative element.

    Args:
        lst (list): List of elements.

    Returns:
        bool: True if there is any negative element, False otherwise.
    """
    return any(x < 0 for x in lst)


def get_augmented_results(image, bboxes):

        # Define the augmentations
    transform = A.Compose([

        # Combination 1
        # A.RandomBrightnessContrast(brightness_limit=0.4, contrast_limit=0.4, p=1),  
        # A.CLAHE(clip_limit=2, tile_grid_size=(8, 8), p=1.0),  
        # A.Rotate(limit=5, p=1),  

        # Combination 2
        # A.Rotate(limit=5, p=1),  
        # A.GaussNoise(var_limit=(10.0, 30.0), p=1),  
        # A.RandomFog(fog_coef_lower=0.3, fog_coef_upper=0.5, alpha_coef=0.1, p=1),  

        # Combination 3
        # A.Blur(blur_limit=7, p=1),  
        # A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=1),  
        # A.Rotate(limit=5, p=1),  

        # Combination 4
        # A.CLAHE(clip_limit=2, tile_grid_size=(8, 8), p=1.0),  
        # A.Blur(blur_limit=7, p=1),  

        # Combination 5
        A.RandomBrightnessContrast(brightness_limit=0.4, contrast_limit=0.4, p=0.7),  # Randomly adjust brightness and contrast
        A.CLAHE(clip_limit=2, tile_grid_size=(8, 8), p=0.7),  # Apply CLAHE
        A.Rotate(limit=5, p=0.7),  # Randomly rotate the image, angle between -5 to 5 degrees
        A.GaussNoise(var_limit=(10.0, 30.0), p=0.7),  # Add Gaussian noise
        A.Blur(blur_limit=7, p=0.7),  # Apply blur
        A.HueSaturationValue(hue_shift_limit=20, sat_shift_limit=30, val_shift_limit=20, p=0.7),  # Randomly adjust hue, saturation, and value
        A.RandomFog(fog_coef_lower=0.3, fog_coef_upper=0.5, alpha_coef=0.1, p=0.7),  # Add random fog

        A.Resize(640, 640)  # Resize image to 640x640
    ], bbox_params=A.BboxParams(format='yolo'))


    # Apply the augmentations
    transformed = transform(image=image, bboxes=bboxes)
    transformed_image, transformed_bboxes = transformed['image'], transformed['bboxes']
    
    return transformed_image, transformed_bboxes


def has_negative_element(matrix):
    """
    Check if there is a negative element in the 2D list of augmented bounding boxes.

    Args:
        matrix (list[list]): The 2D list.

    Returns:
        bool: True if a negative element is found, False otherwise.

    """
    return any(element < 0 for row in matrix for element in row)


def save_augmentation(trans_image, trans_bboxes, trans_file_name):
    """
    Saves the augmented label and image if no negative elements are found in the transformed bounding boxes.

    Parameters:
        trans_image (numpy.ndarray): The augmented image.
        trans_bboxes (list): The transformed bounding boxes.
        trans_file_name (str): The name for the augmented output.

    Returns:
        None
    """
    tot_objs = len(trans_bboxes)
    if tot_objs:
        # Convert bounding boxes to YOLO format
        trans_bboxes = multi_obj_bb_yolo_conversion(trans_bboxes, CONSTANTS['CLASSES']) if tot_objs > 1 else [single_obj_bb_yolo_conversion(trans_bboxes[0], CONSTANTS['CLASSES'])]
        if not has_negative_element(trans_bboxes):
            # Save augmented label and image
            save_aug_lab(trans_bboxes, CONSTANTS["out_lab_pth"], trans_file_name + ".txt")
            save_aug_image(trans_image, CONSTANTS["out_img_pth"], trans_file_name + ".png")
            # Draw bounding boxes on the augmented image
            draw_yolo(trans_image, trans_bboxes, trans_file_name)
        else:
            print("Found Negative element in Transformed Bounding Box...")
    else:
        print("Label file is empty")

# cd YOLO数据增强
# conda activate myenv