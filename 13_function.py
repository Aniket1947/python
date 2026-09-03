# Simple Function with argument
# def sum(a,b):
#     return a+b

# print(sum(2,4))

###################################################################################################

# Simple function with default argument
# def mul(a=4,b=2):
#     return a*b
# print(mul())

###################################################################################################

# Simple function with default argument but it will get ignored if we pass the argument in this example we are passing 3and 6
# def mul(a=4,b=2):
#     return a*b
# print(mul(3,6))

####################################################################################################

# Simple function with keyword argument in this we provide argument with argument name.
# def add(a,b):
#     print(a+b)

# add(b=4,a=6)

###################################################################################################
# Simple function with required argument,here and 3 and 5 are required argument because if we don't pass it will throw an error:sum() missing 2 required positional arguments: 'a' and 'b'
# def sum(a,b):
#     print(a+b)

# sum(3,5)

# Keyword Arbitary Argument

# def sum(*numbers):
#     print(numbers)
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     print(f"The sum of numbers is {sum}")
#     print(f"The average of numbers is {sum/len(numbers)}")

# sum(3,4,5)

def keyValue(**name):
    print(type(name))
    for value in name.keys(): 
        print(f"Hello {value}",end=",")

keyValue(name1="Aniket",name2="Sameer",name3="Sonu")