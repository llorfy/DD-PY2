class Flowerbed:
    """
    Класс, представляющий клумбу
    """
    def __init__(self, name: str, num: int):
        """
        Инициализация объекта класса Flowerbed

        :param name: название для клумбы цветов
        :param num: количество цветов на клумбе
        """
        self.name = name
        self.num = num
        self.max_num = None

    def __str__(self) -> str:
        """
        Метод для строкового представления объекта класса Flowerbed

        :return: строковое представление объекта класса Flowerbed
        """
        return f"Название: {self.name}, количество цветов: {self.num}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр класса Flowerbed.

        :return: строка, показывающая, как может быть инициализирован экземпляр класса Flowerbed
        """
        return f"{self.__class__.__name__}(name={self.name!r}, num={self.num!r}"

    #метод, который можно наследовать в дочерний
    def get_max_num(self) -> int:
        """
        Метод, возвращающий максимально возможное количество цветов,
        которые можно разместить на клумбе (max_num).

        :return: максимально возможное количество цветов
        """
        ...

    #метод, который нужно перегрузить в дочернем
    def is_that_amount_possible(self) -> bool:
        """
        Метод, который проверяет, поместится ли заданное количество цветов
        на клумбу.

        :return: True, если цветы поместятся и False если нет
        """
        ...


class Roses(Flowerbed):
    """
    Класс, представляющий розы

    Строковое представление класса наследуется из базового класса Roses.
    """
    def __init__(self, name: str, num: int, color: str, num_r: int):
        """
        Инициализация объекта класса Roses

        :param name: название клумбы
        :param num: количество цветов на клумбе
        :param color: цвет роз
        :param num_r: количество роз
        """
        Flowerbed.__init__(name, num)
        self.color = color
        self.num_r = num_r

    def __str__(self) -> str:
        """
        Метод для строкового представления объекта класса Roses

        :return: строковое представление объекта класса Roses
        """
        return f"Название: {self.name}, цвет: {self.color}, количество роз: {self.num_r}"

    def __repr__(self) -> str:
        """
        Метод возвращает строку, показывающую,
        как может быть инициализирован экземпляр класса Roses.

        :return: строка, показывающая, как может быть инициализирован экземпляр класса Roses
        """
        return f"{self.__class__.__name__}(name={self.name!r}, color={self.color!r}, num_r={self.num_r!r}"

    def is_that_amount_possible(self) -> bool:
        """
        Метод, который проверяет, поместится ли заданное количество цветов
        на клумбу.
        Необходимо перегрузить, т. к. для роз мы обозначили другое количество.

        :return: True, если цветы поместятся и False если нет
        """
        ...

#подобным образом можно задать дочерний класс, например, нарциссов

if __name__ == "__main__":
    # Write your solution here
    pass
