a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))
c = int(input("Введите третье значение: "))

task_1 = a == 0 or b == 0 or c == 0 or "Нулевых значений нет"
print(task_1)

#task_2 = a or b != 0 and c != 0 or 'Все нули'
#print(task_2)

if a > (b + c):  # task_3
    print(a - b - c)
if a < (b + c):  # task_4
    print(b + c - a)
if a > 50 and (a < b or a < c):  # task_5
    print('Вася')
if a > 5 or (b == 7 and c == 7):  # task_6
    print('Петя')
