from pynput.keyboard import Key

# Режим отладки
DEBUG = False
DEBUG_SCREENSHOTS = False

# Размеры области скриншота и обрезки
SCREENSHOT = 'screenshot.png'   # имя файла скриншота
TOP_START_POINT = 0.15          # отступ сверху (от высоты экрана)
LEFT_START_POINT = 0.15         # отступ слева (от ширины экрана)
SCREENSHOT_WIDTH = 0.61         # ширина скриншота (от ширины экрана)
SCREENSHOT_HEIGHT = 0.6         # высота скриншота (от высоты экрана)


# Диапазоны цветов для обнаружения поплавка
LOWER_BOUND = (10, 100, 100)    # Нижняя граница для желтого
UPPER_BOUND = (35, 255, 255)    # Верхняя граница для желтого


# Проверка поклёва
CHECK_DELAY = 0.2               # Задержка между проверками
THRESHOLD_POINTS = 15           # Пороговые значения для смещения поплавка 10
THRESHOLD_DISTANCE = 15       # Пороговые значения для смещения поплавка (дистанция) 13
DELAY_BEFORE_CHECKING = 3       # Время перед началом проверки поклёвки


# Кнопки действий
BUTTON_TOGGLE_RUNNING = 'num_sub'         # Клавиша для включения/выключения программы
BUTTONS_STOP_FISHING = ['w', 'a', 's', 'd', 'space']  # Клавиши для остановки рыбалки
BUTTON_CAST_FISHING_ROD = Key.f5          # Клавиша для заброса удочки
BUTTON_HOOK = Key.f9                      # Клавиша для подсечки


# Диапазоны времени ожидания
DELAY_CAST_FISHING_ROD = [0.7, 2.3]         # Диапазон времени перед забросом удочки
DELAY_HOOK = [0.5, 2]                       # Диапазон времени перед подсечкой


# Время ожидания поклёва
WAIT_BITING_LIMIT = 22
