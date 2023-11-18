import cv2
from sympy import true
from ultralytics import YOLO
import argparse
import supervision as sv
from supervision.geometry.core import Point
from supervision.detection import line_counter 
import numpy as np

LINE_START = Point(900, 0)
LINE_END = Point(900, 720)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="battery detection")
    parser.add_argument("--webcam-resolution", default=[1280, 720], nargs=2, type=int)
    args = parser.parse_args()
    return args


def count_batteries():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO('C:/repos/TCC/tcc-backend/runs/detect/train2/weights/best.pt')

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )
    
    line_counter = sv.LineZone(start=LINE_START, end=LINE_END)
    line_annotator = sv.LineZoneAnnotator(thickness=4, text_thickness=4, text_scale=2)


    while True: 
        ret, frame = cap.read()

        result = model.track(frame, agnostic_nms=True)[0]
        detections = sv.Detections.from_ultralytics(result)
        

        frame = box_annotator.annotate(scene=frame, detections=detections)
        

        line_counter.trigger(detections=detections)
        frame = line_annotator.annotate(frame=frame, line_counter=line_counter)

        cv2.imshow("battery detect", frame)

        if (cv2.waitKey(30) == 27):
            break

count_batteries()

