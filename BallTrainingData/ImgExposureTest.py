#!/usr/bin/env python3
import time
import cv2
from picamera2 import Picamera2


FPS = 40
EXPOSURE_US = 23000     # use the value measured from your 640x480 preview
GAIN = 4.0             # likewise
SHOW_EVERY = 20

picam2 = Picamera2()
config = picam2.create_video_configuration(
    main={"size": (1296, 972), "format": "RGB888"},
    sensor={"output_size": (1296, 972), "bit_depth": 10},
    controls={
        "FrameDurationLimits": (int(1e6 / FPS), int(1e6 / FPS)),
        "AeEnable": False,
        "ExposureTime": EXPOSURE_US,
        "AnalogueGain": GAIN,
    },
    buffer_count=6,
)
picam2.configure(config)
picam2.start()
print(picam2.camera_configuration()["sensor"])

n, t0 = 0, time.time()
try:
    while True:
        frame = picam2.capture_array("main")   # BGR order, ready for OpenCV

        # ... process every frame here (segmentation etc.) ...

        n += 1

        if n % SHOW_EVERY == 0:
            cv2.imshow("Pi Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if n % 200 == 0:
            print(f"{200 / (time.time() - t0):.1f} fps")
            t0 = time.time()
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
    cv2.destroyAllWindows()
