import json
import sys
import os
from math import hypot


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_obj:
        python_obj = json.load(file_obj)
    return python_obj


def find_min_max_bar(dict_bars):
    min_bar = min(dict_bars['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    max_bar = max(dict_bars['features'],
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return min_bar, max_bar


def find_nearest_bar(py_obg_bars, longitude, latitude):
    list_bars = []
    for bar in py_obj_bars['features']:
        distance = hypot(
            longitude - bar['geometry']['coordinates'][0],
            latitude - bar['geometry']['coordinates'][1],
        )
        list_bars.append((distance, bar['properties']['Attributes']['Name']))
    nearest_bar = min(list_bars)
    return nearest_bar


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            py_obj_bars = load_data(sys.argv[1])
            min_max_bar = find_min_max_bar(py_obj_bars)
            print('Самый маленький бар ',
                  min_max_bar[0]['properties']['Attributes']['Name'])
            print('Cамый большой бар',
                  min_max_bar[1]['properties']['Attributes']['Name'])
            try:
                longitude = float(input('Введите долготу : '))
                latitude = float(input('Введите широту  : '))
            except ValueError:
                print('Неверный формат. Попробуй еще раз...')
                sys.exit()
            if 60.0 < longitude or latitude < 30.0:
                print('Далековато до москвы')
                sys.exit()
            nearest_bar = find_nearest_bar(
                py_obj_bars,
                longitude,
                latitude,
            )
            print(nearest_bar[1])
        else:
            print('файла не существует')
    else:
        print('нет входного файла')
