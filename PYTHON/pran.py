# ask = input("which operation you want to do : ")
# a = int(input("enter first number : "))
# b= int(input("enter second number : "))

# match ask:
#     case "addition":
#         print(a + b)
#     case "subtraction":
#         print(a-b)
#     case "multiply":
#         print(a*b)
#     case "divide":
#         print(a/b)
#     case _:
#         print("there's an error")



# def generate_fibonacci(n):
#     fibonacci_series = []
#     if n <= 0:
#         return fibonacci_series
#     elif n == 1:
#         fibonacci_series.append(0)
#         return fibonacci_series
#     elif n == 2:
#         fibonacci_series.extend([0, 1])
#         return fibonacci_series
#     else:
#         fibonacci_series.extend([0, 1])
#         for i in range(2, n):
#             next_num = fibonacci_series[-1] + fibonacci_series[-2]
#             fibonacci_series.append(next_num)
#         return fibonacci_series

# # Example usage:
# n = int(input("Enter the number of Fibonacci numbers to generate: "))
# fib_series = generate_fibonacci(n)
# print("Fibonacci series of", n, "numbers:", fib_series)



def evenOdd(x):
  if x % 2 == 0:
    print("even")
  else:
    print("odd")

evenOdd(50)







