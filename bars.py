import json
import sys
import os
from math import hypot


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_obj:
        python_obj = json.load(file_obj)
    return python_obj


def find_min_bar(dict_bars):
    min_bar = min(dict_bars['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return min_bar


def find_max_bar(dict_bars):
    max_bar = max(dict_bars['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return max_bar


def find_nearest_bar(py_obj_bars):
    while True:
        try:
            your_dolgota = float(input('Введите долготу : '))
            your_shirota = float(input('Введите широту  : '))
            break
        except ValueError:
            print('Неверный формат. Попробуй еще раз...')

    list_bars = []
    for bar in py_obj_bars['features']:
        distance = hypot(your_dolgota - bar['geometry']['coordinates'][0],
                         your_shirota - bar['geometry']['coordinates'][1])
        list_bars.append((distance, bar['properties']['Attributes']['Name']))
    near_bar = min(list_bars)
    return near_bar


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            py_obj_bars = load_data(sys.argv[1])
            min_bar = find_min_bar(py_obj_bars)
            max_bar = find_max_bar(py_obj_bars)

            print('Самый маленький бар',
                  min_bar['properties']['Attributes']['Name'])
            print('Самый большой бар',
                  max_bar['properties']['Attributes']['Name'])

            nearest_bar = find_nearest_bar(py_obj_bars)
            print('Ближайший бар', nearest_bar[1])
        else:
            print('файла не существует')
    else:
        print('нет входного файла')
