import os
import sys
from collections import Counter


def get_file(l_file_name):
    cwd = os.getcwd()
    folder_name = 'files'
    full_file_name = os.path.join(cwd, folder_name, l_file_name)

    try:
        file = open(full_file_name, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print(f'File "{full_file_name}" not found or access denied')
        return None

    return file


def get_cook_book(book_name):
    file = get_file(book_name)
    if file is None:
        return None

    result = {}

    for dish in file:
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name.strip(),
                                'quantity': int(quantity),
                                'measure': measure.strip()})
        result[dish.strip()] = ingredients
        file.readline()

    file.close()
    return result


def get_order(order_name):
    file = get_file(order_name)
    if file is None:
        return None

    result = [f.strip() for f in file]
    file.close()
    return result


def get_shop_list_by_dishes(dishes):
    dishes_dict = Counter(dishes)

    result = {}

    for key, value in dishes_dict.items():
        for ingredient in cook_book[key]:
            if ingredient['ingredient_name'] in result:
                result[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * int(value)
            else:
                result[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                         'quantity': ingredient['quantity'] * int(value)}
    return result


cook_book = get_cook_book('cookbook.txt')
if cook_book is None:
    sys.exit(1)

print(cook_book)

# Примеры использования

# Чтение заказа из файла
print(get_shop_list_by_dishes(get_order('order.txt')))

# Задание значения заказов вручную в коде для примера
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Запеченный картофель', 'Утка по-пекински', 'Омлет']))
print(get_shop_list_by_dishes(['Утка по-пекински', 'Омлет', 'Запеченный картофель', 'Утка по-пекински', 'Омлет']))
print(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Утка по-пекински', 'Омлет']))
print(get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Фахитос']))
