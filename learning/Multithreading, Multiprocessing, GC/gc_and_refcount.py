import gc


a = 12 # 1
b = 23 # 2


# del(a)
for i in range(10): # i = 
    print(i)

print(i)


def a():
    c = 33
    return c
    # del(c)

a()
print(dir(a))

a = [] # 
a.append(a) # [[]]

# end of the program
# gen 1 []


# Three generation cycle is applied for object that create a reference cycle and can not be cleaned by garbage collector
def create_cycle():
 
    # create a list x
    a = [ ]
 
    # A reference cycle is created
    # here as x contains reference to
    # to self.
    a.append(a)
  
create_cycle()

x = []
x.append(1)
x.append(2)
 
# delete the list from memory or
# assigning object x to None(Null)
del x
import sys 
# print(sys.getcheckinterval(x))


# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector
# as 0 object
print("Garbage collector: collected", "%d objects." % collected)

i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = {}
    x[i+1] = x
    print(x)

# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))
 
print("Creating cycles...")
for i in range(10):
    create_cycle()
 
collected = gc.collect()
 
print("Garbage collector: collected %d objects." % (collected))

# get the current collection
# thresholds as a tuple
a = []
a = []
a.append(a)
print("Garbage collection thresholds:", gc.get_threshold())
print("Garbage collection thresholds:", gc.get_count())
# 
