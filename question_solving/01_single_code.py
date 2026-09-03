def sum(n):
    if n<=1:
        return n
    else:
       return n + sum(n-1)

num=int(input("Enter the number:"))
if num <=1:
    print("Enter the number greater than 1")
else:
    print(f"The sum of {num} natural number is {sum(num)}.")  