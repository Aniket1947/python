class employee:
    def greet(self):
        print("This Greet is from employee class.")

class programmer(employee):
    def greet1(self):
        print("This greet is from programmer class.")

class another_programmer(programmer):
    def greet2(self):
        print("This greet is from Another programmer class.")

ap=another_programmer()
ap.greet()
ap.greet1()
ap.greet2()