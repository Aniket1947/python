def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)

num=int(input("Enter the Number:"))
print(f"The factorial of {num} is {factorial(num)}.")