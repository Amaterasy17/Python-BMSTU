# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    result = []
    if len(args) == 1:
        for item in items:
            name = item.get(args[0])
            if name:
                result.append(name)
        return result
    else:
        sub_result = dict()
        for item in items:
            for name_field in args:
                name = item.get(name_field)
                if name:
                    sub_result[name_field] = name
            result.append(sub_result)
        return result
