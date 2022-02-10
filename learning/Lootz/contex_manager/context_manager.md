## Under the hood of with 
```
mgr = (EXPR)
exit = type(mgr).__exit__  # Not calling it yet
value = type(mgr).__enter__(mgr)
exc = True
try:
    try:
        VAR = value  # Only if "as VAR" is present
        BLOCK
    except:
        # The exceptional case is handled here
        exc = False
        if not exit(mgr, *sys.exc_info()):
            raise
        # The exception is swallowed if exit() returns true
finally:
    # The normal and non-local-goto cases are handled here
    if exc:
        exit(mgr, None, None, None)
```


```
# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    # Make sure to close the file after using it
    file.close()
```

### The context manager object results from evaluating the expression after with. In other words, expression must return an object that implements the context management protocol. This protocol consists of two special methods:
1. ### `.__enter__()` is called by the with statement to enter the runtime context.
2. ### `.__exit__()` is called when the execution leaves the with code block.

### Here’s how the with statement proceeds when Python runs into it:
1. ### Call expression to obtain a context manager.
2. ### Store the context manager’s `.__enter__()` and `.__exit__()` methods for later use.
3. ### Call `.__enter__()` on the context manager and bind its return value to target_var if provided.
4. ### Execute the with code block.
5. ### Call `.__exit__()` on the context manager when the with code block finishes.
```
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")
```

### Nested call of `with` statement
```
with A() as a, B() as b:
    pass
```

