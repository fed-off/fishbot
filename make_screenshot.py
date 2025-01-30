import pyautogui
import numpy as np
import config

def capture_and_save():
    # Получаем размер экрана
    screen_width, screen_height = pyautogui.size()

    # Вычисляем размеры области скриншота и обрезки
    top = int(screen_height * config.TOP_START_POINT)                # отступ сверху
    left = int(screen_width * config.LEFT_START_POINT)               # отступ слева
    width = int(screen_width * config.SCREENSHOT_WIDTH)              # ширина скриншота
    height = int(screen_height * config.SCREENSHOT_HEIGHT)           # высота скриншота

    # Делаем скриншот выбранной области
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # Сохраняем скриншот
    screenshot.save(config.SCREENSHOT)
