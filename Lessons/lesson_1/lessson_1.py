"""
  mutable: list, dict, set
  immutable: all else

  difference between is and id
  what is id()
  id() - is a reference to and an object ID in memory: https://www.geeksforgeeks.org/difference-operator-python/
  reference count
  -255 to 255 is cached so that when we compare values within this range we get True

"""
a = 1
a = 2
l = [1]
l[0] = 2
if a:
  pass

a == a

id(a) # указатель на место в памяти
a = 1
b = 1
print(a is b, id(a), id(b))
print(None == None) # singletone
print(1 + True) # base class int and that's why we can accomplish simple operations on them

print("state", a and b) # False 

a = 1
b = 2.4
c = 1j
print(dir(2))

print("radd", b.__radd__(2)) # 2 + (-1) почитать
s = "dsadasdsa dsadas"
s.strip()
print(s.islower())

print("chr", chr(1))
print(ord("A"))
print("dsad".join("dsadsa"))
"{0} {1}".format(2, 3)
print(f"{23+23:d}")

# list
l = [1,2,3,4, 2, 3, 2, -1, -1, -1]
max_repeat = l[0]
for i in l:
  a = l.count(i)
  if max_repeat < a:
    max_repeat = a

a = l.pop()
print(a)

l.sort()
print(l.count(3))

# dict
# hash - unique value which must be immutable. 
# key: int | str | tuple - immutable object
b = {
  1: [2,3,4],
  1: [2],
}
b["A"] = 123

# tuple
t = (2,3,4,5,6)
print( (2, 100) > (2, 200) )

a, b, *_ = t
print(a, b, _)

_ # saves last value in python interpreter

# set
s = set({1,3,7,0})
s2 = set({2,3,4,5})
print(s)

# immutable set
frozenset()
