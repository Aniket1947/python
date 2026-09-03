# # from PyPDF2 import PdfWriter

# # merger=PdfWriter()

# # pdfs=[]
# # n=int(input("Enter the number of PDF you want to merge:"))

# # for i in range(0,n):
# #     name=input(f"Enter the {i+1} pdf name:")
# #     pdfs.append(name)
# #     print(pdfs)

# # for pdf in pdfs:
# #     merger.append(pdf)
    

# # merger.write("Merger.pdf")
# # merger.close()
# from PyPDF2 import PdfWriter

# merger=PdfWriter()
# pdfs=[]

# n=int(input("Enter the Number you want to merge PDF:"))

# for i in range(n):
# 	name=input(f"Enter the {i+1} pdf name:")
# 	pdfs.append(name)

# for pdf in pdfs:
# 	merger.append(pdf)

# merger.write("Merged.pdf")
# merger.close()






from PyPDF2 import PdfWriter

merger=PdfWriter()
pdfs=[]
n=int(input("Enter the Number of pdf you want to merge:"))

for i in range(0,n):
    name=input(f"Enter the {i+1} pdf name:")
    pdfs.append(name)
    
for pdf in pdfs:
    merger.append(pdf)

merger.write("Merged.pdf")
merger.close()
 



