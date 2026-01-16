# Strings

- enclosed in single, double, and multi double quotes
  - 'str', "str", """ str """


```
>>> chai = 'masala chai'
>>> first_char = chai[0]
>>> print(first_char)
m   
>>> chai
'masala chai'
>>> slice_chai = chai[0:6] 
>>> slice_chai
'masala'
>>> chai
'masala chai'


>>> chai[0].upper() + chai[1:6] 
'Masala'
```


```
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]     # 2 for skipping the string
'0246'
>>> num_list[0:7:3]     # 3 for skipping the string
'036'
```


```
# strip method
>>> chai = "     Masala Chai   "
>>> chai
'     Masala Chai   '
>>> print(chai.strip()) 
Masala Chai
```



```
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon", "Ginger"))  # case-sensitive
Ginger Chai
```


```
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split())   # split by space -> split(" ")
['Lemon,', 'Ginger,', 'Masala,', 'Mint']

>>> print(chai.split(", ")) 
['Lemon', 'Ginger', 'Masala', 'Mint']
```


```
>>> chai = "Masala Chai"
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai"))
-1    # not found
```



```
>>> chai = "Masala Chai Chai Chai"
>>> print(chai.count("Chai"))
3
```



```
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
```



```
>>> chai_variety = ["Lemon", "Masala", "Ginger"]    
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety)) 
LemonMasalaGinger
>>> print(" ".join(chai_variety)) 
Lemon Masala Ginger
>>> print("-".join(chai_variety)) 
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety)) 
Lemon, Masala, Ginger
```



```
>>> chai = "Masala Chai"
>>> print(len(chai))
11
>>> for letter in chai:
...     print(letter)
... 
M
a
s
a
l
a

C
h
a
i
```



```
>>> chai = "He said, "Masala chai is awesome" "
  File "<stdin>", line 1
    chai = "He said, "Masala chai is awesome" "
                      ^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Is this intended to be part of the string?
>>> chai = "He said, \"Masala chai is awesome\" " 
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala/nChai"
>>> chai
'Masala/nChai'
>>> print(chai) 
Masala/nChai
>>> chai = "Masala\nChai" 
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nChai"    # r stands for raw
>>> print(chai)
Masala\nChai
>>> chai = r"c:\user\pwd\user"
>>> print(chai)
c:\user\pwd\user
>>> chai = r"c:\user\pwd\user\" 
  File "<stdin>", line 1
    chai = r"c:\user\pwd\user\"   # 👉\ at the end results error
           ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
```


```
>>> chai = "Masala Chai"
>>> print("Masala" in chai)
True
>>> print("Masalaa" in chai) 
False
```