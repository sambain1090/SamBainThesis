import time
from MainThread import shared

def main():
    while shared.quit_flag == False:
        print("PiCamThread is running...")
        time.sleep(20)
