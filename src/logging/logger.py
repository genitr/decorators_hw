"""Модуль содержит функции для ведения журнала логов"""

from functools import wraps
from datetime import datetime


def write_log_to_file(log_file_path: str, message: str) -> None:
    """
        Добавляет запись в файл лога.

        :param log_file_path: Путь к файлу
        :param message: Сообщение для записи.
        """
    with open(log_file_path, 'a', encoding='utf-8') as file:
        file.write(message + '\n')


def logger(old_function):
    """
    Декоратор, который записывает в файл детали выполнения функции.

    :param old_function: Декорируемая функция.
    :return: Обернутую функцию с возможностью ведения журнала.
    """
    @wraps(old_function)
    def wrapper(*args, **kwargs):
        date = datetime.now().strftime('%d.%m.%y')
        time = datetime.now().strftime('%H:%M')
        try:
            result = old_function(*args, **kwargs)

            log_info = (
                f'Date: {date}, Time: {time}, Function: {old_function.__name__}, '
                f'args: {args}, kwargs: {kwargs}, Result: {result}')
            write_log_to_file('main.log', log_info)
            return result
        except Exception as e:
            print(f"Ошибка в функции {old_function.__name__}: {e}")
            raise

    return wrapper