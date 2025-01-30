import config
import find_bobber

prev_position = None  # Храним последние координаты

def is_biting():
    global prev_position  # Используем глобальную переменную для хранения последних координат
    delta_position = None
    # Получаем текущие координаты поплавка
    current_position = find_bobber.get_coordinates()

    # Проверяем, удалось ли найти поплавок
    if current_position is None:
        print("Поплавок не найден!")
        return False

    # Если у нас нет предыдущих координат, просто сохраняем их
    if prev_position is None:
        prev_position = current_position
        return False

    left_delta_x = abs(current_position[0][0] - prev_position[0][0])
    left_delta_y = abs(current_position[0][1] - prev_position[0][1])
    right_delta_x = abs(current_position[1][0] - prev_position[1][0])
    right_delta_y = abs(current_position[1][1] - prev_position[1][1])

    delta_position = [(left_delta_x, left_delta_y), (right_delta_x, right_delta_y)]

    # Выводим отладочную информацию
    # print(f"Левая {delta_position[0][0], delta_position[0][1]}\nПравая{delta_position[1][0], delta_position[1][1]}\n---")

    # Обновляем предыдущие координаты перед следующим циклом
    prev_position = current_position

    # Условие для определения поклёвки
    return ((left_delta_x > config.THRESHOLD or right_delta_x > config.THRESHOLD) 
        or (left_delta_y > config.THRESHOLD or right_delta_y > config.THRESHOLD))
