from ultralytics import YOLO

model = YOLO('C:/repos/TCC/tcc-backend/runs/detect/train2/weights/best.pt')

results = model.predict(source='0', show=True, conf=0.5, line_width=2)

print(results)