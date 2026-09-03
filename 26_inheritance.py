class Animal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print(f"This is Animal class and the name of dog is {self.name}.")
    
class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"The name of dog is {self.name} and he braks Wooh!")

a=Animal("Sweety",12)
# a.speak()
d=Dog("Bruno",13)
d.speak()
# d.Age()


# class Animal():
#     def dog(self):
#         print("Bow Bow")

# class Animal1(Animal):
#     def cat(self):
#         print("Meow Meow")

# a=Animal1()
# a.dog()
# a.cat()