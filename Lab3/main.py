from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
     ]
    print('result field:')
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))

    list = ['Abc', 'ABC', 'AbC']
    generator = gen_random(5, 15, 20)
    print('result generator:')
    print(generator)
    print('result unique with generator')
    for item in Unique(generator):
        print(item)
    print('result unique with list')
    for item in Unique(list):
        print(item)
    dict = {
        'ignore_case': True,
    }
    print(' ')
    print('result unique with list and ignore_case = true:')
    for item in Unique(list, **dict):
        print(item)

if __name__ == "__main__":
    main()

