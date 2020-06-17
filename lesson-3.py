""" the task 1 """
def m_fun():
    try:
        num_1 = int(input('Enter numbe one: '))
        num_2 = int(input('Enter numbe two: '))
        print(num_1 / num_2)
    except ValueError:
        print('Enter incorrect')
    except ZeroDivisionError:
        print("На ноль делить нельзя")
m_fun()

""" the task 2 """
def user_date (fname, sname, year, city, email, phone):
    print(f"Имя: {fname}, Фамилия: {sname}, Год: {year}, Город: {city}, Email: {email}, Телефон: {phone}")
user_date(fname="John", sname="Smith", year=1989, city="New York", email="admin@google.com", phone=89123456789)

""" the task 3 """
    """
    Возвращает сумма 2х максимальных числе в массиве
    
    (number, number) -> number
    
    >>> my_func(123,5135,23)
    5258
    """
def my_func(num1, num2, num3):
    date = [num1, num2, num3]
    result = sum(date) - min(date)
    return result
print(my_func(123,5135,23))
""" the task 4 """
def my_func(x, y):
    if x < 0 or y > 0:
        return print("Введенные данные не корректны")
    i = 0
    result = 0
    while i < abs(y):
        result = x if i == 0 else result * x
        i += 1
    return print(round(1 / result, 8))
my_func(2,-2)

def my_func2(x, y):
    if x < 0 or y > 0:
        return print("Введенные данные не корректны")
    return print(round(x ** y, 8))
my_func2(2,-2)

""" the task 5 """
def fun_sum():
    total_sum = 0
    while True:
        num = input('Введите числа с пробелами: ')
        date = num.split()
        try:
            date = date[:date.index("q")]
        except ValueError:
            pass
        for ind, key in enumerate(date):
            date[ind] = int(key)

        total_sum += sum(date)
        print(total_sum)
        if num.find("q") > -1:
            break
    return total_sum
fun_sum()

""" the task 6 """
def in_func(word):
    for i in word:
        if ord(i) < 97 or ord(i) > 122:
            print('Error')
            return
    return chr(ord(word[0]) - 32) + word[1:]
print(in_func('hello'))

my_S = input("Enter str: ")
words = my_S.split()
new_words = []
for i in words:
    if in_func(i) == None:
        print('Error')
        break
    else:
        new_words.append(in_func(i))
print(' '.join(new_words))