import shutil

shutil.copy("D:\\python\\file_handling\\Aniket.txt","D:\\python\\file_handling\\sameer.txt")#This will copy source path to desination path
shutil.copytree("D:\\python\\file_handling","D:\\python\\file_handling1") #This will copy whole directory  from source path to desination path
shutil.rmtree("D:\\python\\file_handling1") #This will remove the whole directory
