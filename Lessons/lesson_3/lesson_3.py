a = 0 # global

def func():
    a = 12 # local
    def func_2():
        # enclosed
        a = 32
    
    func_2()
    return a

print(func())

L = [1, 2, 3]
L = tuple(x + 10 for x in L)
print(type(L))


X = (1, 2)
Y = (3, 4)
list(zip(X, Y)) 
A, B = zip(*zip(X, Y))
print(A, B)


def gen_func():
    for i in range(10):
        yield i
        print(f"works {i}")

L = [1, 2, 3]
I = iter(L)
R = range(100)
I2 = iter(R)


def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next

for i in [1]:
    print(i)
else:
    print("works")

print(dir()) # return the names in the current scope.
