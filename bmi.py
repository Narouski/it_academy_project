sex = input("Укажите ваш М или Ж: ").lower()
height = float(input("Введите ваш рост в см: "))
weight = float(input("Введите ваш вес в кг: "))
BMI = round(weight / (height / 100) ** 2, 2)
x = '=' * 50

if sex == 'm' or sex == 'м':
    if BMI <= 16:
        print(f"Ваш BMI равен {BMI}. У вас дефицит массы.")
    elif 16 < BMI <= 18:
        print(f"Ваш BMI равен {BMI}. У вас недостаточная масса тела.")
    elif 18.5 < BMI <= 23.8:
        print(f"Ваш BMI равен {BMI}. Он соответствует норме.")
    elif 23.9 < BMI <= 28.5:
        print(f"Ваш BMI равен {BMI}. У вас ожирение первой степени.")
    elif 28.6 < BMI <= 38.9:
        print(f"Ваш BMI равен {BMI}. У вас ожирение второй степени.")
    elif 39 < BMI <= 40:
        print(f"Ваш BMI равен {BMI}. У вас ожирение третьей степени.")
elif sex == 'w' or sex == 'ж':
    if BMI <= 16:
        print(f"Ваш BMI равен {BMI}. У вас дефицит массы.")
    elif 16 < BMI <= 20:
        print(f"Ваш BMI равен {BMI}. У вас недостаточная масса тела.")
    elif 20.1 < BMI <= 24.9:
        print(f"Ваш BMI равен {BMI}. Он соответствует норме.")
    elif 25 < BMI <= 29.9:
        print(f"Ваш BMI равен {BMI}. У вас ожирение первой степени.")
    elif 30 < BMI <= 39.9:
        print(f"Ваш BMI равен {BMI}. У вас ожирение второй степени.")
    elif BMI > 40:
        print(f"Ваш BMI равен {BMI}. У вас ожирение третьей степени.")
else:
    print(f"Что-то пошло не так, попробуйте ещё раз!")

print('16<' + x[:int(BMI) - 17] + '|' + x[50 - int(BMI):] + '>50')

def menu():
    pass

def user_list():
    pass

def user_info():
    pass

def changes_data_user():
    pass

def delete_user():
    pass

def make_user():
    pass

def ex_program():
    pass