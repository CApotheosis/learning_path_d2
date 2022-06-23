'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# import this

a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

# set_1 = {(1,2, [4,5]), 5, 4} # set doesn't support mutable types as arguments
# print(set_1)

import sys
# print(sys.path)

a = 2
print("addres" , id(2)) # to get addres in memory
print("addres" , id(a)) # to get addres in memory

"""
else in for cycle will work only if cycle was succesfully executed without break or error
same for while loop
pass statement is a null statement

func_name.__doc__ - returns function docstring if exist

function with arguments pattern:
def func_name(name, psw="deafult", *args, mandatory_value, mandatory_default_value="default", **kwargs):
    pass

Advantages of Recursion
- Recursive functions make the code look clean and elegant.
- A complex task can be broken down into simpler sub-problems using recursion.
- Sequence generation is easier with recursion than using some nested iteration.
Disadvantages of Recursion
- Sometimes the logic behind recursion is hard to follow through.
- Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
- Recursive functions are hard to debug.

anonymous functions:
lambda argumentsL: expression

Python variables:
int
float
complex
string
list
tuple
set
dictionary
frozenset

OrderedDict
Decimal
Named Tuples
Fractions
"""
def func_name(name, psw="deafult", *args, mandatory_value, mandatory_default_value="default", **kwargs):
    print(name, psw, args, mandatory_value, mandatory_default_value, kwargs, sep="\n")

func_name(2, (3,4,5), mandatory_value="mandatory_value", key="value")



mapped = map(lambda x: x**2, range(10))
next(mapped)
next(mapped)
next(mapped)
next(mapped)
for i in mapped:
    print(i)
i_map = iter(mapped)
# print( next(i_map) )

numbers = list(range(0, 10, 2))
i_numbers = iter(numbers)
print( next(i_numbers))
I_2 = iter(i_numbers)
print( next(i_numbers), next(I_2), next(i_numbers))

s = {1, 2, 3, 6, 7, 8}
print(tuple(enumerate(s)))


d = {
    1: 2,
    1: 3,
}
print(len(d), d, d.pop(1))



import sys
# get the number of blocks in use for each of the class size pools.
# sys._debugmallocstats() 

from dis import dis
y = "hello"
def greet(message=y):
    print(message.capitalize() + " " + y)

messages = [y]
greet(*messages)
dis(greet)

import sys
print(sys.getrefcount(10000))
import gc
gc.freeze()