"""Модуль для запуска программы"""

import os

from src.logging.logger import logger1, logger2
from generator.flat_generator import flat_generator


def test_1():
    path = 'logging/log_files/main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger1
    def hello_world():
        return 'Hello World'

    @logger1
    def summator(a, b=0):
        return a + b

    @logger1
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


def test_2():
    paths = ('logging/log_files/log_1.log',
             'logging/log_files/log_2.log',
             'logging/log_files/log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger2(path)
        def hello_world():
            return 'Hello World'

        @logger2(path)
        def summator(a, b=0):
            return a + b

        @logger2(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'

def test_3():
    @logger1
    def log_generator(list_):
        new_list = []
        for i in flat_generator(list_):
            new_list.append(i)
        return new_list

    log_generator([[45, 90, 'python'], ['g', 'i', 't'],[1, 2, 3]])

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
