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

## Coding Class-Based Context Managers
- ### `.__enter__(self)` This method handles the setup logic and is called when entering a new with context. Its return value is bound to the with target variable.

- ### `.__exit__(self, exc_type, exc_value, exc_tb)` This method handles the teardown logic and is called when the flow of execution leaves the with context. If an exception occurs, then exc_type, exc_value, and exc_tb hold the exception type, value, and traceback information, respectively.

### Class based context manager
```python
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")


with HelloContextManager() as hello:
    print(hello)
```
