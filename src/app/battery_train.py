from ultralytics import YOLO

model = YOLO('C:/repos/TCC/tcc-backend/runs/detect/train/weights/best.pt')

model.train(data='C:/repos/TCC/tcc-backend/src/app/battery_config.yaml', epochs=3, imgsz=640)