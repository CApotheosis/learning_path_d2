## An `interpreter` is a kind of program that executes other programs

### When you write a Python program, the Python interpreter reads your program and carries out the instructions it contains. In effect, the interpreter is a layer of software logic between your code and the computer hardware on your machine.

### After writing python code and sending it into execution two steps are carried out:
- ### compilation into byte code
- ### routing into virtual machine 

<br>

## Byte code compilation
### Simple said, it's process of converting source code into byte representation for faster execution. Before the version 3.2 there will be corresponding files with .pyc (under __pycache__ directory) extension to run python program. This is a byte code representation of your source code.

<br>

### If Python cannot write the byte code files to the machine, the program will still work - the byte code is generated in memory and simply discarded on program exit. However, .pyc files speed startup time and it's good to have them for large programs. Python can execute .pyc code even if source code is absent. (Frozen binaries)

<br>

### Finally, keep in mind that byte code is saved in files only for files that are imported, not for the top-level files of a program that are only run as scripts.

<br>

## The Python Virtual Machine (PVM)
### The `PVM` is just a big code loop that iterates through your byte code instructions, one by one, to carry out their operations. The PVM is the runtime engine of Python; it’s always present as part of the Python system, and it’s the component that truly runs your scripts. Technically, it’s just the last step of what is called the “Python interpreter.”

## Development implications
### In Python, there's no distinction between development and execution environments. The systems compile and execution of source is one and same. This means there'is no need to have or compile th entire system's code. 


## `Inheritance` is a way of creating a new class for using details of an existing class without modifying it. 
## `Encapsulation`: Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
## `Polymorphism`: is an ability (in OOP) to use a common interface for multiple forms (data types).

Key Points to Remember:
- Object-Oriented Programming makes the program easy to understand as well as efficient.
- Since the class is sharable, the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects, so programmers can write efficient code.

Key Takeaways
- Instance methods need a class instance and can access the instance through self.
- Class methods don’t need a class instance. They can’t access the instance (self) but they have access to the class itself via cls.
- Static methods don’t have access to cls or self. They work like regular functions but belong to the class’s namespace.
- Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.


Memory allocation in C:
- `static`: memory allocation, where memory requirements are calculated
at compile time and allocated by the executable when it starts
- `automatic`: memory allocation, where memory requirements for a
scope (e.g., function) are allocated within the call stack when a
frame is entered and freed once the frame is terminated
- `dynamic`: memory is preserved for compilation time for dynamic data like user input

Operating Systems reserve a section of the system memory for dynamically
allocation to processes. This section of memory is called a heap.


Python heavily relies on Dynamic memory allocation to handle all dynamic creation of objeccts. To free the memory python uses the garbage collection and reference counting algorithms.

CPython comes with three dynamic memory allocation domains:
1. `Raw Domain` - Used for allocation from the system heap. Used
for large, or non-object related memory allocation
2. `Object Domain` - Used for allocation of all Python Object-related
memory allocation
3. `PyMem Domain` - The same as PYMEM_DOMAIN_OBJ, exists for legacy
API purposes

CPython uses two memory allocators:
1. The Operating System allocator (malloc) for the Raw memory domain
2. The CPython allocator (pymalloc) for the PyMem and Object
Memory domains

The largest group of memory is an arena. CPython creates arenas of
256KB to align with the system page size. A system page boundary is
a fixed-length contiguous chunk of memory.

Arenas: CPython creates arenas of 256KB to align with the system page size.
Inside Arenas resides Pools of 16 bytes, so there are 32 classes (for 64-bit systens). Pools are all 4096 bytes (4KB), so there are always 64 pools in an
arena.

A register of the pools within an arena is called a pool table. A pool table is a headed, circular, doubly-linked list of partially-used pools.

Within a pool, memory is allocated into blocks.

```python
import sys
# get the number of blocks in use for each of the class size pools.
sys._debugmallocstats() 
```

`Reference Counting`

Py_INCREF() and Py_DECREF(). These macros are the primary API for incrementing and decrementing references to Python objects.
Inside Py_DECREF(), when the reference counter (ob_refcnt) value becomes 0, the object destructor is called via _Py_Dealloc(op), and any allocated memory is freed.



- Not all object would be deleted after variable declaration
- chaching: -6 ... 256, short strings; () - empty tuple
- Potential Race Condition

Цилические ссылки 
```python
x = []
x.append(x)
del x
```
GC module - garbage collector
- handles cyclic references
- uses generation approach to optimize memory scan time
- import gc to manage it
- it's not a silver bullet
- includes crutches

gc запускается когда количество созданных за вычетом удаленных объектов превышает 700 
просматривает все объекты в модуле и пытается их удалить ссылку(рвет ссылке - делает decref На объект) на объект чтобы убрать циклическую ссылку, если не получилось удалить объект в первой итерации, то запускается вторая итерация и третья, основанная на на поколенческой передаче/подхорду 

Поколений 3
0   1   2
700 10  10
На каждые 10 сканов первого поколения происходит скан второго поколения, на каждые 10 запусков 2 поколения происходит один скан 3-его. Если объект не умер после последнего скана(поколения), в конце будет проверяться до тех пор пока не удалиться.  

Удаляет ли gc объекты? - вопрос на завал. Это открытый вопрос в котором любой ответ не правильный.

gc.freeze() 

weakrefs
- a weak reference to an object is not enough to keep the object alive
- used for caches and mapping implementation for large objects
- bot all objects can be weakly referenced (it doesn't work with dicts but have WEakKeyDictioney and WeakValueDictionary classes)
- doesn't work with __slots__ bt default
- Has finalize() function that sometimes can be better that __del__:
    - doen't need full state of the object
    - can be registered for third party objects
    - has potential issues if called on program exit
