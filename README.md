# Рыболовный бот

Этот проект представляет собой автоматический бот для ловли рыбы в игре (world of warcraft), который управляет действиями через клавиши и анализирует экран с помощью компьютерного зрения.

## Установка зависимостей

Для установки всех зависимостей, используйте команду: pip install -r requirements.txt
(с зависимостями не уверен, но вроде всё верно)

## Использование

1. Откройте игру, уберите лишние элементы интерфейса (оставьте воду и поплавок), используйте "Огромные поплавки".
2. Запустите скрипт (python main.py) и поставьте фокус на окно игры (чтобы нажатие клавиш вызывало действия в игре).
3. Выполнится заброс на кнопку F5 и бот начнёт отслеживать поплавок.
4. Бот будет автоматически забрасывать удочку, ждать поклёвки и подсекать рыбу (на кнопку F9).
5. Если бот потеряет поплавок или время выйдет, программа завершится.
6. Результаты будут выведены по завершению работы.

## Завершение программы

Программу можно остановить, нажав любую из клавиш: `w`, `a`, `s`, `d`, `space`.

## Зависимости

Этот проект требует следующих библиотек:

- `pyautogui` для создания скриншотов.
- `opencv-python` для обработки изображений.
- `numpy` для работы с массивами данных.
- `keyboard` для отслеживания нажатий клавиш.
- `pynput` для симуляции нажатий клавиш.

## Рекомендации

Этот проект является открытым, и вы можете использовать его по своему усмотрению.
Учтите, что большинство игр запрещает использование ботов и автоматизацию игрового процесса,
поэтому рекомендую использовать этот код не для ботинга, а для обучения и экспериментов.
