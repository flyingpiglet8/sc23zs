import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
classes = ['anger','fear','happy','neutral','sad','surprise']

image_path = r'/Users/piglet/Desktop/expression/expression_augmentation640/train/images/51_jpg.rf.3c62afef9789e85d56ec7878813c5879_aug_out_1.png'
img = Image.open(image_/path)

label_path = r'/Users/piglet/Desktop/expression/expression_augmentation640/train/images/51_jpg.rf.3c62afef9789e85d56ec7878813c5879_aug_out_1.txt'
with open(label_path, 'r') as f:
    labels = f.readlines()

fig, ax = plt.subplots(1)
ax.imshow(img)

width, height = img.size

for label in labels:
    parts = label.strip().split()
    class_id = int(parts[0])
    x_center = float(parts[1]) * width
    y_center = float(parts[2]) * height
    bbox_width = float(parts[3]) * width
    bbox_height = float(parts[4]) * height
    
    xmin = x_center - bbox_width / 2
    ymin = y_center - bbox_height / 2
    
    rect = patches.Rectangle((xmin, ymin), bbox_width, bbox_height, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    
    plt.text(xmin, ymin, classes[class_id], bbox=dict(facecolor='white', alpha=0.5))

plt.show()
