while True:
    try:
        num1=int(input("Enter a first Number:"))
        num2=int(input("Enter a Second Number:"))

        result=num1/num2
        print(result)

    except ValueError:
        print("Enter only number:")
    
    except ZeroDivisionError:
        print("can't divide by zero")

    except Exception as e:
        print(f"Error: {e}")
     