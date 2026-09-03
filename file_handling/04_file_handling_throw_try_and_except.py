try:
    f=open("D:\\python\\file_handling\\Aniket.txt","r")
    content=f.read()
    print(content)
    f.close()
except:
    print("File not found")