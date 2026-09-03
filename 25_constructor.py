#Simple example of constructor without arugment
# class employee():
#     def __init__(self): # This init(Constructor) will call automatically once object is created.
#         print("Hey We are learning python.") 

# e=employee()

# Simple example of Constructor with arugment
class person():
    def __init__(self,name,occ):
        self.name=name
        self.occ=occ
    
    def info(self):
        print(f"The name of employee is {self.name} and the role of {self.name} is {self.occ}")


a=person("Aniket","Python Developer")
a.info()
b=person("Hrishi","Java Developer")
b.info()



# class employee:
#     company="Wipro" #This is class attribute
#     def __init__(self,name,salary,company):
#         self.name = name #This are the instance attribute
#         self.salary = salary
#         self.company=company
        
#     def greet(self): #This are the method attribute
#         return self.salary
    
#     def info(self):
#         return f"The name of employee is {self.name} and the salary of employee is {self.salary} and the company name is {self.company}."
#     def difference_between_class_and_instance_attribute(self):
#         return f"This company name comes from instance attribute name-{self.company} and this is class attribute called with class name i.e employee class company name-{employee.company}"
    
# e1=employee("Aniket",35000,"Tesla")
# print(e1.greet())
# print(e1.name)
# print(e1.info())
# print(e1.difference_between_class_and_instance_attribute())
# # Object Introspection
# # print(dir(e1))
