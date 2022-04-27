# Functions
import re


def func_name(x, y, z):
    return x + y + z

# Function scope

# LEGB - Local, Enclosed, Global, Built-in
y, z = 1, 2
# http://com-copyright-wtf-archive-nonprod.s3.amazonaws.com/DO_NOT_DELETE_TEST/batches/ASCO_ST/3_JCO.18.00131.xml
def all_global():
    global x
    x = y + z

all_global()
print(x)

X = 99 # Global scope name: not used
def f1():
    X = 88 # Enclosing def local
    def f2():
        print(X) # Reference made in nested def
    f2()

f1() #

# Factory Functions: Closures - is a function that retains value(s) of another function (even though function is removed from memory) and uses it.
def maker(N):
    def action(X): # Make and return action
        return X ** N # action retains N from enclosing scope
    return action
    # example with lambda
    # return lambda X: X ** N

f = maker(2)
print(f(3))

# In python 2.x there wasn't look to search in enclosed scope, thus defaults assigment x=x was used to retain value.
def f1():
    x = 88
    def f2(x=x): # Remember enclosing scope X with defaults
        print(x)
    f2()
f1() # Prints 88

# loop variables may require defaults, not scopes
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x) # But all remember same last i!
        # acts.append(lambda x, i=i: i ** x) # Remember current i
    return acts

acts = makeActions()
print(acts[0](2)) # print the same 
print(acts[1](2)) # print the same
print(acts[2](2)) # print the same


# Nonlocal
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1 # now we have wite access to state
    return nested

f = tester(0)
f("spam")

# Gloabal vs nonlocal
def tester(start):
    def nested(label):
        # nonlocal state # Nonlocals must already exist in enclosing def!
        state = 0
        print(label, state)
    return nested

def tester(start):
    def nested(label):
        global state        # Globals don't have to exist yet when declared
        state = 0           # This creates the name in the module now
        print(label, state)
    return nested


def tester(start):
    global state # Move it out to the module to change it
    state = start # global allows changes in module scope
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested


# Class overloading as functions
class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label): # Intercept direct instance calls
        print(label, self.state) # So .nested() not required
        self.state += 1

h = tester(99)
h("juice")


# Function attributes
def tester(start):
    def nested(label):
        print(label, nested.state) # nested is in enclosing scope
        nested.state += 1 # Change attr, not nested itself
    nested.state = start # must Initialize state after func defined

    return nested

f = tester(2)
f("spam")
print(f.state)



# Args (Parameters)
"""Argument Matching Basics.
    Positionals: matched from left to right
    Keywords: matched by argument name
    Defaults: specify values for optional arguments that aren’t passed
    Varargs collecting: collect arbitrarily many positional or keyword arguments
    Varargs unpacking: pass arbitrarily many positional or keyword arguments
    Keyword-only arguments: arguments that must be passed by name

    func(value) Caller Normal argument: matched by position
    func(name=value) Caller Keyword argument: matched by name
    func(*iterable) Caller Pass all objects in iterable as individual positional arguments
    func(**dict) Caller Pass all key/value pairs in dict as individual keyword arguments
    def func(name) Function Normal argument: matches any passed value by position or name
    def func(name=value) Function Default argument value, if not passed in the call
    def func(*name) Function Matches and collects remaining positional arguments in a tuple
    def func(**name) Function Matches and collects remaining keyword arguments in a dictionary
    def func(*other, name) Function Arguments that must be passed by keyword only in calls (3.X)
    def func(*, name=value) Function Arguments that must be passed by keyword only in calls (3.X)
"""

# copying list
l = [1,2,3,4]
print(list(l))
print(list.copy(l))

# erro argument assigment syntax
# def f(a, *b, **d, c=6): print(a, b, c, d)
# keyword only arguments must be coded after * and before **
def f(a, *b, c=6, **d): print(a, b, c, d) # Collect args in header
def f(a, c=6, *b, **d): print(a, b, c, d) # c is not keyword-only here!

def func(a, b, c, d): print(a, b, c, d)
args = (1, 2, 3, 4)
func(*args)


def kwonly(a, *arg, b, c):
    print(a, arg, b, c)

kwonly(1, c=3, b=2)

# Refcount
import sys

iter(range(10))

y = "hello"
def greet(message=y):
    print(message.capitalize() + " " + y)

messages = [y]
greet(*messages)
print(sys.getrefcount(y))
"""
# Garbage Collector.
import gc
getitem()

# def gc_callback(phase, info):
#     print(f"GC phase:{phase} with info:{info}")

# gc.callbacks.append(gc_callback)
# x = []
# x.append(x)
# del x
# gc.collect()

# Generational GC
# gc.set_debug(gc.DEBUG_STATS)
gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_SAVEALL)
z = [0, 1, 2, 3]
del z
gc.collect()
gc.garbage

gc.get_count()
gc.collect(0) # generation to collect
gc.get_threshold()
"""

# trunck based - 

import os 

print(os.path.join(os.path.dirname(__file__), 'logs'))
