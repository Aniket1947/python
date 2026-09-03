# n=int(input("Enter the Number to check wheather the given number is odd and even without using module:"))
# x=int(n/2)
# if n == x*2:
#     print(f"{n} is a even Number.")
# else:
#     print(f"{n} is a odd number.")


n=int(input("Enter the Number to check wheather the given number is odd and even without using module:"))
while n>1:
    n=n-2

if n == 0:
    print("Even Number.")
else:
    print("Odd Number.")