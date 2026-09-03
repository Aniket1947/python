n=int(input("Enter the number:"))

if n==1:
    print("Its is not a prime number.")

if n > 1:
    for i in range (2,n):
        if n %  i == 0:
            print("Not a prime Number")
            break
    else:
        print("This is prime number.")