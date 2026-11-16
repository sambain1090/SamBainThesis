import numpy as np
import cv2
import keyboard

import YoloDetection

from dataclasses import dataclass, field

## Camera types
PICAM = 0
MAIXSENSE = 1
MACCAM = 2
XBOXCAM = 3

@dataclass
class Ball:
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    covariance: np.ndarray = field(default_factory=lambda: np.eye(3))

    velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))
    acceleration: np.ndarray = field(default_factory=lambda: np.zeros(3))

class Camera:
    position: np.ndarray
    orientation: np.ndarray
    type: int

def trackPosition(ball, cameras):
    for camera in cameras:
        if camera.type == PICAM:
            YoloDetection.piCamPositionEstimate()
            pass
        elif camera.type == MAIXSENSE:
            # Get the position from the MaixSense
            YoloDetection.maixSenseEstimate()
            pass
        elif camera.type == MACCAM:
            # Get the position from the MacCam
            pass
        elif camera.type == XBOXCAM:
            # Get the position from the XboxCam
            pass

    return ball 
    
def main():
    ball = Ball()
    cameras = [
        Camera(position=[0, 0, 0], orientation=[0, 0, 0], type=PICAM),
        Camera(position=[0, 0, 0], orientation=[0, 0, 0], type=MAIXSENSE)
    ]

    while not keyboard.is_pressed("esc"):
        ball = trackPosition(ball, cameras)

if __name__ == "__main__":
    main()