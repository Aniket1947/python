# #simple decorator example
# def decorator_function(fuc):
#     def wrapper():
#         print("Some Code is going to excute")
#         fuc()
#         print("Code as been excuted sucessfully")
#     return wrapper


# @decorator_function
# def say_hello():
#     print("Hey We are learning Python")

# say_hello()


##############################################################################################
# from functools import reduce
# def decorator(func):
#     def wrapper(*args):
#         func(*args)
#     return wrapper

# @decorator
# def add_two_number(*args):
#     new=reduce(lambda x,y:x+y,args)
#     print(new)

# @decorator
# def multiplication(a,b):
#     print(f"The multiplication of two is {a*b}")



# (add_two_number(2,3,4))
# ((multiplication(2,3)))

# def decorator(func):
#     def wrapper(*args):
#         print("Proccess is Ongoing...")
#         func(*args)
#         print("Proccess is done!")
#     return wrapper

# @decorator
# def add(*args):
#     new=reduce(lambda x,y:x+y,args)
#     print(new)
    

# @decorator
# def mul(a,b):
#     print(a*b)


# add(2,3,4,5,6)
# mul(2,3)
    

##############################################################################################

# def number_of_times_will_repeat_this_function(n):
#     def decorator(fun):
#         def wrapper(a,b):
#             for i in range(n):
#                     fun(a,b)
#         return wrapper
#     return decorator

# @number_of_times_will_repeat_this_function(7)
# def say_hello(a,b):
#      print(f"Hello {a+b}")
    
# say_hello(6,5)



##############################################################################################
# def number_of_times_code_will_repeat(n):
#     def decorator(func):
#         def wrapper(name):
#             for i in range(n):
#                 func(name)
#         return wrapper
#     return decorator

# @number_of_times_code_will_repeat(2)
# def greet(name):
#     print(f"The name of employee is {name}")

# greet("Aniket")

