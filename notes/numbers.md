## Numbers

- ensure the data types are same while operations
  - 40 + 2.23 --> bad practice
  - 40 + int(2.23) --> good practice
  - float(40) + 2.23 --> good practice


```
>>> x, y, z
(2, 3, 4)
>>> x < y < z   # short hand version
True
>>> x < y and y < z
True
```



```
>>> 1 == 2 < 3    # equivalent to 1 == 2 and 2 < 3
>>> False
```


```
>>> import math        
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
```


```
>>> math.trunc(3.5)   # return an int closer to 0
3
>>> math.trunc(-3.5)
-3
```


### Complex numbers
```
>>> 2+1j
(2+1j)
>>> (2+1j) * 3
(6+3j)
>>> (2+1j) + 3 
(5+1j)
>>> (2+1j) + 3j
(2+4j)
```



```
>>> #octal
>>> 0o20
16
>>> # hexal
>>> 0xff
255
>>> # binary
>>> 0b1000
8
>>> # methods
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'

>>> int(64)
64
>>> int('64', 8)
52
>>> int('100', 8)
64
>>> int('40', 16)
64
>>> int('1000000', 2)
64
```


### bitwise (idk)

```
>>> x=1
>>> x << 2
4
>>> x | 2 
3
```


### the random package

```
>>> import random
>>> random.random()
0.9082734908127349
>>> random.randint(1, 100)
89

>>> l1 = ['lemon', 'masala', 'ginger', 'mint']
>>> random.choice(l1)
'ginger'
>>> random.shuffle(l1)
>>> l1
['masala', 'ginger', 'mint', 'lemon']
```

### Unexpected behaviour

```
>>> 0.1 + 0.1 + 0.4
0.6000000000000001
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> (0.1 + 0.1 + 0.1) - 0.3 
5.551115123125783e-17
```

```
>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')
```

```
>>> from fractions import Fraction
>>> myFra = Fraction(2, 7)
>>> myFra
Fraction(2, 7)
>>>
>>> float(myFra)
0.2857142857142857
>>> 2/7
0.2857142857142857
```

### Sets -> {1. 2, ...}

```
>>> setone = {1, 2, 3, 4}
>>> setone & {1, 3}
{1, 3}
>>> setone | {1, 3} 
{1, 2, 3, 4}
>>> setone | {1, 3, 7} 
{1, 2, 3, 4, 7}
```

```
>>> setone
{1, 2, 3, 4}
>>> setone - {1, 2, 3, 4}
set()     # we don't get empty {} cuz this👉 {} is dictionary
>>> type({})
<class 'dict'>
```


### Boolean

```
>>> type(True)
<class 'bool'>
>>> True == 1
True
>>> False == 0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with literal. Did you mean "=="?
False
>>> True + 4
5
```