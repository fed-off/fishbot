import cv2
import numpy as np

import config
import make_screenshot


def get_coordinates():
    make_screenshot.capture_and_save()
    image = cv2.imread(config.SCREENSHOT)

    # Преобразуем в HSV для удобной работы с цветами
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Определяем диапазоны для цветов поплавка
    lower_bound = np.array(config.LOWER_BOUND)    # нижняя граница
    upper_bound = np.array(config.UPPER_BOUND)    # верхняя граница
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

            # Определяем левую центральную точку
            leftmost = tuple(largest_contour[largest_contour[:, :, 0].argmin()][0])


            bobber_left = [int(leftmost[0]), int(leftmost[1])]
            bobber_center = [cx, cy]

            return bobber_left, bobber_center
        
            # Для отладки
            # Рисуем точки
            cv2.circle(image, leftmost, 5, (255, 0, 0), -1)  # Синяя точка - левая граница
            cv2.circle(image, (cx, cy), 5, (0, 255, 0), -1)  # Зеленая точка - центр

            # Показываем результат
            cv2.imshow("Detected Float", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()