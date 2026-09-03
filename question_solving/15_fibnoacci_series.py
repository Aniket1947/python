# def fib(n):
#     if n<0:
#         print("Invalid Input")
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(9))


def fib(n):
   if n <=1:
      return n
   else:
       return fib(n-1) + fib(n-2)

n=int(input("Enter the Number:"))

if n<=0:
    print("Enter positive Number:")
else:
    for i in range(n):
        print(fib(i))
   
