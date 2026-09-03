f=open("example.txt","w")
text="Hello World" #There are two type to write a into the file.This is first type.
f.write(text)
f.write("\nHello World1!")#This is second type of write file.
f.close() 

f=open('example.txt','r')
content=f.read()
print(content)
f.close()