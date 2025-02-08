from keyboard import Keyboard
from bobber import Bobber
from utils import random_delay
import config
import time

class FishingBot:
  def __init__(self):
    self.keyboard = Keyboard()
    self.fish_count = 0
    self.fish_lost = 0
    self.count = 0
    self.start_time = time.time()

  def start(self):
    print('Рыбалка началась')
    while True:
      self._fish()

  def _fish(self):
    self.count += 1
    bobber = self._cast_fishing_rod()
    if self._wait_biting(bobber):
      self._hook()
      self.fish_count += 1
    else:
      self.fish_lost += 1
    self._print_stats()
    

  def _cast_fishing_rod(self):
    random_delay(config.DELAY_CAST_FISHING_ROD[0], config.DELAY_CAST_FISHING_ROD[1])
    print("Забрасываю удочку")
    self.keyboard.press_key(config.BUTTON_CAST_FISHING_ROD)
    return Bobber()

  def _wait_biting(self, bobber):
    start_time = time.time()
    time.sleep(config.DELAY_BEFORE_CHECKING)
    print('Слежу за поплавком')

    while True:
      if bobber.is_biting():
        print('Поклевка')
        return True
      time_threshold = random_delay(config.WAIT_BITING_LIMIT - config.DELAY_BEFORE_CHECKING - 1, config.WAIT_BITING_LIMIT)
      if time.time() - start_time > time_threshold:
        print('Время ожидания поклевки истекло')
        return False
      time.sleep(config.CHECK_DELAY)

  def _hook(self):
    random_delay(config.DELAY_HOOK[0], config.DELAY_HOOK[1])
    print('Подсекаю')
    self.keyboard.press_key(config.BUTTON_HOOK)


  def _print_stats(self):
    total_time = time.time() - self.start_time
    minutes = int(total_time) // 60
    seconds = int(total_time) % 60

    columns = [
      f"{minutes:02}:{seconds:02}",
      f"{self.count}",
      f"{self.fish_count}",
      f"{self.fish_lost}"
    ]
    print('\t|\t'.join(columns))
