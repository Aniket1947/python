class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    #Both function __init__ and fromStr both are output is same but both function taking arugment in different form __init__ is taking normaling as we use, but fromStr is taking string so for that reason we use @classmethod as alternative constructor. 
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1=employee("Aniket",30000)
print(e1.name)
print(e1.salary)

string="Aniket-35000"
e2=employee.fromStr(string)
print(e2.name)
print(e2.salary)
