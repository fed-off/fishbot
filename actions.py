import time
import keyboard
import random
from pynput.keyboard import Controller, Key

import config
import manager
import check_biting

# Инициализация контроллера клавиатуры
keyboard_controller = Controller()

# Нажатие клавиши с случайной задержкой для естественного поведения
def press_key(key):
    # Случайная задержка от 0.1 до 0.3 секунд
    delay = random.uniform(0.1, 0.3)
    time.sleep(delay)
    keyboard_controller.press(key)
    time.sleep(random.uniform(0.05, 0.1))  # Небольшая задержка перед отпусканием
    keyboard_controller.release(key)

def ranom_delay(time_start, time_end):
    delay = random.uniform(time_start, time_end)
    # print(f"Жду {round(delay, 2)} секунд")
    time.sleep(delay)



def cast_fishing_rod():
    ranom_delay(config.DELAY_CAST_FISHING_ROD[0], config.DELAY_CAST_FISHING_ROD[1])
    
    if not manager.is_running:
        return print('Рыбалка прервана')
    
    check_biting.prev_position = None
    print("Забрасываю")
    press_key(config.BUTTON_CAST_FISHING_ROD)


def hook():
    ranom_delay(config.DELAY_HOOK[0], config.DELAY_HOOK[1])
    
    if not manager.is_running:
        return print('Рыбалка прервана')
    print('Подсекаю')
    press_key(config.BUTTON_HOOK)


def wait_biting():
    if not manager.is_running:
        return print('Рыбалка прервана')
    
    start_time = time.time()

    time.sleep(config.DELAY_BEFORE_CHECKING)
    print('Слежу за поплавком')

    while manager.is_running:
        if check_biting.is_biting():
            print('Поклевка')
            return True
        if time.time() - start_time > random.uniform((config.WAIT_BITING_LIMIT - config.DELAY_BEFORE_CHECKING - 1), config.WAIT_BITING_LIMIT):
            print('Время ожидания поклевки истекло')
            return False
        time.sleep(config.CHECK_DELAY)







