## An `interpreter` is a kind of program that executes other programs

### When you write a Python program, the Python interpreter reads your program and carries out the instructions it contains. In effect, the interpreter is a layer of software logic between your code and the computer hardware on your machine.

### AFter writing python code and sending it into execution two steps are carries out:
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
### In Python, there's no distinction between development and execution environments. The systems compile and execution of source is one and same. This means there'is no need to to have or compile th entire system's code. 