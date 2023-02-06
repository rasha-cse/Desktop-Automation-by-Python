import pyautogui
import time

spark_screenshot_path = r"C:\Users\rasha\PycharmProjects\MouseMover\spark\\"

x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "window.png", confidence=0.7)
pyautogui.click(x, y)

time.sleep(1)
x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "powerButton.png", confidence=0.7)
pyautogui.click(x, y)

time.sleep(2)
x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "shutdown.png", confidence=0.9)
pyautogui.doubleClick(x, y)