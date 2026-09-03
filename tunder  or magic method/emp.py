class Employee:
    def __init__(self,name):
        self.name=name

    def __len__(self): #Throw this method we are getting the actual length of name arugment which is passed.
        i=0 # Here i is initialize with zero
        for c in self.name: #The for run on self.name it will itreate each single character of self.name
            i = i+1 #here the value of i increase by 1
        return i #Here we will get the actual length of self.name
    
    def __str__(self): #This method will automatically called when we print class object variable name.Also we can call them specifically by calling print(str(e))
        return f"The name of employee is {self.name}."
    
    def __repr__(self): #This method will automatically called when we don't get the __str__ method.Also we can call them specifically by calling print(repr(e))
        return f"Employee('{self.name}')"
    
    def __call__(self): #This method will get call by just class object name i.e e().
        print("Hey I am good.")
    
e=Employee("Aniket")
print(e)
print(str(e))
print(repr(e))
e()
print(len(e))