"""Програма сортування списку та розрахунку середнього часу кожної ітерації"""
import time
from random_words import RandomWords

str_list = []
w = RandomWords()
for i in range(0, 5000):
    str_list.append(w.random_word())
print("List for sorting:", str_list)


def bubble_sort(data):
    """Bubble Sort Algorithm"""
    length = len(data)
    for i_index in range(length):
        swapped = False
        for j_index in range(0, length - i_index - 1):
            if data[j_index] > data[j_index + 1]:
                data[j_index], data[j_index + 1] = data[j_index + 1], data[j_index]
                swapped = True
        if not swapped:
            break
    return data


def sort(lst, num):
    """Calculation of average sort processing time"""
    time_lst = []
    for step in range(0, num):
        timer_strt = time.time()
        bubble_sort(lst)
        timer_fin = time.time()
        sort_time = timer_fin - timer_strt
        time_lst.append(sort_time)
    average_time = sum(time_lst) / len(time_lst)
    print("After sorting: ", lst)
    print("List of times:", time_lst)
    print(f"Average_time: {average_time}")


sort(str_list, 5)
