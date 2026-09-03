
#Python doesn't provide any protection of public private and protected this is only Convention(Ek tarika ya fhir soch hai code karne ki) in python.

#Public Access specifier Which is normal as we use.
class employee:
    def __init__(self):
        self.name="Aniket Varma"

e=employee()
print(e.name)

#Protected Access specifier.

class program:
    def __init__(self):
        self._language="Python" #In this single _ we treated as protected specifier which is only accessable in class and sub-class as an convention(Ek tarika ya fhir soch hai code karne ki).But we can access it easily.
    
p=program()
print(p._language)

#Private Access specifier

class task:
    def __init__(self):
        self.__result="Task Completed"


t=task()
# print(t.__result) #This will throw an error because __ underscore it means we cannot access directly but you can access indirectly
print(t._task__result) #Throw this you can access __ underscore this is known as name mangling.
print(t.__dir__())