import random

def number_sorter():

    random_number = [random.random() for _ in range(1000)]

    sort_number = sorted(random_number, key = lambda x: x)

    print(sort_number)

number_sorter()