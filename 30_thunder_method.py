class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return f"{self.x + other.x},{self.y + other.y}"
    
    def __sub__(self,other):
        return f"{self.x - other.x},{self.y - other.y}"
    
    def __mul__(self,other):
        return (f"{self.x*other.x},{self.y*other.y}")
    
    def __str__(self):
        return f"Victor: {self.x},{self.y}"
    

v1=vector(4,2)
v2=vector(3,1)
v3=v1*v2
v4=v1+v2
print(v3)
print(v4)
