""" the task 1 """
data = []
while True:
    my_str = input("Введите данные: ")
    if my_str == "":
        break
    data.append(my_str + "\n")
with open("lesson-5.txt", "w", encoding="utf-8") as m_file:
    m_file.writelines(data)

""" the task 2 """
with open("lesson-5.txt", "r", encoding="utf-8") as m_file:
    i = 0
    for line in m_file:
        words = len(line.split())
        i += 1
        print(f"Строка №{i} Количество слов в строке - {words}")
    print(f"Количество строк - {i}")

""" the task 3 """
with open("text_3.txt", "r", encoding="utf-8") as m_file:
    names = []
    i = 0
    sum = 0
    for line in m_file:
        m_Str = line.split()
        if float(m_Str[1]) < 20000:
            names.append(m_Str[0])
        sum += float(m_Str[1])
        i += 1
    avg_sum = sum / i
    print(f"Список сотрудников: {', '.join(names)}")
    print(f"Средняя зарплата: {avg_sum}")

""" the task 4 """
with open("text_4.txt", "r", encoding="utf-8") as m_file:
    rus_num = ["Один", "Два", "Три", "Четыре"]
    i = 0
    result = []
    for line in m_file:
        m_Str = line.split()
        m_Str[0] = rus_num[i]
        i += 1
        result.append(" ".join(m_Str) + "\n")
    with open("result.txt", "w", encoding="utf-8") as res_file:
        res_file.writelines(result)

""" the task 5 """
with open("in_data.txt", "w", encoding="utf-8") as m_file:
    rus_num = [str(el) for el in range(0, 30)]
    m_file.write(" ".join(rus_num))

with open("in_data.txt", "r", encoding="utf-8") as m_file:
    data = m_file.read().split()
    j = 0
    for i in data:
        j += int(i)
    print(f"Сумма чисел: {j}")

""" the task 6 """
with open("text_6.txt", "r", encoding="utf-8") as m_file:
    dict_lessons = {}
    for line in m_file:
        line_parts = line.split()
        name = line_parts[0].replace(":", "")
        sum_lessons = 0
        for part in line_parts[1:]:
            if part == "-":
                continue
            else:
                sum_lessons += int(part[0:part.find("(")])
        dict_lessons.update({name: sum_lessons})
    print(dict_lessons)

""" the task 7 """
import json

with open("text_7.txt", "r", encoding="utf-8") as m_file:
    dict_comp = {}
    avg_profit = 0
    sum_profit = 0
    i = 0
    for line in m_file:
        line_parts = line.split()
        profit = int(line_parts[2]) - int(line_parts[3])
        dict_comp.update({line_parts[0]: profit})
        if profit > 0:
            sum_profit += profit
            i += 1

    avg_profit = sum_profit / i
    result = [dict_comp, {"average_profit": avg_profit}]

    with open("out_data_7.json", "w", encoding="utf-8") as out_file:
        json.dump(result, out_file, sort_keys=True, indent=4, ensure_ascii=False)

