import pyautogui
import cv2
import numpy as np
import time
import random
import keyboard  # Для отслеживания нажатий клавиш
from pynput.keyboard import Controller, Key

# Инициализация контроллера клавиатуры
keyboard_controller = Controller()

# Функция для создания скриншота
def capture_and_save():
    screenshot = pyautogui.screenshot()  # Создание скриншота
    screenshot.save("screenshot.png")    # Сохранение в файл

# Функция для нахождения центра поплавка
def find_float_center(image_path):
    image = cv2.imread(image_path)

    # Преобразуем в HSV для удобной работы с цветами
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Определяем диапазоны для цветов поплавка
    lower_bound = np.array([10, 100, 100])    # Нижняя граница
    upper_bound = np.array([35, 255, 255])    # Верхняя граница для желтого
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Находим контуры на маске
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Если контуры найдены
    if contours:
        # Находим самый большой контур (вероятно это поплавок)
        largest_contour = max(contours, key=cv2.contourArea)

        # Вычисляем моменты для нахождения центра масс
        moments = cv2.moments(largest_contour)
        if moments["m00"] != 0:
            # Центр масс
            cx = int(moments["m10"] / moments["m00"])
            cy = int(moments["m01"] / moments["m00"])

            # Возвращаем координату y
            return cy
    return None

# Нажатие клавиши с случайной задержкой для естественного поведения
def press_key(key):
    # Случайная задержка от 0.1 до 0.3 секунд
    delay = random.uniform(0.1, 0.3)
    time.sleep(delay)
    keyboard_controller.press(key)
    time.sleep(random.uniform(0.05, 0.1))  # Небольшая задержка перед отпусканием
    keyboard_controller.release(key)

def stop_program():
    global running
    running = False
    print("Программа остановлена по нажатию клавиши.")

# Регистрация горячих клавиш для остановки
keyboard.add_hotkey('w', stop_program)
keyboard.add_hotkey('a', stop_program)
keyboard.add_hotkey('s', stop_program)
keyboard.add_hotkey('d', stop_program)
keyboard.add_hotkey('space', stop_program)

# Запуск цикла
if __name__ == "__main__":
    start_time = time.time()  # Начало общего времени рыбалки
    max_time = random.uniform(850, 1100) # Максимальное время работы программы - примерно 15 минут (900 секунд)
    total_catch = 0  # Общее количество пойманной рыбы
    total_missed = 1  # Общее количество утерянных рыб
    running = True  # Флаг для отслеживания, нужно ли продолжать выполнение
    time.sleep(2)  # Задержка перед началом
    if running:
        press_key(Key.f5)  # Заброс удочки
        time.sleep(3)  # Задержка перед началом ловли

    while running:
        if time.time() - start_time > max_time:  # Если прошло примерно 15 минут, останавливаем программу
            print("Программа завершена. Время рыбалки истекло.")
            break
        
        last_y = None  # Переменная для хранения последней координаты y
        iteration_start = time.time()  # Начало каждой итерации цикла

        while time.time() - iteration_start < random.uniform(17, 20):  # Цикл длится от 17 до 20 секунд (ожидание поклёва)
            if not running:
                break  # Завершаем выполнение программы
            
            capture_and_save()
            cy = find_float_center("screenshot.png")
            
            print(f"Получена координата y: {cy}")  # Выводим текущую координату y для отладки
            
            # Проверяем, если разница в координатах y больше 50
            if cy is not None and last_y is not None and abs(last_y - cy) > 50:
              print("Поплавок утерян!")
              running = False  # Останавливаем программу
              break  # Выход из внутреннего цикла

            # Проверяем, если cy не равно None
            if cy is not None and last_y is not None and abs(last_y - cy) > 7:
                print("Поклёв!")
                
                # Генерация случайного таймаута (от 0.5 до 2 секунд)
                timeout = random.uniform(0.5, 2)
                print(f"Жду {timeout} секунд перед подсечкой...")
                time.sleep(timeout)
                
                if not running:
                    break  # Завершаем выполнение программы

                # Выводим сообщение о подсечке
                print("Подсекаю!")
                press_key(Key.f9)
                total_catch += 1  # Увеличиваем счётчик пойманной рыбы
                total_missed -= 1 # Уменьшаем счётчик утерянной рыбы
                
                # Прерываем цикл после подсечки
                break
            
            # Обновляем last_y
            if cy is not None:
                last_y = cy

            time.sleep(0.25)  # Пауза в 0.25 секунды

        if not running:
            break  # Завершаем выполнение программы

        # Таймаут перед забросом
        timeout = random.uniform(1, 2)
        print(f"Жду {timeout} секунд перед забросом...")
        time.sleep(timeout)

        if not running:
            break  # Завершаем выполнение программы
        
        # Выводим сообщение о забросе
        print("Забрасываю!")
        press_key(Key.f5)
        total_missed += 1
        time.sleep(3)  # Задержка перед продолжением
        print("Продолжаю ловить!")

    print("Цикл завершен.")
    # Вывод итогов
    total_time = time.time() - start_time
    print(f"\nИтоги рыбалки:")
    print(f"Общее время рыбалки: {int(total_time) // 60}:{int(total_time) % 60}")
    print(f"Поймано рыбин: {total_catch}")
    print(f"Упущено рыбин (не было подсечки): {total_missed}")
