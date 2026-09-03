class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def getInfo(self):
        print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")

class programmer(employee):
    def __init__(self,name,salary,language):
        self.name=name
        self.salary=salary
        self.language=language

    def programmer_language(self):
        print(f"The name of employee is {self.name} and the salary of employee is {self.salary} and he write a code in {self.language}.")
    
e=employee("Aniket",900000)
e.getInfo()
p=programmer("Rohan",600000,"Python")
p.programmer_language()
