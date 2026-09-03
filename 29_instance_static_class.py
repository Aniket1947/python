# class employee:
#     company="Wipro"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def get_info(self):
#         print(f"The name of employe is {self.name} and the salary of employee is {self.salary}")

#     @staticmethod
#     def sum(a,b):
#         return a+b
    
#     @classmethod
#     def print_company(cls):
#         print(cls.company)
    
#     @classmethod
#     def change_company(cls,new_company):
#         cls.company=new_company
    
# e=employee("Aniket",80000)
# e.get_info() #This code is same as same return below
# employee.get_info(e) #This is why we pass self arugment in class function because class object passes in this example as e pass.
# print(e.sum(2,3))
# e.print_company()
# e.change_company("Tesla")
# e.print_company()
# print(employee.company)

class employee:
    company="Wipro"
    def __init__(self,name,salary,company):
        self.name=name
        self.salary=salary
        self.company=company

    def get_info(self):
        print(f"The name of company is {self.company} and the name of employee is {self.name} and the salary of employee is {self.salary}.")

    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def company_detail(cls):
        print(f"The name of company is {cls.company}")
    
    @classmethod
    def change_company(cls,new_company):
        print(f"Changing company name from {cls.company}",end=" ")
        cls.company=new_company
        print(f"to {new_company}")



e1=employee("Aniket",89000,"TCS")
e1.get_info()
print(e1.add(2,3))
e1.company_detail()
e1.change_company("Tesla")
e1.company_detail()


# class employee:
#     company="Wipro"
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     def info(self):
#         print(f"The name of employee is {self.name} and the salary of employee is {self.salary} and the company name is {self.company}")
    
#     @classmethod
#     def class_access(cls):
#         print(f"The company name is {cls.company}.")


# e=employee("Harry",80000)
# e.info()
# e.company="TCS"
# e1=employee("Rohan",50000)
# e.class_access()
