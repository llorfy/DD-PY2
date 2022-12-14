from typing import Union
import doctest

#-----------Украшение комнаты к новому году-------------

# Класс "Гирлянда на окно"
class Garland:
    def __init__(self, window_width: Union[int, float], garland_width: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Гирлянда"
        :param window_width: Ширина окна
        :param garland_width: Длина гирлянды
        Примеры:
        >>> grlnd = Garland(100, 100)  # инициализация экземпляра класса
        """
        if not isinstance(window_width, (int, float)):
            raise TypeError
        if window_width < 0:
            raise ValueError
        self.window_width = window_width

        if not isinstance(garland_width, (int, float)):
            raise TypeError
        if garland_width < 0:
            raise ValueError
        self.garland_width = garland_width

    def is_empty_window(self) -> bool:
        """
        Функция, которая проверяет, есть ли гирлянда на окне
        :return: Есть ли гирлянда на окне
        Примеры:
        >>> grlnd = Garland(100, 0)
        >>> grlnd.is_empty_window()
        """
        ...

    def is_suitable_garland(self) -> str:
        """
        Функция, которая проверяет, подходит ли по размеру гирлянда
        :return: Подходит ли гирлянда (больше, меньше или по размеру)
        Примеры:
        >>> grlnd = Garland(100, 120)
        >>> grlnd.is_suitable_garland()
        """
        ...

# Класс "Игрушки для ёлки"
class Christmas_tree_decorations:
    def __init__(self, capacity: int, decorations: dict):
        """
        Создание и подготовка к работе объекта "Ёлочные игрушки"
        :param capacity: Сколько игрушек помещается на ёлку
        :param decorations: Словарь, по ключу которого цвет игрушек, а значение - количество
        Примеры:
        >>> c_t_d = Christmas_tree_decorations(10, {'красный': 2, 'синий': 3, 'жёлтый': 5}) # инициализация экземпляра класса
        """
        if not isinstance(capacity, int):
            raise TypeError
        if capacity < 0:
            raise ValueError
        self.capacity = capacity

        if not isinstance(decorations, dict):
            raise TypeError
        for key in decorations:
            if decorations[key] < 0:
                raise ValueError
            if not isinstance(decorations[key], int):
                raise ValueError
        self.decorations = decorations

    def is_suitable_decorations(self) -> bool:
        """
        Функция, которая проверяет, влезут ли игрушки на ёлку
        :return: Влезут ли игрушки (если игрушек больше, то выдаёт ошибку)
        Примеры:
        >>> c_t_d = Christmas_tree_decorations(10, {'красный': 2, 'синий': 3, 'жёлтый': 5})
        >>> c_t_d.is_suitable_decorations()
        """
        ...

    def change_decorations(self, color_: str, num_: int) -> None:
        """
        Функция, которая заменяет количество игрушек выбранного цвета
        :return: Изменённый список игрушек
        Примеры:
        >>> c_t_d = Christmas_tree_decorations(10, {'красный': 2, 'синий': 3, 'жёлтый': 5})
        >>> c_t_d.change_decorations('красный', 1)
        """
        ...

    def change_color(self, color_1: str, color_2: str) -> None:
        """
        Функция, которая заменяет выбранный цвет игрушек
        :return: Изменённый список игрушек
        Примеры:
        >>> c_t_d = Christmas_tree_decorations(10, {'красный': 2, 'синий': 3, 'жёлтый': 5})
        >>> c_t_d.change_decorations('красный', 'розовый')
        """
        ...

# Класс "Остальные украшения для комнаты"
class Other_decorations:
    def __init__(self, money: Union[int, float], o_decorations: dict):
        """
        Создание и подготовка к работе объекта "Украшения для комнаты"
        :param money: Имеющийся бюджет
        :param o_decorations: Словарь с названием украшения и его стоимостью
        >>> o_d = Other_decorations(1000, {'венок': 500, 'мишура': 100})  # инициализация экземпляра класса
        """
        if not isinstance(money, (int, float)):
            raise TypeError
        if money < 0:
            raise ValueError
        self.money = money

        if not isinstance(o_decorations, dict):
            raise TypeError
        for key in o_decorations:
            if o_decorations[key] < 0:
                raise ValueError
            if not isinstance(o_decorations[key], (int, float)):
                raise ValueError
        self.o_decorations = o_decorations

    def is_enough_money(self) -> bool:
        """
        Функция, которая проверяет, хватит ли денег на украшения
        :return: Хватит ли денег
        Примеры:
        >>> o_d = Other_decorations(1000, {'венок': 500, 'мишура': 100})
        >>> o_d.is_enough_money()
        """
        ...

    def add_decorations(self, name_: str, price_: int) -> None:
        """
        Функция, которая добавляет одно украшение
        :return: Изменённый список украшений
        Примеры:
        >>> o_d = Other_decorations(1000, {'венок': 500, 'мишура': 100})
        >>> o_d.add_decorations('новогодняя свеча', 200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()

