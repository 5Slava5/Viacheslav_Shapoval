# Функція назва місяця за номером
import sys

list_of_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                  5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
                  10: 'October', 11: 'November', 12: 'December'
                  }


def month_name(m):
    """A month number must be an integer"""
    return list_of_months[m]


try:
    print(month_name(int(input("Enter a number of a month (1-12): - "))))
except ValueError as er1:
    print(f'it must be an integer, not a word: {er1}', file=sys.stderr)
except KeyError as er2:
    print(f'it must be a number between 1 and 12: {er2}', file=sys.stderr)