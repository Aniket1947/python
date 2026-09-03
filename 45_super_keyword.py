class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showinfo(self):
        print(f"The name of employe is {self.name} and the id of employee is {self.id}")
    
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        super().showinfo()
        self.lang=lang
    

p=programmer("Aniket",23,"Python")
print(p.name)
print(p.id)
print(p.lang)