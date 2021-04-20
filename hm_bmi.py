user_list = {}
users = []


def update_user():
    print("changes_data_user")


def delete_user():
    choice_to_delete = input("Введите имя пользователя которого хотите удалить: ")
    if choice_to_delete in user_list:
        print(*f"Пользователь {user_list.pop(choice_to_delete)} был удалён")
        return main()
    else:
        print("Пользователя с данным именем нет")
        return main()


def make_user():
    first_name = input("Введите ваше имя: ")
    second_name = input("Введите вашу фамилию: ")
    age = input("Введите ваш возрост: ")
    users.extend((first_name, second_name, age))
    user_list[first_name] = users
    print(f"Пользователь {first_name} {second_name} создан успешно!")
    return main()


def users_list():
    print(*users[::3])
    return main()


def user_info():
    print(user_list)
    return main()


def ex_program():
    print("Всего доброго!")
    exit(0)


def main():
    menu = """
    1. Список пользователей.
    2. Информация о пользователе.
    3. Изменить данные пользователя.
    4. Удалить пользователя.
    5. Создать пользователя.
    6. Выход.
    """
    print(menu)

    choice = int(input("Выберите действие: "))

    if choice == 1:
        users_list()
    elif choice == 2:
        user_info()
    elif choice == 3:
        update_user()
    elif choice == 4:
        delete_user()
    elif choice == 5:
        make_user()
    elif choice == 6:
        ex_program()
    else:
        print("Упс, что-то пошло не так, попробуйте ещё раз")
        return main()


main()

