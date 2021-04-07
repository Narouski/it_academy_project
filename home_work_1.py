less = "Не знаю, как там в Лондоне, " \
       "я не была. Может, там собака — друг человека. " \
       "А у нас управдом — друг человека!"
print(less)

task1 = len(less)
print(task1)

task2 = less[::-1]
print(task2)

task3 = less.title()
print(task3)

task4 = less.upper()
print(task4)

task5_1 = less.count('нд')
task5_2 = less.count('ам')
task5_3 = less.count('о')
print(task5_1, task5_2, task5_3)

task6 = less.find('Лондон')
print(task6)
