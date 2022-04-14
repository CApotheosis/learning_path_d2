"""
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
print(type(dir(builtins))) 
# for builtin in dir(builtins):
#     print(dir(builtin)) 
# len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('__')])
"""
Raises
Table View
RM's KPI (-1)


Фильтрация по локации и менежерам
Check 


"""
