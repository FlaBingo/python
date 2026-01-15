your code --> Byte code (not machine code) --> Python Virtual Machine

1. Compile to Byte Code (low lever and platform independent)

--> Byte code runs faster
.pyc --> compiled python (frozen Binaries)

__ pycache__
Source Change and python version

hello.cpython-314.pyc
--> Works only for imported files
--> not for top level files


_________________

Python Virtual Machine (PVM)
--> Code loop to iterate byte code
--> Run time Engine
--> Also known as python interpreter
____________________

Byte Code is Not machine Code 
--> python specific interpretation
--> cpython (standard implementation), jython, IronPython, Stackless, PyPy






_____________________


from importlib import reload
reload(hello: <which is a file name>)