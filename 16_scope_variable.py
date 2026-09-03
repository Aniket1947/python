y=12
def sum(a,b):
    c=a+b
    x=100 # This is local variable and it will access inside the function
    global y #This means that it change global variable but this changes only made after the function call another wise it will it previous value in this it was 12.
    y=11
    print(f"This is local x:{x}") #First it will check x variable inside function if it get x varaiable inside the function then it will print that variable else it will check outside the function 
    return f"The sum of a and b is {c}"

x=10 #This is global variable and it will access every where in the program
print(f"This is global x:{x}")
print(f"This is variable y before function call:{y}")
print(sum(3,4))
print(f"This is variable y after function call:{y}")