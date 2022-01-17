"""

f = open("script.py")
# Reads file line ny line like __next__ method
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline(), "stop")

f.seek(0)
# the only difference is that __next__ returns StopIteration error instead of returning empty string
print(f.__next__()) # this is an iteration protocol in python
print(f.__next__())
print(f.__next__())
print(f.__next__())

f.seek(0)

for line in open('script.py'):       # Use file iterators to read by lines
    print(line.upper(), end='')       # Calls __next__, catches StopIteration

# Iteration protocol
L = [1, 2, 3]
I = iter(L)

print(I.__next__())
print(I.__next__())
print(I.__next__())

# Iteration on dictionaries
D = {'a':1, 'b':2, 'c':3}
for key in D: # views objects
    print(key, D[key])

# for loop will use the iteration protocol to grab one key each time 
# through, so we don't need to call keys() method 
I = iter(D)
print(next(I))

import os 
P = os.popen('dir')
print(P.__next__())
print(P.__next__())
# Error: object is not an iterator, because we didn't call iter() function
print(next(P)) 


L = [1, 2, 3]
L = [x + 10 for x in L]

# list compehension on files
# Files are closed when list is executed, because garbage-collected
lines = [line.rstrip() for line in open('script.py')]

# Built-in tools which make use of iteration protocol
sorted(open('script.py')) # returns new sorted list
# All other return iterable
map(str.upper, open('script.py')) 
zip(open('script.py'), open('script.py'))
enumerate(open('script.py'))
filter(bool, open('script.py'))
import functools, operator

functools.reduce(operator.add, open('script.py'))

# Other tools which implement iteration protocol
list(open('script.py'))
tuple(open('script.py'))
'&&'.join(open('script.py'))

a, b, c, d = open('script.py') # Sequence assignment
print(a, b, c, d)
a, *b = open('script.py') 
'y = 2\n' in open('script.py') # False
'x = 2\n' in open('script.py') # True
L = [11, 22, 33, 44]
L[1:3] = open('script.py')
print(L)
L = [11]
L.extend(open('script.py'))

set(open('script.py'))
{line for line in open('script.py')}
{ix: line for ix, line in enumerate(open('script.py'))}

# usage with *arg
def f(*arg): print(arg, sep='&')
f(*open('script.py')) 
f(*[1, 2, 3, 4]) 

# usage of zip to unpack values
X = (1, 2)
Y = (3, 4)
list(zip(X, Y)) 
A, B = zip(*zip(X, Y))
print(A, B)


R = range(10)
I = iter(R)
print(len(R), R[1])



D = dict(a=1, b=2, c=3)
K = D.keys() # A view object in 3.X, not a list
# print(next(K)) # error. is not an iterator
I = iter(K)
print(next(I))

f = open("script.py")
i = iter(f)
print(next(i))

"""