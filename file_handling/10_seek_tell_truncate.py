
#Example of seek function:seek function will skip the number of character f.seek(6) 
with open("D:\\python\\file_handling\\Aniket.txt","r") as f:
    f.seek(6)
    data=f.read()
    print(data)
    #123456789et


with open("D:\\python\\file_handling\\Aniket.txt","r") as f:
    f.seek(10)
    print(f.tell())
    data=f.read()
    print(data)






#Example of truncate in this example we use truncate it means that only f.truncate(5) 5 character will store in file. 
# with open("D:\\python\\file_handling\\Aniket.txt","w") as f:
#     f.write("Hello World!")
#     f.truncate(5)

# with open("D:\\python\\file_handling\\Aniket.txt","r") as f:
#     print(f.read())
