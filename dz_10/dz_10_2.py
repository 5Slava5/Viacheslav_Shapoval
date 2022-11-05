# Обробка помилок у функції на перевірку унікальності елементів списку
import sys


def unique(lst):
    print(lst)
    try:
        set_list = set(lst)
        if len(lst) == len(set_list):
            print("У цьому списку усі елементи унікальні")
        else:
            print("У цьому списку маються однакові елементи")
        raise

    except Exception as er1:
        print(f'it must be a list: {er1}', file=sys.stderr)


unique([100, 75, 20, 12, 25, 20, "adsf", 1.2, 0])
