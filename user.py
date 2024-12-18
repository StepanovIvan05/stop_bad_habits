import time
from datetime import datetime


class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.habits_list = []

    def add_habbit(self, name, count_relapse=0):
        self.habits_list.append(Habit(name, count_relapse))

    def add_comm(self, text, habit):
        var = self.habits_list[self.habits_list.index(habit)]
        var.add_comment(text)

    def delete_habbit(self, habit):
        """
        тут еще не знаю как лучше привычку или индекс привычки в списке
        :param habit: привычка или индекс
        :return:
        """
        self.habits_list.remove(habit)

    def get_login(self):
        """
        получение логина для поиска пользователя по логину
        проверка на то что логин существует должна проводиться при создании пользователя
        то есть в мейне (короче не в этом файле)
        :return:
        """
        return self.__login

    def check_password(self, password):
        """
        для входа по логину находим пользователя и проверяем пароль
        :param password:
        :return:
        """
        return password == self.__password

    def set_password(self, new_password):
        """
        для смены пароля (на будущее)
        :param new_password:
        :return:
        """
        self.__password = new_password


class Habit:
    def __init__(self, name, count_relapse):
        """
        тут начальное время фиксируется и дата
        подумал может полезно когда у типа 8374958 рецидивов
        посмотреть когда он начал пытаться бросить
        в данный момент просмотр истории рецидивов не предусмотрен
        хотя можно коммент добавлять с данными
        :param name:
        :param count_relapse:
        """
        self.name = name
        self.start_time = time.time()
        self.start_date = datetime.now()
        self.count_relapse = count_relapse
        self.comments = []

    def add_comment(self, comment):
        """
        список со строками
        :param comment:
        :return:
        """
        self.comments.append(comment)

    def add_relapse(self):
        """
        рецидив обновляет время и возвращает время воздержания
        в секундах
        :return:
        """
        self.count_relapse += 1
        self.start_time = time.time()
