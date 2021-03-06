def show_menu():
    MENU = """
    1. Список пользователей.
    2. Информация о пользователе.
    3. Изменить данные пользователя.
    4. Удалить пользователя.
    5. Создать пользователя.
    6. Выход.
    """
    print(MENU)
    return int(input("Выберите действие: "))


def users_list():
    print("users_list")


def user_info():
    print("user_info")


def update_user():
    print("changes_data_user")


def delete_user():
    print("delete_user")


def make_user(first_name=input("Введите ваше имя: "),
              second_name=input("Введите вашу фамилию: "),
              age=input("Введите ваш возрост: ")):
    USERS = []
    USERS += first_name, second_name, age
    print(USERS)


def ex_program():
    print("Всего доброго!")
    exit(0)


ACTIONS = {
    1: users_list,
    2: user_info,
    3: update_user,
    4: delete_user,
    5: make_user,
    6: ex_program,
}


def select_action(answer: int):
    return ACTIONS.get(answer, show_menu)


def main():
    MENU = """
    1. Список пользователей.
    2. Информация о пользователе.
    3. Изменить данные пользователя.
    4. Удалить пользователя.
    5. Создать пользователя.
    6. Выход.
    """
    print(MENU)
    answer = 0

    while True:
        action = select_action(answer)
        answer = action()


main()
