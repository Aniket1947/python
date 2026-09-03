with open("D:\\python\\file_handling\\Aniket1.txt","w") as f:
    text="Hello World!"
    f.write(text)

with open("D:\\python\\file_handling\\Aniket1.txt","r") as f:
    content=f.read()
    print(content)

# with open("D:\\python\\file_handling\\Aniket1.txt","a") as f:
#     text="\nHello World2!"
#     f.write(text)

# with open("D:\\python\\file_handling\\Aniket1.txt","r") as f:
#     content=f.read()
#     print(content)
