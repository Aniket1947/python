# Quiz 1
# num=int(input("Enter the number:"))

# if(num < 0):
#     print(f"Number is negative and the number is {num}")
# elif(num == 0):
#     print("You have enter number 0")
# else:
#     print(f"Number is postive and the number is {num}")

    
    
# Quiz 2
# age=int(input("Enter your age:"))
# if (age >18):
#     print("You can vote")
# else:
#     print("You cannot vote")

# Quiz 3
# num=int(input("Enter the Number:"))
# if(num % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# Quiz 4
n=input("Enter the Number between 1 to 7:")

match n:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")


# Quiz 5
# num1=int(input("Enter the first Number:"))
# num2=int(input("Enter the seconde Number:"))
# opr=input("+ for addition,- for Subtraction,* for mutliplication, / for divide:")
# match opr:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1-num2)
#     case "*":
#         print(num1*num2)
#     case "/":
#         print(num1/num2)
#     case _:
#         print("Invalid Input")

# Quiz 6
# for i in range(1,11):
#     print(i)

# Quiz 7
# table=int(input("Enter the table you want:"))
# for i in range(1,11):
#     print(f"{table} X {i} = {table*i}")

# Quiz 8
# sum=0
# for i in range(0,101):
#     sum +=i
# print(sum)

# Quiz 9
# for i in range(1,5):
#     print("*"*i)

# Quiz 10
# i=1
# while(i<101):
#     print(i)
#     i+=1

# Quiz 11
# password="Y2K123"
# entered_pass=input("Enter Password")

# while (entered_pass != password):
#     entered_pass=input("Wrong Password! Try again and enter password")

# print("Sucessfully Login")

# Quiz 12
# number=9876543321
# print(int(str(number)[::-1]))  

#Quiz 13
# for i in range(1,11):
#     if(i==7):
#         break
#     print(i) 

# Quiz 14
# for i in range(1,11):
#     if(i==7):
#         continue
#     print(i) 

# i=1
# while(i<=10):
#     if(i==7):
#         i+=1
#         continue
#     print(i)
#     i+=1

# Quiz 15


# for i in range(1,6):
#     match i:
#         case 1:
#             print("One")
#         case 2:
#             print("Two")
#         case 3:
#             pass
#         case 4:
#             print("Four")
#         case 5:
#             print("Five")