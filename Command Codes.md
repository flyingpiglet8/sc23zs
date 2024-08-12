* Complete the experiment by entering the following command line commands in the server terminal.

### Autodl Initialization

```cmd
# Unzip the package file
apt-get update
apt-get install -y unzip
unzip  <zipnemame>.zip -d <path>

# #Download Configuration File
pip install -r requirements.txt -i 

# If you are in mainland China, please use the Tencent source to download the configuration file
pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```

### TensorBoard

```cmd
tensorboard --logdir=yolov10-main/runs/v10_RAFDB_YOLO_Detection/train/events.out.tfevents.1721103456.autodl-container-c8744bb216-720002de.1899.0
```



###  yolov5

```cmd
# yolov5 Training Command
python train.py
# yolov5 Test Command
python YOLOv5-val.py
```



### yolov8

·yolov8 Training commands

```cmd
# Build a new model and train it from scratch
yolo detect train data=/root/autodl-tmp/YOLO_format/data.yaml model=yolov8m.yaml epochs=500 imgsz=640

# Training with pre-trained weights
yolo detect train data=/root/autodl-tmp/AffectNet-YOLO/data.yaml model=yolov8m.yaml pretrained=/root/ultralytics-main/yolov8m.pt epochs=2000 imgsz=640 batch=32 save_period=-1
```

·The yolov8 test command 

```cmd
yolo task=detect mode=val model=/root/ultralytics-main/runs/v8_RAFDB_YOLO_Detection/train/weights/best.pt data=/root/autodl-tmp/RAFDB_YOLO-detection/data.yaml  batch=1
```

·The yolov8 reasoning command

```cmd
yolo predict model="/root/ultralytics-main/runs/v8_RAFDB_YOLO_Detection/train/weights/best.pt" source='/root/ultralytics-main/ultralytics/assets' 
```



### yolov10

·The yolov10 training command

```cmd
# Regular
yolo detect train data=/root/autodl-tmp/expression/data.yaml model=yolov10m.yaml pretrained=/root/yolov10-main/yolov10m.pt epochs=2000 batch=32 imgsz=640 device=0 


# Improved
yolo detect train data=/root/autodl-tmp/RAFDB_YOLO-detection/data.yaml model=/root/yolov10-main/ultralytics/cfg/models/v10/yolov10-DoubleAttention.yaml pretrained=False epochs=2000 batch=32 imgsz=640 device=0 

```

·The yolov10 test command

```cmd
yolo val model=/root/yolov10-main/runs/v10_baseline/train/weights/best.pt data=/root/autodl-tmp/RAFDB_YOLO-detection/data.yaml  batch=32
```

·The yolov10 reasoning command

```cmd
yolo predict model=/root/yolov10-main/runs/v10_CA_detection/train/weights/best.pt source=/root/autodl-tmp/Testphotos 
## The files to be inferred are placed in yolov10-main/ultralytics/assets, and the inference results are generated in yolov10-main/runs/detect
```

