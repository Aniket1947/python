# Docstring in def 
def sum(a,b):
    '''It takes two argument and print the sum of two argument '''
    print(f"The sum of two numbers are {a+b}")

print(sum.__doc__)
sum(4,6)

# docstring in class
class employee():
    '''This is employee docstring.'''
    def __init__(self):
        print("This is employee class.")

emp=employee()
print(emp.__doc__)


