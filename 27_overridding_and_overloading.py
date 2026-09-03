#Method overridding

class Father:
    def sleep(self): #We can call the method by creating the object of this class.As we can see this class was inherit by child class so child class can aslo call this method but in child class having same sleep method name it will overide and it will only call child class sleep method.
        print("Sleep time is 11am to 6am.")

    def eat(self): # Same as it is rule apply on this method.
        print("Eating time 9am")

class Son(Father):
    def sleep(self): #With the same name the sleep method will override the Father(parent) class.if this sleep method not define in child class then the parent class sleep method will call from child object i.e, with s.sleep().
        super().sleep()
        print("Sleep time is 1am to 9am.")
     
    def eat(self): # Same as it is rule apply on this method.
        print("Eating time is 10am.")

s=Son()
s.sleep() 

#########################################################################################################################

#Method Overloading Example 1

class Calculator:
    def add(self, *args):
        total=0
        for i in args:
            total=total+i
        return total


calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3, 4))

#########################################################################################################################

#Method Overloading Example 2

class Example:
    def greet(self, name=None):
        if name is not None: # You also use if name != None:
            print(f"Hello, {name}!")
        else:
            print("Hello!")

obj = Example()
obj.greet()
obj.greet("Alice")

#########################################################################################################################

#Method Overloading Example 3

from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first + second
    print(result)

@dispatch(int, int, int)
def product(first, second, third):
    result = first + second + third
    print(result)

@dispatch(float, float, float)
def product(first, second, third):
    result = first + second + third
    print(result)

product(2, 3)
product(2, 3, 2)
product(2.2, 3.4, 2.3)