from operator import itemgetter

class Library:
    """Библиотека функций языков программирования"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LanguageOfProgramming:
    """Язык программирования"""
    def __init__(self, id, name, popularity, lib_id):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.lib_id = lib_id

class LibraryLanguage:
    """
    'Языки программирования в библиотеках' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, lib_id, lan_id):
        self.lib_id = lib_id
        self.lan_id = lan_id

# Библиотеки
libs = [
    Library(1, 'Boost'),
    Library(2, 'Django'),
    Library(3, 'STL'),

    Library(11, 'Entity framework'),
    Library(22, 'React framework'),
    Library(33, 'Awesome Go framework'),
]

# Языки программирования
lans = [
    LanguageOfProgramming(1, 'C++', 1500000, 1),
    LanguageOfProgramming(2,'Python', 2000000, 2),
    LanguageOfProgramming(3,'C#', 1000000, 1),
    LanguageOfProgramming(4, 'Golang', 10000000, 2),
    LanguageOfProgramming(5, 'JS', 1400000, 3),
]

lib_lans = [
    LibraryLanguage(1,1),
    LibraryLanguage(2,2),
    LibraryLanguage(3,3),
    LibraryLanguage(3,4),
    LibraryLanguage(3,5),

    LibraryLanguage(11,1),
    LibraryLanguage(22,2),
    LibraryLanguage(33,3),
    LibraryLanguage(33, 4),
    LibraryLanguage(22, 5),
]

def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(lang.name, lang.popularity, lib.name) 
        for lib in libs 
            for lang in lans
                if lang.lib_id == lib.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lib.name, ll.lib_id, ll.lan_id) 
        for lib in libs 
            for ll in lib_lans 
                if lib.id == ll.lib_id]
    
    many_to_many = [(lan.name, lan.popularity, lib_name) 
        for lib_name, lib_id, lan_id in many_to_many_temp
        for lan in lans if lan.id==lan_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for lib in libs:
        # Список языков, используемых в библиотеке
        lib_languages = list(filter(lambda i: i[2]==lib.name, one_to_many))
        # Если библиотека не пустая        
        if len(lib_languages) > 0:
            # Популярность языков библиотеки
            popularity_lans = [popularity for _,popularity,_ in lib_languages]
            # Популярность библиотеки
            popularityOfLibrary = sum(popularity_lans)
            res_12_unsorted.append((lib.name, popularityOfLibrary))

    # Сортировка по популярности
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for lib in libs:
        if 'framework' in lib.name:
            # Список языков из библиотеки
            languagesFromLib = list(filter(lambda i: i[2]==lib.name, many_to_many))
            # Только имена языков из данной библиотеки
            lib_lans_names = [x for x,_,_ in languagesFromLib]
            # Добавляем результат в словарь
            # ключ - имя библиотеки, значение - список языков
            res_13[lib.name] = lib_lans_names

    print(res_13)

if __name__ == '__main__':
    main()

