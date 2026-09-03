# n=int(input("Enter the rows you want:"))
# for i in range(1, n + 1):  # Outer loop for rows
#         for j in range(i):  # Inner loop for stars in each row
#             print("*", end="")
#         print()


n=int(input("Enter the rows you want:"))
for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()