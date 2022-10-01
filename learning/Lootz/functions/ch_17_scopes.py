w"""
X = 99 # Global (module) scope X

def func():
    X = 88 # Local (function) scope X: a different variable

# Exception namespace
e = "error"
print(e)

try:
    a = 1/0
except ZeroDivisionError as e: # variable e will be deleted if exception happens
    print(e)

# NameEror - because variables used in except block are local and deleted after usage
print(e)
"""

import builtins

from django import conf
print(type(dir(builtins))) 
# for builtin in dir(builtins):
#     print(dir(builtin)) 
# len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('__')])
"""
Raises
Table View
RM's KPI (-1)


Фильтрация по локации и менеджерам
Check 


"""

a = 1

def func():
    b = 2
    def nested():
        nonlocal b
        c = 3
        b = b + 2
        print(a, b, c)
    
    nested()

func()
print(a)

def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)

import update
import config

print(config.a, config.b)

d = {
    1: 2,
    "34": 3,
    (1,2): "hello",
    # [2,3]: "yes",
}