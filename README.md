# sc23zs


###  This project contains:

1. **Experimental dataset preprocessing and information presentation folder:** "Code for RAFDB", "Code for Other Datasets", "Code for AffectNet-YOLO"。

2. **YOLO data augmentation code for this experiment:** "YOLO_Data_Augmentation"（This folder is used to complete data expansion using five rounds of data augmentation on the training set of the Expression-Roboflow dataset. The section is mainly referenced: https://github.com/muhammad-faizan-122/yolo-data-augmentation.   In this project, the data augmentation technique for multi-target face data is additionally added to the utils.py file and the most suitable parameters are saved after several debugging sessions.）

3. **Data augmentation parameter debugging process:** "Data-Augmentation-Test_1.ipynb", "Data-Replacement of parameters by yourselfAugmentation-Test_2.ipynb".

4. **Analyzing Charting:**"Analysis_Drawing.ipynb"

5. **Experiment Command File:**"Command Codes.md"  (Replacement of parameters by yourself)

6. **The final adopted improved models network structure:**"YOLOv10-CA.yaml"

7. **Test file for YOLO with FPS calculation function:**"YOLOv5-val.py", "YOLOv8-validator.py",  "YOLOv10-validator.py"

8. **Python scripts for experiments:**

   | Script Files                                   | Purpose                                                      |
   | ---------------------------------------------- | ------------------------------------------------------------ |
   | Convert_FER2013_to_YOLO_format.py              | Convert FER2013 dataset to YOLO format                       |
   | Convert_RAFDB_to_YOLO_format.py                | Convert RAF-DB dataset to YOLO format                        |
   | DataBalance-YOLO-format.py                     | Data balancing of YOLO format datasets through data augmentation techniques |
   | Dataset_Splitting_YOLOformat.py                | YOLO format dataset subset splitting                         |
   | Labels_test.py                                 | YOLO dataset label positioning check                         |
   | YOLO-2Files-check.py                           | YOLO dataset label files and image files check               |
   | Comprehensive-YOLO-Dataset-Visualisation.ipynb | Show YOLO dataset details                                    |
   | Training-Trend-Display.ipynb                   | Demonstrate the trend of each parameter during YOLO training |
   | YOLO-Dataset-Information-Visualisation.ipynb   | YOLO dataset information visualisation                       |

9. **Results weights folder:**"Results_Weights_pt": https://drive.google.com/file/d/1HbVQP-f5fr8GswKXbPBd57QVEH1uYt5X/view?usp=drive_link

10. **Server dataset deployment profiles:** "Datasets Configuration" folder

11. **Datasets:** These datasets, with the exception of AffectNet-YOLO, have been preprocessed and refined. The datasets have all been converted and improved by the script format of this project, and can be directly used for the expression recognition task of the YOLO family of algorithms. The dataset configuration files are shown in 8. The dataset-sharing links are published below:

    | Datasets                         | Links                                                        |
    | -------------------------------- | ------------------------------------------------------------ |
    | Expression-Roboflow-Augmentation | https://drive.google.com/file/d/1Yj2TuZroQKVrt1rNQEkv_7L3uiu9eb3w/view?usp=drive_link |
    | Expression-Roboflow-7.2.1        | https://drive.google.com/file/d/1BihqS5kFATTV9PBMTB3kvu13RVxAIALC/view?usp=drive_link |
    | RAFDB-YOLO-Classification        | https://drive.google.com/file/d/1Kb8epxn1FsQaCis-THG4n4yUZz2XTn7Q/view?usp=drive_link |
    | RAFDB-YOLO-Detection             | ———————————————————————————                                  |
    | AffectNet-YOLO                   | https://drive.google.com/file/d/1Kb8epxn1FsQaCis-THG4n4yUZz2XTn7Q/view?usp=drive_link |
    | FER2013-YOLO                     | https://drive.google.com/file/d/1VG6TUTPTbV6yc0XcNL86gek7Cc-h9Af7/view?usp=drive_link |

    * The RAFDB-YOLO-Detection dataset production process was done by myself to proofread and annotate the original RAF-DB, and this part took a lot of time and effort. For academic requests, please contact songzh022@outlook.com and indicate the purpose.

### Project Description

The content of this project is the implementation code of the corresponding thesis, the main model is YOLOv5, YOLOv8 and YOLOv10. The project provides the format conversion and preprocessing scripts of various mainstream datasets, as well as the perfect dataset (which can be used directly). The original YOLO model did not add the speed calculation function in the test phase, this project provides the test files with FPS calculation function under the structure of v5, v8 and v10, which can be used directly by replacing the original model files. The weights files of the training part have also been provided and can be reproduced. The training parameters are detailed in the paper. Please note that some of the core weights and core datasets are not open source, if you need, please contact the author of this paper email. 

The original datasets are provided below:

* AffectNet DB:   https://www.kaggle.com/datasets/fatihkgg/affectnet-yolo-format   

* RAF-DB:  http://www.whdeng.cn/raf/model1.html   

* Expression-Roboflow:   https://universe.roboflow.com/workshop-yg2yt/expression-abyan   

* Others:   https://universe.roboflow.com/emotiondetection/facedetection2-6qc02 & https://universe.roboflow.com/project-zpt98/facial-recognition-qxgdz  

Please note that all datasets involve faces, and care should be taken to circumvent ethical and legal issues. The improved datasets provided in this project are for theoretical reproduction of the thesis only, and are not allowed for non-academic research or commercial applications. At the same time, the usage requirements of the original authors of the datasets must be complied with.

If you have any questions, please contact the email address for any other questions: songzh022@outlook.com.
