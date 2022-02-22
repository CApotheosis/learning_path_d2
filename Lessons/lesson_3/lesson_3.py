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

Report status for today by countries:



Uzbekistan: Time of parsing 18:00 (UTC 0) - 23:00 (UTC 5).
Today: Unable to generate due to linkedin error, but everything else worked.



manual-check: Fine, linkedin files were parsed.




Kazakhstan: Time of parsing 19:00 (UTC 0) - 24:00 (UTC 5)
Today: Unable to generate due to linkedin error, but everything else worked.



manual-check: Fine, linkedin files were parsed.




Georgia: Time of parsing 20:00 (UTC 0) - 1:00 (UTC 5)
Today: Unable to generate due to linkedin error, but everything else worked. Aggregator is disabled



manual-check: Fine, linkedin files were parsed.




Armenia: Time of parsing 21:00 (UTC 0) - 2:00 (UTC 5)
Today: Unable to generate due to linkedin error, but everything else worked. Dataart error is still present.



manual-check: Linked in files were parsed, but got (ProtocolError, MaxRetryError) for all companies and failed on statistics.




Lithuania: Time of parsing 22:00 (UTC 0) - 3:00 (UTC 5)
Today: Unable to generate due to linkedin error, but everything else worked except Statistics.



manual-check: Linked in files were parsed, but got (ProtocolError, MaxRetryError) for all companies (except wargaming) and failed on statistics.




Belarus: Time of parsing 23:00 (UTC 0) - 4:00 (UTC 5)
Today: Linked in files were parsed, but got (ProtocolError, MaxRetryError) for many companies and failed on statistics.