import os

a=os.listdir("D:\\python\\file_handling") #This will return list of file inside the directory
print(a)
print(os.getcwd()) #This will return current working directory
print(os.path.exists("D:\\python\\file_handling")) #This will return boolean value of the path exists it will retrun True else False
os.remove("D:\\python\\file_handling\\example.txt") #This will remove the file only if the file is empty.
