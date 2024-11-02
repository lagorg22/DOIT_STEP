
class LoggingMeta(type):
    def __new__(cls, name: str, bases: tuple, dct: dict):
        instance = super().__new__(cls, name, bases, dct)
        methods = [key for key, val in dct.items() if callable(val)]
        print(f'New class named: {name} has been created.\n'
              f'Methods of {name}: {methods}\n')

class Car(metaclass=LoggingMeta):
    def __init__(self, brand: str, model: str):
        self.__brand = brand
        self.__model = model

    def brand(self):
        return self.__brand

    def model(self):
        return self.__model

    def __str__(self):
        return f'Brand: {self.brand}, Model: {self.model}'

class Book(metaclass=LoggingMeta):
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    def name(self):
        return self.__name

    def author(self):
        return self.__author

    def __str__(self):
        return f'Name: {self.name}, Author: {self.author}'
