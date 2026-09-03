from abc import ABC,abstractmethod

class bank(ABC):
    def database(self):
        print("Connecting to Database...")

    @abstractmethod
    def security(self):
        print("This is security class")
    
class mobile(bank):
    def display(self):
        print("This is mobile Application.")
        
    def security(self):
        print("This is security class from mobile")
        return super().security()

mob=mobile()
mob.database()
mob.security()