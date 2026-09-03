

# while True:
#     try:
#         num1=int(input("Enter a first Number:"))
#         num2=int(input("Enter a second Number:"))
#         result=num1/num2
#         print(result)
#     except Exception as e:
#         print(f"Error:{e}")

#     finally:
#         print("This finally block will always get excuted no matter try block get error or not")

def divide(a,b):
    try:
        result=a/b
        print(result)
        return result
    except Exception as e:
        print(e)
        return e
    finally:
        print("This code always excuted")
    print("This print code will not excuted")


num1=int(input("Enter the first Number:"))
num2=int(input("Enter the second Number:"))
(divide(num1,num2))