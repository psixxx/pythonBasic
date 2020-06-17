""" the task 1 """
from sys import argv

try:
    first, hours, h_rate, bonus = argv
    print(f"Зарплата сотрудника: {int(hours) * int(h_rate) + int(bonus)}")
except ValueError:
    print(f"Введены не верные данные, повторите попытку.")

""" the task 2 """
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [numbers[i] for i, v in enumerate(numbers) if i > 0 and numbers[i] > numbers[i-1]]
print(result)

""" the task 3 """
print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])

""" the task 4 """
numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in numbers if numbers.count(el) == 1])

""" the task 5 """
from functools import reduce

result = [i for i in range(100, 1001, 100)]
def my_func(prev_el, el):
    return prev_el + el
print(reduce(my_func, result))

""" the task 6 """
""" 1 подзадача"""
from itertools import count, cycle
from sys import argv

try:
    first, number = argv
    for el in count(int(number)):
        print(el)
        if el >= int(number) + 10:
            break
except ValueError:
    print(f"Введены не верные данные, повторите попытку.")

""" 2 подзадача"""
try:
    data = input("Введите набор слов: ")
    i = 0
    for el in cycle(data.split()):
        if i > 10:
            break
        print(el)
        i += 1
except ValueError:
    print(f"Введены не верные данные, повторите попытку.")

""" the task 7 """
from sys import argv

def fact(el):
    num = 1
    for i in range(1, el + 1):
        num = num * i
        yield num

try:
    first, number = argv
    for i in fact(int(number)):
        print(i)
except ValueError:
    print(f"Введены не верные данные, повторите попытку.")
