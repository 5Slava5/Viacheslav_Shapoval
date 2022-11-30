"""Визначення швидкості роботи функції факторіал числа"""
import math
import time
import concurrent.futures


def factor(num):
    """Function to calculate the factorial of num"""
    return math.factorial(num)


if __name__ == '__main__':
    # Function to calculate the factorial of num with ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        time_lst = []
        str_at = time.time()
        for result in executor.map(factor, range(0, 5)):
            time_lst.append(time.time() - str_at)
            print(f'The result TPE: {result}')
            # print(executor)
    average_time_1 = sum(time_lst) / len(time_lst)
    print(f'The time list TPE: {time_lst}')
    print(f'Time of TPE: {average_time_1}')

# Function to calculate the factorial of num with ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor1:
        time_lst_1 = []
        str_at_1 = time.time()
        for result_1 in executor1.map(factor, range(0, 5)):
            time_lst_1.append(time.time() - str_at_1)
            print(f'The result_PPE : {result_1}')
    average_time_2 = sum(time_lst_1) / len(time_lst_1)
    print(f'The time list PPE: {time_lst_1}')
    print(f'Time of PPE: {average_time_2}')
    if average_time_1 < average_time_2:
        print("________________________________________________")
        print(f'Average time TPE: {average_time_1} is better')
    else:
        print("________________________________________________")
        print(f'Average time PPE: {average_time_2} is better')
