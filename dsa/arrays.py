from array import *

val = array('i', [1,2,3,4,5,6])

# print(val)

# for i in range(0, len(val)):
#   print(val[i], end=", ")

# print("\n")
# val.insert(2, 10)

# add an element at the specific index
# val.append(100)
# replace
# val[0] = 10000

# for i in val:
#   print(i, end=" ")


copyArray = array(val.typecode, (x*2 for x in val))

copyArray.pop(3)

for i in copyArray:
  print(i, end=" ")