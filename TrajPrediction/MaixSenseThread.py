import time
from MainThread import shared

def main():
    while shared.quit_flag == False:
        print("MaixSenseThread is running...")
        time.sleep(5)  # Simulate some work being doneqqqc