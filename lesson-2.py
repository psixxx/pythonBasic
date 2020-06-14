""" the task 1 """
my_list_task_1 = [1, "str", [20,50,100], {"key": 123, 2: "good"}, (True, False), {"a", "b", 2}, True, None]
for ind, el in enumerate(my_list_task_1, 1):
    print(ind, type(el))

""" the task 2"""
my_list_task_2 = []
while True:
    a = input("Enter num: ")
    if a == "":
        break
    my_list_task_2.append(a)
print(my_list_task_2)
for i in range(0, len(my_list_task_2)-1, 2):
    my_list_task_2[i], my_list_task_2[i+1] = my_list_task_2[i+1], my_list_task_2[i]
print(my_list_task_2)

""" the task 3"""
my_list_task_3 = [
    {'January': "Winter"},
    {'February': "Winter"},
    {'March': "Spring"},
    {'April': "Spring"},
    {'May': "Spring"},
    {'June': "Summer"},
    {'July': "Summer"},
    {'August': "Summer"},
    {'September': "Autumn"},
    {'October': "Autumn"},
    {'November': "Autumn"},
    {'December': "Winter"},
]
month = int(input('Enter month 1-12: '))
for key, value in my_list_task_3[month-1].items():
    print(f'Month - {key} and "Season - {value}')

""" the task 4"""
my_list_task_4 = input('Enter string: ')
my_list = my_list_task_4.split()

for i in range(len(my_list)):
    print(f"{i} - {my_list[i]:.10}")

""" the task 5"""
my_list_task_5 = [7, 5, 3, 3, 2]
num = int(input('Enter number: '))

if my_list_task_5.count(num) == 0:
    for i in my_list_task_5:
        if i < num:
            my_list_task_5.insert(my_list_task_5.index(i), num)
            break
    my_list_task_5.append(num) if my_list_task_5.count(num) == 0 else None
else:
    my_list_task_5.insert(my_list_task_5.index(num) + my_list_task_5.count(num), num)
print(my_list_task_5)


""" the task 6"""
products, name_list, price_list, count_list, unit_list = [], [], [], [], []
i = 1

while True:
    want = int(input('Enter? 1/0: '))
    if want == 1:
        name = input('Enter name: ')
        price = int(input('Enter price: '))
        count = int(input('Enter count: '))
        unit = input('Enter unit: ')

        products.append((i, {"name": name, "price" : price, "count": count, "unit": unit}))
        name_list.append(name) if name_list.count(name) == 0 else None
        price_list.append(price) if name_list.count(price) == 0 else None
        count_list.append(count) if name_list.count(count) == 0 else None
        unit_list.append(unit) if name_list.count(unit) == 0 else None
        i += 1
    else:
        break
analytics = {'name': name_list, 'price': price_list, 'count': count_list, 'unit': unit_list}
print(products)
print(analytics)

