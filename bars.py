import json
import sys
import os
from math import hypot


def load_data(filepath):
    with open(filepath, 'r', encoding='utf8') as file_obj:
        python_obj = json.load(file_obj)
    return python_obj


def find_min_bar(bars):
    min_bar = min(bars,
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return min_bar


def find_max_bar(bars):
    max_bar = max(bars,
                  key=lambda i: i['properties']['Attributes']['SeatsCount'])
    return max_bar


def find_nearest_bar(bars, longitude, latitude):
    nearest_bar = min(
        bars,
        key=lambda bar: hypot(
            longitude - bar['geometry']['coordinates'][0],
            latitude - bar['geometry']['coordinates'][1],
        ))
    return nearest_bar


if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        bars = load_data(sys.argv[1])['features']
        min_bar = find_min_bar(bars)
        max_bar = find_max_bar(bars)
        print('Самый маленький бар ',
              min_bar['properties']['Attributes']['Name'])
        print('Cамый большой бар',
              max_bar['properties']['Attributes']['Name'])
        try:
            longitude = float(input('Введите долготу : '))
            latitude = float(input('Введите широту  : '))
        except ValueError:
            sys.exit('Неверный формат. Попробуй еще раз...')
        nearest_bar = find_nearest_bar(
            bars,
            longitude,
            latitude,
        )
        print(nearest_bar['properties']['Attributes']['Name'])
    else:
        print('нет входного файла')
