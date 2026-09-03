# Quiz 1
# def decorator(func):
#     def wrapper():
#         print("Function is being called")
#         func()
#     return wrapper


# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()

######################################################################################################################

# Quiz 2
# from time import time
# def timer(func):
#     def wrapper(n):
#         t1=time()
#         func(n)
#         result=func(n)
#         t2=time()
#         print(t2-t1)
#         return result
#     return wrapper



# @timer
# def sum_1m(n):
#     sum=0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# a=(sum_1m(1000000))
# print(a)

######################################################################################################################

# Quiz 3

# class employee:
#     def __init__(self,salary):
#         self._salary=salary
    
#     @property
#     def get_salary(self):
#         return self._salary
    
#     @get_salary.setter
#     def get_salary(self,value):
#         if value > 0:
#             self._salary=value
#         else:
#             print("Don't put negative value.")
        
# e=employee(34000)
# e.get_salary=-3
# print(e.get_salary)

######################################################################################################################

# Quiz 4

class Mathutils:
    company="wipro"
    def __init__(self,name,company):
        self.name=name
        self.company=company

    @staticmethod
    def addition(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print(f"This is utility class for math operations and the company name is {cls.company}")

print(Mathutils.addition(2,38))
(Mathutils.description())

######################################################################################################################
# Quiz 5
# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def __str__(self):
#         print(f"{self.title} by {self.author}")
    
#     def __len__(self):
#         return len(self.title) 

# b1=book("100 days of coding challenge","Aniket")
# b2=book("Python for beginners","Aniket")
# b1.__str__()
# print(b1.__len__())
# b2.__str__()
# print(b2.__len__())

######################################################################################################################
        
# Quiz 6
# class negativeNumberError():
#     pass
# try:
    
#     num1=int(input("Enter the first Number:"))
#     num2=int(input("Enter the second Number:"))
#     if num1 < 0 or num2 <0:
#         raise negativeNumberError("You are enterimg negative number.Don't do this!")

#     result= num1/num2
#     print(result)
# except ValueError as e:
#     print(f"Error: {e}")  

# except ZeroDivisionError as e:
#     print(f"Error: {e}") 


######################################################################################################################

# Quiz 7
# Quiz 7.1
# l=[1,2,3,4,5]

# new_list=list(map(lambda x:x**3,l))
# print(new_list)

# Quiz 7.2

# l=[10,11,12,13,14,15]
# new_list=list(filter(lambda x:x%2==0,l))
# print(new_list)

# Quiz 7.3
# from functools import reduce
# l=[1,2,3,4]
# l=reduce(lambda x,y:x+y,l)
# print(l)

#####################################################################################################################


# Quiz 8.1

# while (text:=input("Enter the value:")) != "quit":
#     print(text)

# Quiz 8.2

# words=["python","rock","ai"]

# length=[n for w in words if( n := len(w))>=4]
# print(length)

#####################################################################################################################


# Quiz 9.1
# def sum(*args):
#     sum=0
#     for i in args:
#         # print(i)
#         sum += i
#     return sum

# print(sum(2,3,4))


# Quiz 9.2

# def print_details(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#     for item in kwargs.keys():
#         print(kwargs[item])

# print_details(name="Alice",age=25,city="Delhi")
#####################################################################################################################
 
# Bonus Challenge
# def combine(func):
#     def wrapper(*args, **kwargs):
#         sum=0
#         for item in args:
#             sum += item
#         print(sum)
#         for key,value in kwargs.items():
#             print(f"{key}:{value}")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper

# @combine
# def show_data(*args, **kwargs):
#     print("This is orginal function.")

# show_data(2,3,4,Aniket=99,Sameer=89)
########################################################################################################
# def combine(func):
#     def wrapeer(*args, **kwargs):
#         print(f"Before calling:{func.__name__}")
#         print(f"Positional args:{args}")
#         print(f"Positional kwargs:{kwargs}")

#         result=func(*args,**kwargs)
#         print(f"After calling {func.__name__}")
#         print(f"Result:{result}")
#         return result
#     return wrapeer

# @combine
# def add(a, b, c):
#     return a + b + c
# add(2, 3, 4)

# @combine
# def greet(name,age):
#     print(f"Hello {name},you are {age} years old.")
# greet("Aniket",23)

# @combine
# def info(id, name, city="Unknown"):
#     return f"ID: {id}, Name: {name}, City: {city}"

# info(101, "Aniket", city="Mumbai")



#####################################################################################################################


#  Bonus challenge 2
# class vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,other):
#         print(f"{self.x}+{other.x},{self.y}+{other.y}")
#         return f" {self.x +other.x}   {self.y + other.y}"
    
# v1=vector(2,3)
# v2=vector(4,5)
# v3=v1+v2
# print(v3)

#Bonus challenge 3

# class negativeNumberError:
#     pass

# while True:
#     try:
#         num1=int(input("Enter thr first value:"))
#         num2=int(input("Enter the second value"))
#         if num1 < 0 or num2 < 0:
#             raise negativeNumberError("Negative number not allowed!")
#         result=num1/num2
#         print(result)
#     except ZeroDivisionError as e:
#         print(f"Error:{e}")
#     except ValueError as e:
#         print(f"Error:{e}")

    



    





#####################################################################################################################





#####################################################################################################################





#####################################################################################################################
