import threading
import time

import PiCamThread
import MaixSenseThread

class sharedClass:
    def __init__(self):
        self.quit_flag = False
        self.quit_lock = threading.Lock()

def main():
    # Create shared object
    global shared
    shared = sharedClass()

    # Create a thread for PiCamData
    t_piCam = threading.Thread(target=PiCamThread.main)
    t_maixSense = threading.Thread(target=MaixSenseThread.main)

    # Start the thread
    t_piCam.start()
    t_maixSense.start()

    # End program when 'q' is entered
    while not shared.quit_flag:
        if keyboard.is_pressed('q'):
            with shared.quit_lock:
                shared.quit_flag = True
            print("Exiting program...")
            break
            
        time.sleep(3)

    # Join threads
    t_piCam.join()
    t_maixSense.join()


if __name__ == "__main__":
    main()
