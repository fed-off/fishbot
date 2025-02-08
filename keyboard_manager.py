import keyboard
from pynput.keyboard import Controller, Key
from utils import random_delay


class Keyboard:
  def __init__(self):
    self.controller = Controller()
  
  def press_key(self, key):
    random_delay(0.1, 0.3)
    self.controller.press(key)
    random_delay(0.05, 0.1)
    self.controller.release(key)

  def add_hotkey(self, key, callback):
    keyboard.add_hotkey(key, callback)
