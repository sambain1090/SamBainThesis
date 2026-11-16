import cv2
import math
from ultralytics import YOLO

# Export once, then reuse the exported model on later runs

model = YOLO("pingpongmodel_ncnn_model")

positions = []  # (frame_idx, cx, cy, conf)

# stream=True yields one frame at a time instead of holding the whole video in memory
for i, r in enumerate(model("ball_toss.mp4", stream=True, conf=0.3)):
    if len(r.boxes) == 0:
        positions.append((i, None, None, None))  # ball not detected this frame
        continue

    # Pick the most confident detection (you only have one ball)
    best = r.boxes.conf.argmax()
    cx, cy, w, h = r.boxes.xywh[best].tolist()  # pixel coords, center-based


    
    conf = float(r.boxes.conf[best])
    positions.append((i, cx, cy, conf))

    # Optional: visualize
    frame = r.orig_img.copy()
    cv2.circle(frame, (int(cx), int(cy)), 6, (0, 255, 0), -1)
    cv2.rectangle(frame, (int(cx - w/2), int(cy - h/2)), (int(cx + w/2), int(cy + h/2)), (0, 255, 0), 2)
    cv2.imshow("ball", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

def getPositionPiCam(cx, cy, w, ball_diam=0.04):
    fov_v = 41.4
    fov_h = 53.5
    focal_length = 0.0036  # m
    ang_x = fov_h * (cx / 640 - 0.5)
    ang_y = fov_v * (cy / 480 - 0.5)
    dist = (ball_diam * focal_length) / w

    pos_x, pos_y = polarToCartesian(dist, ang_x)
    _, pos_z = polarToCartesian(dist, ang_y)

    return pos_x, pos_y, pos_z

def polarToCartesian(distance, angle):
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    return x, y