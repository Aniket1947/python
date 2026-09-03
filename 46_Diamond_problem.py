class A:
    def display(self):
        print("Display from A Class.")
    
class B(A):
    pass
    def display(self):
        print("Display from B Class.")

class C(A):
    pass
    def display(self):
        print("Display from C Class.")

class D(B,C):
    pass
    # def display(self):
    #     print("Display from D Class.")


d=D()
d.display()
print(D.mro())