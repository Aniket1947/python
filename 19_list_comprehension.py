
#Without list comprehension 
# a=5
# table=[]
# for i in range(1,11):
#     table.append(a*i)
# print(table)

#With list comprehension 
# table=[5*i for i in range(1,11)]
# print(table)
# num=[2,3,4,5,6,7,8,9]
# even_number=[x for x in num if x %2 ==0]
# print(even_number)

# square=[x*x for x in num ]
# print(square)

# flat = [num for row in matrix for num in row]
# print(flat)

# flat = []
# for row in matrix:
#     for num in row:
#         flat.append(num)
# print(flat)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = []

for row in matrix:                 # Outer loop
    print(f"Row: {row}")           # Debug: Show current row
    for num in row:                # Inner loop
        print(f"   Number: {num}") # Debug: Show each number inside the row
        flat.append(num)           # Add the number to flat list

print("Final Flattened List:", flat)



