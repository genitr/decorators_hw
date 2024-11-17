""" Модуль содержит функции для генераторов списка"""


def flat_generator(list_of_lists):
    for items in list_of_lists:
        if isinstance(items, list):
            for item in items:
                yield item
        else:
            yield items
