import time

import manager
import actions


def fishing():
    fish_count = 0
    fish_lost = 0
    start_time = time.time()
    
    print('Рыбалка началась')

    while manager.is_running:
        print('\t')
        actions.cast_fishing_rod()
        if actions.wait_biting():
            actions.hook()
            fish_count += 1
        else:
            fish_lost += 1

    total_time = time.time() - start_time
    minutes = int(total_time) // 60
    seconds = int(total_time) % 60

    print('\nРыбалка завершена')
    print(f'\nПрошло {minutes} минут и {seconds} секунд \nПоймал {fish_count} рыб\nУпустил {fish_lost} рыб')
