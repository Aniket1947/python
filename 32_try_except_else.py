

while True:
    try:
        num1=int(input("Enter the first Number:"))
        num2=int(input("Enter the second Number:"))

        result=num1/num2
        print(result)
        
    except Exception as e:
        print(f"Error: {e}")
    # Else block only will get excute if there is no error occurs in try block   
    else:
        print("Everything think is ok in the code.")