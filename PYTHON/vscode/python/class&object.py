# class Student:
#     def __init__(self):
#         self.name = "vishnu"
#         self.age = 20
#         self.marks = 900
#     def talk(self):
#         print('Hi, I am', self.name)
#         print('My age is', self.age)
#         print('My marks age', self.marks)
# s1 = Student()
# s1.talk()


# class Father:
#     def __init__(self, property) -> None:
#         self.property = property
#     def display_property(self):
#         print("Father's property =", self.property) 
        
# class Son(Father):
#     def __init__(self, property1 = 0, property =0):
#         super().__init__(property)
#         self.property1 = property1
#     def display_property(self):
#         print("Total property of child = ", self.property1 + self.property)
# s = Son(200000, 800000)
# s.display_property()


# class Square:
#     def __init__(self, x) -> None:  
#         self.x =x
#     def area(self):
#         return "Area of square =", self.x*self.x
# class Rectangle(Square):
#     def __init__(self, x, y) -> None:
#         super().__init__(x)
#         self.y =y
#     def area(self):
#         return "Area of this rectangle =", self.x * self.y

# square = Rectangle(6,10)
# print(square.area())


# from emp import Emp
# import pickle
# f = open("empdetail.txt", "wb")
# empno = int(input("Enter number of empoyees: "))
# for i in range(empno):
#     id = int(input("Emplyee ID: "))
#     name = input("Employee name: ")
#     sal = float(input("Employee salary: "))
#     e = Emp(id,name,sal)
#     pickle.dump(e, f)
# f.close()

# f1 = open("empdetail.txt", "rb")
# print("Employees details: ")
# while True:
#     try:
#         obj = pickle.load(f1)
#         obj.display()
#     except EOFError:
#         print("End of file reached...")
#         break
# f1.close()


# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# # Input two numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# # Calculate GCD
# result = gcd(num1, num2)

# # Output the result
# print(f"The Greatest Common Divisor of {num1} and {num2} is {result}")



# class Programmer:
#     def __init__(self, name, id  , sal) -> None:
#         self.name = name
#         self.id = id
#         self.sal = sal
#     def display_info(self):
#         print(f"The name of the programmer is {self.name} with ID:{self.id} and Salary package of {self.sal}")
    

# p = Programmer("satyam", 100, 1000000)
# p.display_info()

# class Calc:
    
#     # a = 5
#     # b = 6
#     def show(self,a , b):
#         pass
#         # print(a)
#         # print(b)
#         # print(self.a)
#         # print(self.b)
#     def __init__(self, x) -> None:
#         self.x = x
#     def sq(self):
#         return self.x*self.x
#     def cb(self):
#         print(self.x*self.x*self.x)
#     def sqrt():
#         print("Let me seee.....")
# n = 4
# c = Calc(n)
# print(c.show(2, 3))
# # print(c.cb())

# def write():
#     try:
#         print("Hello there")
#         return "My name is something"
#     finally:
#         print("Meri koi aukat hai ki nhi")
#         print("Haa, Meri kuchh to aukat hai")
#         return ("Thanks you, finally")

# print(write())

# ask = int(input("Enter the number to generate table: "))
# table = [ask*i for i in range(1, 11)]
# print(table)

# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(a/b)
# except ZeroDivisionError as z:
#     print("infinite")
# else:
#     print("It worked")

def div5(n):
    if (n % 5 == 0):
        return True
    return False

list1 = [1,2,3,4,5,6,7,8,9,10]
s = list(filter(div5, list1))
print(s)