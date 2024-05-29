import cv2
import numpy as np
from yolodetect import YoloDetect


points = []
model = YoloDetect()


def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])


def draw_polygon(frame, points):
    for point in points:
        frame = cv2.circle(frame, (point[0], point[1]), 5, (0, 0, 255), -1)

    frame = cv2.polylines(frame, [np.int32(points)],
                          False, (255, 0, 0), thickness=2)
    return frame


detect = False

video = cv2.VideoCapture('test_video.mp4')

if (video.isOpened() == False):
    print("Error opening video file")


while(video.isOpened()):

    ret, frame = video.read()

    if ret == True:
        frame = draw_polygon(frame, points)

        if detect:
            frame = model.detect(frame=frame, points=points)

        key = cv2.waitKey(0)
        if key == ord('q'):
            break

        elif key == ord('d'):
            points.append(points[0])
            detect = True

        # cv2.namedWindow("Intrusion Warning", cv2.WINDOW_FULLSCREEN)
        # cv2.resizeWindow("Intrusion Warning", 1600, 2560)
        cv2.imshow('Intrusion Warning', frame)
        cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

    else:
        break


video.release()
cv2.destroyAllWindows()
