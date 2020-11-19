# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        if len(kwargs.items()) > 1:
            ignore_case = kwargs.items()[0]
        else:
            ignore_case = False
        dictionary = {}
        for item in kwargs.items()[1]:
            if ignore_case:
                item.lower()
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        pass

    def __next__(self):
        # Нужно реализовать __next__
        pass

    def __iter__(self):
        return self