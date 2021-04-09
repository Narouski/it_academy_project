height = float(input("Введите ваш рост : "))
weight = float(input("Введите ваш вес: "))

BMI = weight / (height/100) ** 2

print(f'Ваш BMI {round(BMI, 2)}')
