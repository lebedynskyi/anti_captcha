import time

import numpy as np
import pyautogui
from PIL import ImageGrab


class AppLooper:
    def __init__(self, handlers, tick_delay=1):
        self.tick_delay = tick_delay
        self.handlers = handlers

        pyautogui.FAILSAFE = False
        pyautogui.PAUSE = 0.02

    def loop(self):
        while True:
            screenshot = ImageGrab.grab()
            array = np.array(screenshot)
            current_time = time.time()
            for handler in self.handlers:
                handler.on_tick(array, current_time)

            if self.tick_delay > 0:
                time.sleep(self.tick_delay)

            print("\r")
