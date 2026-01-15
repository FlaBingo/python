# Object Types / Data Types

- Number : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- String : 'spam', "Bob's", b'a/x01c', u'sp/xc4m'
- List : [1, [2, 'three'], 4.5], list(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
- Dict : {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

- Set : set('abc'), {'a', 'b', 'c'}

- File : open('eggs.txt'), open(r'C:\ham.bin', 'wb')

- Boolean : True, False
- None : None
- Functions, modules, classes

- Advance : Decorators, Generators, Iterators, MetaProgramming


### Other Topics

```
>>> import random
>>> random.random()
0.8739232625319716
>>>
>>> random.choice([1, 2, 3, 4, 5])
3   
>>> random.choice([1, 2, 3, 4, 5])
1   
```

```
>>> username = "chaiaurcode"
>>> username[-1]
'e'
>>> username[1:3]
'ha'
```

```
>>> mylist = [123, "chai", 3.14]
>>> mylist
[123, 'chai', 3.14]
>>> len(mylist)
3
>>> mylist[0]
123
>>> mylist[-1]
3.14
>>> mylist[1:2]
['chai']
```

```
>>> myD = {'one': 'lemon', 'two': 'ginger', 'comic': 'naagraj'}
>>> myD
{'one': 'lemon', 'two': 'ginger', 'comic': 'naagraj'}
>>> myD['comic']
'naagraj'
```


### Difference between repr(), str(), print() methods


1. repr() (Representation):
- It provides the "official" string representation of an object.
- It is mainly used for debugging and logging because it preserves precise details, such as escape characters (\n) or object types.
- For example, repr("hello") returns ' "hello" ' (including quotes), while repr(datetime.now()) returns the full constructor code.

2. str() (String)
- It returns an "informal" or user-friendly string representation.
- It is meant for displaying information clearly to an end-user, often omitting technical details to improve readability.
- If a class does not define its own __str__ method, it will automatically fall back to using the __repr__ implementation.

3. print() (Console Output)
- This is a function that outputs data to the standard output device (usually your console).
- It does not return a string; instead, it triggers the display of one.
- Internally, it calls str() on any object passed to it before printing, favoring human-readability by default. 