import ctypes
import time

start_time = time.time()
mouse_event = ctypes.windll.user32.mouse_event
MOUSEEVENTF_MOVE = 0x0001

while True:
    mouse_event(MOUSEEVENTF_MOVE, 0, 20, 20, 0)
    time.sleep(300)#sleep for 60 seconds
    print(str((time.time() - start_time)/60) + ' Minutes')