from picamera2 import Picamera2
from datetime import datetime
from pathlib import Path
import time, sys

OUT = Path("")
OUT.mkdir(parents=True, exist_ok=True)

FPS = 40
EXPOSURE_US = 25000     # use the value measured from your 640x480 preview
GAIN = 4.0             # likewise

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
time.sleep(2)

def save():
    name = OUT / datetime.now().strftime("img_%Y%m%d_%H%M%S_%f.jpg")
    picam2.capture_file(str(name), format="jpeg")
    print("Saved", name)

mode = sys.argv[1] if len(sys.argv) > 1 else "key"
try:
    if mode == "timer":
        interval = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
        while True:
            save()
            time.sleep(interval)
    else:
        while True:
            input("Press Enter to capture (Ctrl+C to quit)...")
            save()
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
