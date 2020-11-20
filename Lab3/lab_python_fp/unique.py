# Итератор для удаления дубликатов
# Нужно реализовать конструктор
# В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
# в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
# Например: ignore_case = True, Aбв и АБВ - разные строки
#           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
# По-умолчанию ignore_case = False

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_objects = set()
        self.data = items
        self.index = 0
        self.ignore_case = False
        self.string = ''
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']


    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                self.string = current
                if self.ignore_case:
                    self.string = current.lower()
                if self.string not in self.used_objects:
                    # Добавление в множество производится
                    # с помощью метода add
                    self.used_objects.add(self.string)
                    return current

    def __iter__(self):
        return self