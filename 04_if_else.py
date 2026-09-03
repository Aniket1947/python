age=int(input("Enter Your age:"))
if(age> 18 and age <=60):
    print("You can Dirve.")
elif(age>60 and age<80):
    print("Drive carefully because you are senior citizens.")
elif(age>=81):
    print("Avoid driving because your age is above 80 years.")
else:
    print('You cannot drive you are below 18 years.')



