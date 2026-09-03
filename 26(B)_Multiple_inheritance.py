#Simple Example of multiple inheritance

class ParentA:
    def method_a(self):
        print("Method from ParentA")

class ParentB:
    def method_b(self):
        print("Method from ParentB")

class Child(ParentA, ParentB):
    def method_c(self):
        print("Method from Child")

child_obj = Child()
child_obj.method_a()
child_obj.method_b()
child_obj.method_c()

#Complex Example of multiple inheritance

# class QA:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.app = "Googlepay"

#     @staticmethod
#     def greet():
#         print("Hello,")
    
#     def getInfo1(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}. We are working on the {self.app} application.")

# class programmer:
#     def __init__(self, name, salary, language):
#         self.name = name
#         self.salary = salary
#         self.language = language
    
#     def getInfo(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}. We are working in the {self.language} language.")

# class employee(QA, programmer):
#     def __init__(self, name, salary, language):
#         QA.__init__(self, name, salary)
#         programmer.__init__(self, name, salary, language)

#     def getInfo(self):
#         print(f"The employee {self.name} has a salary of {self.salary}. They work on the {self.app} application and use the {self.language} language.")


# emp = employee("Aniket", 90000, "Python")
# emp.greet()
# emp.getInfo()
# emp.getInfo1()