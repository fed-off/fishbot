import keyboard
import threading
import time

import actions
from fishing import fishing
import config


is_running = False # Флаг для управления запуском программы
fishing_thread = None  # Глобальная переменная для потока


def toggle_running():
    global is_running
    is_running = not is_running
    print(f"Рыбалка {'запущена' if is_running else 'остановлена'}")

keyboard.add_hotkey(config.BUTTON_TOGGLE_RUNNING, toggle_running)



def start_fishing():
    """Запускает процесс рыбалки в отдельном потоке"""
    global fishing_thread
    try:
        if fishing_thread is None or not fishing_thread.is_alive():
            fishing_thread = threading.Thread(target=fishing, daemon=True)
            fishing_thread.start()
    except Exception as e:
        print(f"Ошибка при запуске рыбалки: {e}")

def stop_fishing():
    """Останавливает процесс рыбалки"""
    global is_running
    is_running = False  # Останавливаем рыбалку