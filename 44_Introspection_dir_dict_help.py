# You can perform dir,__dict__,and help() method in list,tuple,etc.

# x=[1,2,3,4,5]
# y=[6,7,8,9]
# print(dir(x)) #Through this method we can able to see all the method which we can perform on this list.
# print(x.__add__(y)) #This Will add both the list in single list
# print(x.append(6)) #This append method will add 6 at the end of the element. 
# print(x)

# x=(1,2,3,4,5)
# y=(6,7,8,9)
# print(dir(x))
# print(x.__add__(y))

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=person("Aniket",23)
print(type(p1.__dict__))
print(p1.__dict__)
p2=person("Harry",24)
print(p2.__dict__)
print(help(person))