from keyboard import Keyboard
from bobber import Bobber
from utils import random_delay, debug
import config
import time
import random

class FishingBot:
  def __init__(self):
    self.keyboard = Keyboard()
    self.fish_count = 0
    self.fish_lost = 0
    self.count = 0
    self.start_time = time.time()
    self.running = False


  def run(self):
    self._setup_hotkeys()
    while True:
      if self.running:
        self._fish()
      else:
        time.sleep(1)

  def _setup_hotkeys(self):
    self.keyboard.add_hotkey(config.BUTTON_TOGGLE_RUNNING, self._toggle_running)
    self.keyboard.add_hotkey('esc', self._exit)
    for key in config.BUTTONS_STOP_FISHING:
      self.keyboard.add_hotkey(key, self._exit)
  
  def _toggle_running(self):
    self.running = not self.running
    if self.running:
      print('Рыбалка началась')
    else:
      print('Рыбалка остановлена')

  def _exit(self):
    print('Рыбалка завершена')
    exit()

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
    debug("Забрасываю удочку")
    self.keyboard.press_key(config.BUTTON_CAST_FISHING_ROD)
    time.sleep(config.DELAY_BEFORE_CHECKING)
    return Bobber()

  def _wait_biting(self, bobber):
    start_time = time.time()
    debug('Слежу за поплавком')
    time_threshold = random.uniform(config.WAIT_BITING_LIMIT - config.DELAY_BEFORE_CHECKING - 1, config.WAIT_BITING_LIMIT)
    while True:
      if bobber.is_biting():
        debug('Поклевка')
        return True
      if time.time() - start_time > time_threshold:
        debug('Время ожидания поклевки истекло')
        return False
      time.sleep(config.CHECK_DELAY)

  def _hook(self):
    random_delay(config.DELAY_HOOK[0], config.DELAY_HOOK[1])
    debug('Подсекаю')
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
    print('|\t' + '\t|\t'.join(columns) + '\t|')
