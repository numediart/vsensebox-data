# 📥 `vsensebox-data`

* `vsensebox-data` can dynamically create individual data packages of the supported modules for [`VSenseBox`](https://github.com/numediart/vsensebox).
* `vsensebox-data` relies on the configurations inside [`setupconfig`](setupconfig) in order to create individual Python wheels.
* Only a few pretrained weight/model files are included in the prebuilt `.whl` [files on GitHub releases](https://github.com/numediart/vsensebox-data/releases).
* The pretrained weight/model files are not included in the repo as they are too big (Over 1GB).
* For `YOLO_Ultralytics`, you can manually download [all other models here](https://github.com/ultralytics/assets/releases).

## Installation

* `YOLO_Classic` ([License](https://github.com/AlexeyAB/darknet))
    ```
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.0/vsensebox_data_yolocls-0.0.0-py3-none-any.whl
    ```

* `YOLO_Ultralytics` ([License](https://github.com/ultralytics)) | YOLOv10 ([License](https://github.com/THU-MIG/yolov10))
    ```
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.2/vsensebox_data_yoloult-0.0.2-py3-none-any.whl
    ```

* `DeepSORT` ([License](https://github.com/deshwalmahesh/yolov7-deepsort-tracking))
    ```
    pip install https://github.com/numediart/vsensebox-data/releases/download/v0.0.0/vsensebox_data_deepsort-0.0.0-py3-none-any.whl
    ```
