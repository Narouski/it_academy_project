height = float(input("Введите ваш рост в см: "))
weight = float(input("Введите ваш вес в кг: "))

BMI = weight / (height/100) ** 2

x = '=' * 60

print(f'Ваш BMI {round(BMI, 2)}')
print('16 ' + x[:int(BMI) - 16] + '|' + x[int(BMI):] + ' 60')
