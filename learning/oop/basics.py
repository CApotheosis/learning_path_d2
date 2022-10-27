"""
Inheritance - is passing an object into another as a parent which results in inheriting objects attributes and methods
Search algorithm in objects:
Find the first occurrence of attribute by looking in object, then in all classes above it, from bottom to top and left to right.

Polymorphism is the provision of a single interface to entities of different 
types or the use of a single symbol to represent multiple different types.
Polymorphism in python is method implementation with the same name for different object types doing same thing.
Example is len. 

Encapsulation refers to the bundling of data with the methods that operate on that data, 
or the restricting of direct access to some of an object's components.
Encapsulation is the process of packing data and function into a bundle of attributes and methods to use for ourselves.

Abstraction is the process of hiding information (abtracting) and giving access to only what's necessary.
Абстракция - это использование минимально необходимого 
"""
# Everything in pyton is an object
# print(type(None)) 
# print(type(True))
# print(type(1))
# print(type(2.3))
# print(type('hi'))
# print(type([]))
# print(type({}))
# print(type(()))

class Person: # class creation

    membership = True # Class object attribute - static
    _secret = "secret code"
    
    

    def __init__(self, name): # self is a reference to Person class
        if Person.membership:
            self.name = name # attribute - dynamic for every instance

    def get_class(self):
        print(self)

    def shout(self):
        print(f'My name is {self.name}')


person_1 = Person("Carol") # instiantiate an object
person_1.get_class()
person_1.shout()
print("secret:", Person._Person__super_secret)
# print(repr(person_1))
# print(str(person_1))
# print(help(person_1)) class info
print("hasattr", hasattr(person_1, "name"))

# @classmethod
class Player:
    """classmethod is likely to self, but instead of self we use cls keyword to reference class
    classmethod can be used without intanciating class and creatin __init__ dunder method
    """
    arr = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} {self.age}"
    # @classmethod
    # def add_nums(cls, num_1, num_2):
    #     return num_1 + num_2

    # intanciating an object with cls
    @classmethod
    def get_player_age(cls, num_1, num_2, a):
        cls.a = a
        return cls("Clark", num_1 + num_2) # Here, we can override basic __init__ - method with cls

    @staticmethod
    def add_nums_2(num_1, num_2):
        return num_1 + num_2

# print(Player.add_nums(1, 4))
player = Player("Joe", 43)
print(player)
player_1 = Player(2, 3)
print(player_1)

{}.__getattribute__

class A:
    def __init__(self, a) -> None:
        A.a = a

print(A(1))
print(A(2))

a_1 = A(1)
a_2 = A(1)
print(a_1)
print(a_2)

"""
    Method resolution order (MRO) - метод для определения очереди наследования
    в классах. Когда мы наследуем класс, то мы создаем некую зависимость одного
    класса от другого, но если таких наследований много, то можно и запутаться
    от кого наследуется переменная или метод в классе. Чтобы узнать, мы можем использовать
    метод mro() и определить важность наследования, тем самым узнать что мы зовём и что
    получим  
"""
# class A:
#     num = 10
#     a = 20

# class B(A):
#     a = 1

# class C(A):
#     num = 1

# class D(B, C):
#     pass

# print(D.num)
# print(D.a)
# print(D.mro())

#     A
#   /  \
#  /    \
# B      C
#  \    /
#   \  /
#    D

# class X: pass
# class Y: pass
# class Z: pass
# class A(X, Y): pass
# class B(Y, Z): pass
# class C(B, A, Z): pass

# print(C.mro())

# class Person(object): pass

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Проверка вызова `super` и `__init__`
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()

s = MyStock('GOOG', 100, 490.1, 1)
print()
print(s.__str__, '\n')

print(dir(s), '\n')


import datetime as dt

d = dt.datetime.now()

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    # def __str__(self):
    #     return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'

s = Date(d.strftime("%Y"), d.strftime("%B"), d.strftime("%A"))
print(s)


# Специальные методы для Математики
# Математические операторы включают вызывов этих методов

# a + b       a.__add__(b)
# a - b       a.__sub__(b)
# a * b       a.__mul__(b)
# a / b       a.__truediv__(b)
# a // b      a.__floordiv__(b)
# a % b       a.__mod__(b)
# a << b      a.__lshift__(b)
# a >> b      a.__rshift__(b)
# a & b       a.__and__(b)
# a | b       a.__or__(b)
# a ^ b       a.__xor__(b)
# a ** b      a.__pow__(b)
# -a          a.__neg__()
# ~a          a.__invert__()
# abs(a)      a.__abs__()
# a = 4
# b = 4
# print(a.__add__(b))
# print(a.__invert__())


# adhock
# pararmetrize