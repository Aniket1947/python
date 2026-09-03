# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     @property
#     def first_name(self):
#         l=self.name.split(" ")
#         # print(l)
#         return l[0]
    
#     @first_name.setter  
#     def first_name(self,first):
#         l=self.name.split(" ")
#         new_name=f"{first} {l[1]}"
#         self.name=new_name

    

# e=Employee("Aniket Varma",34500)
# # print(e.first_name())
# # e.first_name()
# # new_name=e.set_first_name("Sameer")
# # print(new_name)

# print(e.first_name)
# e.first_name="Sameer"
# print(e.name)

#####################################################################################################

# class employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self._salary=salary

#     @property
#     def salary(self):
#         return self._salary
    
#     @salary.setter
#     def salary(self,new_salary):
#         if self.salary > 0:
#             self._salary=new_salary
#             print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")
    
#     def info(self):
#         print(f"The name of employee is {self.name} and the salary of employee is {self.salary}")

# e=employee("Aniket",90000)
# e.info()
# e.salary=100000
# e.salary+=100000



#######################################################################################################

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance  # Protected attribute (not to be accessed directly)

#     # Getter
#     @property
#     def balance(self):
#         return self._balance

#     # Setter
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             print("❌ Balance cannot be negative!")
#         else:
#             self._balance = amount

#     # Deposit method
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"✅ Deposited {amount}. New balance: {self._balance}")
#         else:
#             print("❌ Deposit amount must be positive.")

#     # Withdraw method
#     def withdraw(self, amount):
#         if amount > self._balance:
#             print("❌ Insufficient balance!")
#         elif amount <= 0:
#             print("❌ Invalid withdrawal amount!")
#         else:
#             self._balance -= amount
#             print(f"💸 Withdrawn {amount}. New balance: {self._balance}")


# # --- Testing the Class ---
# acc = BankAccount("Aniket", 1000)

# # Access balance using getter
# print(f"Initial Balance: {acc.balance}")

# # Deposit money
# acc.deposit(500)

# # Withdraw money
# acc.withdraw(300)

# # Trying to set balance directly using setter
# acc.balance = -100   # ❌ Not allowed, prints error

# # Checking updated balance
# print(f"Final Balance: {acc.balance}")

#############################################################################################################

# class account:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
    
#     @property
#     def balance(self):
#         return self.salary
    
#     @balance.setter
#     def balance(self,amount):
#         if amount < 0:
#             print("Balance not should be in negative")
#         else:
#             self.salary=amount

#     def deposit(self,amount):
#         if amount > 0:
#             self.salary += amount
#             print(f"Deposit:{amount}.New Balance:{self.salary}")
#         else:
#             print("Deposit amount should be not in negative.")
    
#     def withdraw(self,amount):
#         if amount > self.salary:
#             print("Insufficient Balance")
#         elif amount <=0:
#             print("Invalid wothdraw Amount")
#         else:
#             self.salary -= amount
#             print(f"withdraw amount {amount}.Remaining Balance {self.salary}")
    
            

        
# acc=account("Aniket",60000)
# print(f"Initial Balance:{acc.balance}")

# acc.deposit(15000)
# acc.withdraw(5000)
# print(f"Final Balance: {acc.balance}")


class employee:
    def __init__(self,salary):
        self._salary=salary
        print(f"The salary of employee is {self._salary}")

    @property
    def get_salary(self):
        return self._salary
    
    @get_salary.setter
    def set_salary(self,new_salary):
        if new_salary > 0:
            self._salary=new_salary
        print(f"The new salary of employee is {self._salary}")
    

e=employee(4000)
e.set_salary=3000
print(e.get_salary)




