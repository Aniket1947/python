# try:
#     with open("Aniket.txt","r") as f:
#         content=f.readline()
#         # content1=f.readline()
#         # content2=f.readline()
#         print(content)
#         # print(content1)
#         # print(content2)
#         for line in f:
#             print(line,end="")
#         f.close()
# except:
#     print("File not found!")


# Using readline() function

# try:
#     with open("Aniket.txt","r") as f:
#         while True:
#             line=f.readline()
#             if not line:
#                 break
#             print(type(line))
#             print(line,end="")
# except:
#     print("File not found!")


# try:
#     with open("D:\\python\\file_handling\\Aniket.txt","r") as f:
#         i=0
#         while True:
#             i=i+1
#             line=f.readline()
#             if not line:
#                 break
#             m1=line.split(",")[0]
#             m2=line.split(",")[1]
#             m3=line.split(",")[2]
#             print(f"The Marks of student {i} in Math is {m1}")
#             print(f"The Marks of student {i} in Science is {m2}")
#             print(f"The Marks of student {i} in English is {m3}")
# except:
#     print("File not found!")


try:
    with open("Aniket2.txt","w") as f:
        lines=["Line1","Line2","Line3"]
        for line in lines:
            f.writelines(line+"\n")
except:
    print("File Not Found")