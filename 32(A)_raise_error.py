num=int(input("Enter the Number between 5 to 10."))

if num <5 or num >10:
    raise ValueError("Enter a number between 5 to 10.")
else:
    print(num)
