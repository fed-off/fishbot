import keyboard
import config
import manager # Импортируем менеджер для управления программой | Не удалять


if __name__ == "__main__":
    print(f"Программа запущена. Для остановки нажмите Esc\nНажмите кнопку {config.BUTTON_TOGGLE_RUNNING} для старта или остановки рыбалки.\n\t")
    keyboard.wait("esc")  # Программа завершится при нажатии "Esc"
