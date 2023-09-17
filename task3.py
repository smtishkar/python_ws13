'''
Создайте класс с базовым исключением
и дочерние классы-исключения:
ошибка уровня, ошибка доступа.
'''
import json


class MyException(Exception):
    pass


class MyExceptionLevel(MyException):
    pass


class MyExceptionAccess(MyException):
    pass

'''
Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
'''


class User:
    def __init__(self, user_id: int, level: int, user_name: str) -> None:
        self.level = level
        self.__user_id = user_id
        self.user_name = user_name

    def load(self, file_name: str):
        with open(f'{file_name}.json', 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)
            print(data)
            users: set = set()
            for one_user in data:
                print(*one_user.values())
                users.add(User(*one_user.values()))
        return users

    def __repr__(self):
        return f'Имя: {self.user_name} Id: {self.__user_id} Уровень доступа: {self.level} '


if __name__ == '__main__':
    p1 = User(user_id=7, level=7, user_name="Test")
    print(p1.load(file_name='test'))