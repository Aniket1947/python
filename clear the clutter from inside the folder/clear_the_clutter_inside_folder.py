import os

# files=os.listdir("D:\python\clear the clutter from inside the folder\clutter")
# i=1
# print("Before ")
# for file in files:
#     if file.endswith(".png"):
#         print(f"D:\python\clear the clutter from inside the folder\clutter\{file}")
#         os.rename(f"D:\python\clear the clutter from inside the folder\clutter\{file}",f"D:\python\clear the clutter from inside the folder\clutter\{i}.png")
#         i+=1
# print("After")
# for file in files:
#     print(f"D:\python\clear the clutter from inside the folder\clutter\{file}")

#^^^^^^^^^^^^^^^^^^^^^^^^^^>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if not os.path.exists("data"):
    os.mkdir("data")

for i in range(1,101):
    os.mkdir(f"data/Day{i}")

files=os.listdir("data")
# print(files)
i=1
for file in files:
    os.rename(f"data/{file}",f"data/tutorial{i}")    
    i+=1