# Quiz 1
# def greet():
#     print("Hello,Python learner!")

# greet()

# Quiz 2
# def square(num):
#     result=num*num
#     return result

# n=int(input("Enter the number:"))
# print(square(n))

# Quiz 3
# def full_name(first,last):
#     text=(" ".join([first,last]))
#     return text

# text=full_name("Aniket","Varma")
# print(text)
# print(type(text))

# Quiz 4
# def calculate_area(length,width=10):
#     area_of_rectangle=length*width
#     return area_of_rectangle

# # Calling function with default parameter
# area=calculate_area(4)
# print(area)

# # Calling function without default parameter
# area=calculate_area(4,4)
# print(area)

# Quiz 5
# add = lambda x,y : x+y
# print(add(4,4))

# Quiz 6
# l=[1,2,3,4,5]
# square=list(map(lambda x:x*x,l))
# print(square)

# Quiz 7
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else: 
#         return n * fac(n-1)

# num=int(input("Enter the Number:"))
# print(fac(num))

# Quiz 8
# def sum_of_digits(n):
#     if n ==0:
#         return n
#     else:
#         return n % 10 + sum_of_digits(n // 10)

# n=int(input("Enter the Number:"))
# print(sum_of_digits(n))


# Quiz  9
# import math

# print(math.sqrt(144))
# print(math.sin(math.radians(90)))

# Quiz 10
# import requests

# a=requests.get("https://api.github.com")
# print(a.text)

# Quiz 11

# def increment():
#     counter=0
#     counter += 1
#     print(counter)

# increment()
# increment()
# increment()
# increment()

# Quiz 12
# def multiply(a,b):
#     '''
#     It's take two parameter.
#     multiply a and b and return the value when the function calls.
#     '''
#     return a*b

# x=multiply(2,4)
# help(multiply)
# print(f"The muitiplication of two number is:{x}")

# Quiz 13
# def fib(n):
#     if n==0:
#         return n
#     else:
#         return n + fib(n-1)

# n=int(input("Enter the Number:"))
# f=fib(n)
# print(f)


# Quiz 14
# def safe_divide(a,b):
#     if a != 0 and b != 0:
#         print(a/b)
#     else:
#         print("Cannot divide by Zero if any number is zero.")

# n1=int(input("Enter the Number:"))
# n2=int(input("Enter the Number:"))
# safe_divide(n1,n2)
