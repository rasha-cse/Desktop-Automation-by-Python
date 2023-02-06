import pyautogui
import time

# pyautogui.click(460, 1050) #spark
# pyautogui.click(510, 1050) #chrome
# pyautogui.click(560, 1050) #rubymine
# pyautogui.click(610, 1050) #intelij
# pyautogui.click(660, 1050) #pycharm

spark_screenshot_path = r"C:\Users\rasha\PycharmProjects\MouseMover\spark\\"

###################### Spark ######################
if pyautogui.locateCenterOnScreen(spark_screenshot_path + "spark.png", confidence=0.9) is None:
    print("Spark Not Available!")
else:
    x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "spark.png", confidence=0.9)
    pyautogui.click(x, y)

###################### Chrome ######################
time.sleep(5)
if pyautogui.locateCenterOnScreen(spark_screenshot_path + "chrome.png", confidence=0.9) is None:
    print("Chrome Not Available!")
else:
    x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "chrome.png", confidence=0.7)
    pyautogui.click(x, y)

###################### RubyMine ######################
time.sleep(5)
if pyautogui.locateCenterOnScreen(spark_screenshot_path + "rubymine.png", confidence=0.9) is None:
    print("RubyMine Not Available!")
else:
    x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "rubymine.png", confidence=0.9)
    pyautogui.click(x, y)

###################### VisualStudioCode ######################
time.sleep(5)
if pyautogui.locateCenterOnScreen(spark_screenshot_path + "VisualStudioCode.png", confidence=0.7) is None:
    print("VisualStudioCode Not Available!")
else:
    x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "VisualStudioCode.png", confidence=0.7)
    pyautogui.click(x, y)

###################### Intelij ######################
# time.sleep(4)
# if pyautogui.locateCenterOnScreen(spark_screenshot_path + "intelij.png", confidence=0.7) is None:
#     print("Intelij Not Available!")
# else:
#     x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "intelij.png", confidence=0.7)
#     pyautogui.click(x, y)

###################### PyCharm ######################
time.sleep(2)
if pyautogui.locateCenterOnScreen(spark_screenshot_path + "pycharm.png", confidence=0.7) is None:
    print("PyCharm Not Available!")
else:
    x, y = pyautogui.locateCenterOnScreen(spark_screenshot_path + "pycharm.png", confidence=0.7)
    pyautogui.click(x, y)