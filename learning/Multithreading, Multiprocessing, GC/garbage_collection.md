## Python objects have three things: Type, value, and reference count. When we assign a name to a variable, its type is automatically detected by Python as we mentioned above.

## Garbage collection is to release memory when the object is no longer in use. This system destroys the unused object and reuses its memory slot for new objects. This can be interpreted as a recycling system in computers.

### `id()` function to see object id on memory and this can compared by `is` operator

### When reference count increases:
```
# Reference count = 1
numbers = [1, 2, 3]
# Reference count = 2
more_numbers = numbers

# It will also increase if you pass the object as an argument:
total = sum(numbers)

# Object in a list
matrix = [numbers, numbers, numbers]
```
### ref count can be vieved with sys modules `sys.getrefcount(numbers)`, but it increases ref count by 1.

## Pros and Cons of reference counting:

# Reference cycle is a problem in reference count
```python
a = [] # 
a.append(a) # 
print(a) # [[]] - reference count is not zero, this means object can't be deleted
```
## Solution
### *Generational garbage collection* is a type of trace-based garbage collection.
### Python keeps track of every object in memory. 3 lists are created when a program is run. Generation 0, 1, and 2 lists.

