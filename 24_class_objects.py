class employee:
    company="Wipro"
    def get_salary(self):
        return 40000
    def greet(self,name):
        self.ename=name
        return (f"Hey {self.ename},Welcome to Wipro.")



e1=employee()
print(e1.get_salary())
print(e1.company)
print(e1.greet("Aniket"))
print(employee.get_salary(e1))