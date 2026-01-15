

## mutable and immutable: In-memory working

### mutable & immutable data types

1. Mutable(changable)
- list
- set
- dictionary
- bytearray
- array

2. Immutable(unchange-able)
- integers
- floating-point numbers
- boolean
- strings
- tuples
- frozen set
- bytes

```
Note: Almost everything in python is an Object
```

```
>>> x = 10
>>> y = x
>>> x
10  
>>> y
10  
>>> x = 15
>>> y
10  
```
- in the above code, we assign 10 to variable x and directly assign x to variable y
- that means y is also 10, but if we change the x to 15
- since integer is immutable, now the x is pointing to 15 but y is still pointing to 10



### Example
```
>>> a = [1, 2, 3]
>>> b = a
>>> a == b
True    # true cuz same value
>>> a is b
True    # true cuz same reference
>>> c = [1, 2, 3]
>>> a == c
True    # true cuz same value
>>> a is c
False   # false cuz different reference
```