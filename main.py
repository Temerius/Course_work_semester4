from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('./input_data/input_video.mp4', save=True)
