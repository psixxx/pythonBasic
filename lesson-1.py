"""------------ задание 1 ------------"""

x = 1
y = 2
my_str = "Hello my friends!"
print(my_str)

name = input('Введите ваше имя: ')
print(name)

num1 = int(input('Введите первое число: '))
num2 = init(input('Введите второе число: '))
sum = num1 + num2
print(sum)

"""------------ задание 2 ------------"""

answ = int(input('Введите время в секундах: '))
print(f"{answ // 3600:02}:{(answ % 3600) // 60:02}:{(answ % 3600) % 60:072}")

"""------------ задание 3 ------------"""

number = input("Введите число: ")
print(f"{int(number)} + {int(number * 2)} + {int(number * 3)} = {int(number) + int(number * 2) + int(number * 3)}")

"""------------ задание 4 ------------"""

dz_4_num = int(input("Введите число: "))
dz_4_max_num = 0
while dz_4_num > 0:
    x = dz_4_num % 10
    if x == 9:
        dz_4_max_num = x
        break
    if x > dz_4_max_num:
        dz_4_max_num = x
    dz_4_num = dz_4_num // 10
print(dz_4_max_num)

"""------------ задание 5 ------------"""

rev = int(input("Введите данные по вырчке: "))
cost = int(input("Введите данные по издержкам: "))
if rev > cost:
    print("Компания работаем в прибыль")
    print(f"Соотношение приыбли к выручке составляет: {((rev - cost) / rev) * 100:.0f}%")
    workers = int(input("Сколько сотрудников в компании? "))
    print(f"Прибыль компании в расчете на одного сотрудника составляет: {(rev - cost) / workers:.0f}")
elif rev < cost:
    print("Компания работаем в убыток")
else:
    print("Компания работает в ноль")

"""------------ задание 6 ------------"""

a_km = int(input('Первый день километров: '))
b_km = int(input('Цель километров: '))
day = 1
while True:
    if day == 1:
        print(f"{day}-й день: {a_km}")
    else:
        a_km = (a_km * 10 / 100) + a_km
        print(f"{day}-й день: {a_km:.2f}")
    if a_km > b_km:
        break
    day += 1
print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {b_km} км")
