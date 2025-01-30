import time

import config
import manager
import check_biting

def fishing():
    while manager.is_running:
        if check_biting.is_biting():
            print("Поклевка! Подсекаем!")
            
        time.sleep(config.CHECK_DELAY)
