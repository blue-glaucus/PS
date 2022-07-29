import random


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


array = list(range(11))
random.shuffle(array)
print('origin list: {}'.format(array))
print('result list: {}'.format(selection_sort(array)))