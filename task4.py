import json

class MyException(Exception):
    pass


class MyExceptionLevel(MyException):
    pass


class MyExceptionAccess(MyException):
    pass


class User:
    def __init__(self, user_id: int, level: int, user_name: str) -> None:
        self.__user_id = user_id
        self.level = level
        self.user_name = user_name

    def load(self, filename: str):
        with open(f'{filename}.json', "r", encoding='utf-8') as file:
            data = json.load(file)
            users: set = set()
            for one_user in data:
                users.add(User(*one_user.values()))
        return users

    def __eq__(self, other):
        return self.user_name == other.user_name and self.__user_id == other.__user_id

    def __hash__(self):
        return int(self.__user_id)

    def __repr__(self):
        return f'Имя:{self.user_name} id:{self.__user_id} Уровень доступа: {self.level}'


# if __name__ == "__main__":
# p1 = User(level = 7, user_id = 10, user_name = "Alex")
# print(p1.load(filename = "test"))


# Задача 5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.



class Project:
    def __init__(self):
        self.users = User(level=7, user_id=132340, user_name="Alex").load("test")
        self.entered_user = None

    def reload_users(self):
        self.users = User(level=7, user_id=132340, user_name="Alex").load("test")

    def enter(self, id: int, name: str):
        that_user = User(level=None, user_id=id, user_name=name)
        if that_user not in self.users:
            raise MyExceptionAccess
        for i in self.users:
            if i == that_user:
                self.entered_user = i


    def add_user(self, id, level, name):
        if self.entered_user.level < level:
            raise MyExceptionLevel
        self.users.add(User(id, level, name))

if __name__ == '__main__':
    proj = Project()
    proj.enter("000021", 'Fedor')
    proj.add_user('093943', 1, "Anna")
    print(proj.users)