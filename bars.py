import json
import sys
import os
from math import hypot


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_obj:
        python_obj = json.load(file_obj)
    return python_obj


def find_min_bar(dict):
    min_bar = min(dict['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return min_bar


def find_max_bar(dict):
    max_bar = max(dict['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return max_bar


def find_nearest_bar(x1, y1, x2, y2, name_bar):
    distance = hypot(x2 - x1, y2 - y1)
    return distance, name_bar


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

            while True:
                try:
                    your_dolgota = float(input('Введите долготу : '))
                    your_shirota = float(input('Введите широту  : '))
                    break
                except ValueError:
                    print('Неверный формат. Попробуй еще раз...')
                except Exception:
                    print('Что то не так...')

            list_bars = []
            for bar in py_obj_bars['features']:
                list_bars.append(
                    find_nearest_bar(bar['geometry']['coordinates'][0],
                                     bar['geometry']['coordinates'][1],
                                     your_dolgota,
                                     your_shirota,
                                     bar['properties']['Attributes']['Name']))
            min(list_bars)
            print('Ближайший бар', min(list_bars)[1])
        else:
            print('файла не существует')
    else:
        print('нет входного файла')
