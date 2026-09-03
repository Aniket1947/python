# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n +  factorial(n-1) 

# x=factorial(5)
# print(x)

# sum=0
# def sum(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return n + sum(n-1)

# num=int(input("Enter a Number:"))
# x=sum(num)
# print(x)


# def sum_list(numbers):
#    if not numbers:
#       return 0
#    else:
#       return numbers[0] + sum_list(numbers[1:])
    
# x=sum_list([1,2,3,4,5,6])
# print(x)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(7))