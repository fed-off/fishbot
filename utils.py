import random
import time
from config import DEBUG

def random_delay(time_start, time_end):
  delay = random.uniform(time_start, time_end)
  debug(f"Жду {round(delay, 2)} секунд")
  time.sleep(delay)

def debug(message):
  if DEBUG:
    print(message)