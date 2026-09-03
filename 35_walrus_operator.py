#Simple example
# x=34
# print(x)
# print(x:=45) #Here the walrus operator is used.Throw walrus operator we can directly change the variable within a expression. i.e x:=45

##################################################################################################

#Example with def function.

# def add(num1,num2):
#     result=num1+num2
#     return result

# num1=int(input("Enter a first Number:"))
# num2=int(input("Enter a second number:"))

# if a:=add(num1,num2):
#     print(a)

##################################################################################################

# l=[1,2,3,4,5]

# while (a:= len(l)) > 0:
#     print(l.pop(),end=" ")

##################################################################################################

names=["Aniket","Sonu","Sameer","Aakash"]
while True:
    if (name:=input("Enter the name or q to quite:")) in names:
        print(f"Hello,{name}")
    elif name =="q":
        break
    else:
        print("Name not Found.")
