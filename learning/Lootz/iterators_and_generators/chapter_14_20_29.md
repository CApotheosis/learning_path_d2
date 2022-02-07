# Chapter 14. Iterations and Comprehensions.
```
for loop works on any iterable object.
```
### An object is considered iterable if it is either a physically stored sequence, or an object that produces one result at a time in the context of an iteration tool like a for loop. In a sense, iterable objects include both physical sequences and virtual sequences computed on demand.

<br/>

### For clarity, this book has a very strong preference for using the term iterable to refer to an object that supports the `iter` call, and iterator to refer to an object returned by an iterable on iter that supports the `next(I)` call. Both these calls are defined ahead.

<br/>

### Any object with a `__next__` method to advance to a next result, which raises StopIteration at the end of the series of results, is considered an `iterator` in Python.

### The usage of for loop executes `__next__` on each call to next object in sequence and is memory efficient (runs at C language speed). We can reach same effect with `while`, but it runs through python virtual machie thus with pythin speed.

<br/>

### The alternative to `__next__` method is next() function.

<br/>

### Technically, there is one more piece to the iteration protocol alluded to earlier. When the `for` loop begins, it first obtains an iterator from the iterable object by passing it to the `iter` built-in function; the object returned by iter in turn has the required next method. The iter function internally runs the `__iter__` method, much like next and `__next__`.

<br/>

### File object is its own iterator, thus it doen't require `iter` method call 

<br/>

### Objects types we can use iteration protocol on:
- basic: list, str, tuple, set, map, filter and etc.
- dictionary
- files
- shelves (os path params)
- range()

## List comprehensions
### List comprehension are basically creating new list while appending values returned by for loop inside, but it's almost twice as fast, because their iterations are performed at C language speed inside the interpreter, rather than with manual Python code. Especially for larger data sets, there is often a major performance advantage to using this expression.

### Files are closed autimatically when garbage-collected if still open. Hense, list comprehensions will also automatically close the file when their temporary file object is garbage-collected after the expression runs.

### Interestingly, the iteration protocol is even more pervasive in Python today than the examples so far have demonstrated—essentially everything in Python’s built-in toolset that scans an object from left to right is defined to use the iteration protocol on the subject object

### `map`, `filter` and `zip` are exhausted after iteration of elements and multiple assignments are impossible, but this can be done with `range`.

### Generator objects can't be indexed and we can't access length.
### (i for i in range(100)) is a generator, not a tuple.


# Chapter 20

