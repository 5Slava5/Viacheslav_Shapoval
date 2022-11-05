# Функція назва місяця за номером
import sys

list_of_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
                  5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
                  10: 'October', 11: 'November', 12: 'December'
                  }

inp = int(input("Please input number of a month: - "))


def monthname(m):
    try:
        return list_of_months[m]
    except ValueError as er1:
        print(f'it must be an integer: {er1}', file=sys.stderr)
    except KeyError as er2:
        print(f'it must be a number between 1 and 12: {er2}', file=sys.stderr)
    except TypeError as er3:
        print(f'it must be a number more than 0: {er3}', file=sys.stderr)


print(monthname(inp))
