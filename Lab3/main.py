from lab_python_fp.field import field


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
     ]
    print(field(goods, 'title'))
    print(field(goods, 'title', 'price'))

if __name__ == "__main__":
    main()

