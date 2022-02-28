def fib():
    a, b = 0, 1
    while 1: 
       yield b # stops execution and resumes from here on the next call
       a, b = b, a+b

f = fib()
# print(next(f))
# print(next(f))
# print(next(f))


# def f():
#     1/0
#     yield 43

# try:
#     f = f() # Error
#     print(next(f)) 
# except Exception as err:
#     print(err)
# finally:
#     print("works")
#     print(next(f)) # Calls StopIteration error


import sys
nums_squared_lc = [i * 2 for i in range(10000)]
# print(sys.getsizeof(nums_squared_lc)) # byte size
nums_squared_gc = (i ** 2 for i in range(10000))
# print(sys.getsizeof(nums_squared_gc)) # # byte size

# If the list size is less than memory size, it's better to use list comprehension 
import cProfile

# print(cProfile.run('sum([i * 2 for i in range(10000)])')) # Execution time 0.002
# print(cProfile.run('sum((i * 2 for i in range(10000)))')) # Execution time 0.006


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():
    num = 0
    while True:
        print("num =", num)
        if is_palindrome(num):
            print("num2 =", num)
            i = (yield num) # 11
            print("i =", i)
            if i is not None: # i = None
                num = i
        num += 1


# pal_gen = infinite_p


# pal_gen = infinite_palindromes()
# for i in pal_gen:
#     print(i)
#     digits = len(str(i))
#     if digits == 5:
#         pal_gen.throw(ValueError("We don't like large palindromes"))
#     pal_gen.send(10 ** (digits))

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(i)
    digits = len(str(i))
    if digits == 5:
        pal_gen.close() # raises StopIteration
    pal_gen.send(10 ** (digits))
