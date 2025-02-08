import pyautogui
import numpy as np
import config
import cv2


class Bobber:
  def __init__(self):
    self.points = self._get_coordinates()
    self.checks = [
      self._check_delta_threshold,
      self._check_distance_threshold
    ]
  
  def is_biting(self):
    result = False
    current_points = self._get_coordinates()
    if current_points and self.points:
      for check in self.checks:
        if check(current_points):
          result = True
          break
    self.points = current_points
    return result


  def _check_distance_threshold(self, current_points):
    for current_point, prev_point in zip(current_points, self.points):
      distance = np.linalg.norm(current_point - prev_point)
      if distance > config.THRESHOLD_DISTANCE:
        return True
    return False

  def _check_delta_threshold(self, current_points):
    for current_point, prev_point in zip(current_points, self.points):
      delta = np.abs(current_point - prev_point)
      if delta[0] > config.THRESHOLD_POINTS or delta[1] > config.THRESHOLD_POINTS:
        return True
    return False

  def _get_coordinates(self):
    screenshot = self._make_screenshot()
    bobber_contour = self._find_bobber_contour(screenshot)
    if bobber_contour is not None:
      leftmost = self._get_leftmost_point(bobber_contour)
      center = self._get_central_point(bobber_contour)
      if config.DEBUG:
        self._draw_points(screenshot, [leftmost, center])
      return [leftmost, center]
  
  def _make_screenshot(self):
    # Получаем размер экрана
    screen_width, screen_height = pyautogui.size()

    # Вычисляем размеры области скриншота и обрезки
    top = int(screen_height * config.TOP_START_POINT)                # отступ сверху
    left = int(screen_width * config.LEFT_START_POINT)               # отступ слева
    width = int(screen_width * config.SCREENSHOT_WIDTH)              # ширина скриншота
    height = int(screen_height * config.SCREENSHOT_HEIGHT)           # высота скриншота

    # Делаем скриншот выбранной области
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return np.array(screenshot)

  def _find_bobber_contour(self, screenshot):
    # Преобразуем в HSV для удобной работы с цветами
    screenshot_hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)
    # Определяем диапазоны для цветов поплавка
    lower_bound = np.array(config.LOWER_BOUND)    # нижняя граница
    upper_bound = np.array(config.UPPER_BOUND)    # верхняя граница
    mask = cv2.inRange(screenshot_hsv, lower_bound, upper_bound)

    # Находим контуры на маске
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Если контуры найдены
    if contours:
      # Находим самый большой контур (вероятно это поплавок)
      bobber_contour = max(contours, key=cv2.contourArea)
      return bobber_contour
    return None

  def _get_central_point(self, contour):
    moments = cv2.moments(contour)
    if moments["m00"] != 0:
      # Центр масс
      cx = int(moments["m10"] / moments["m00"])
      cy = int(moments["m01"] / moments["m00"])
      return np.array([cx, cy])
    return None
  
  def _get_leftmost_point(self, contour):
    leftmost = tuple(contour[contour[:, :, 0].argmin()][0])
    return np.array([int(leftmost[0]), int(leftmost[1])])

  def _draw_points(self, screenshot, points):
      # Для отладки
      # Рисуем точки
      for point in points:
        cv2.circle(screenshot, point, 5, (0, 255, 0), -1)

      # Показываем результат
      cv2.imshow("Detected Float", screenshot)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
