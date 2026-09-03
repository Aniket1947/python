import numpy as np 
import matplotlib.pyplot as plt
Years=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
Virat=[900,1200,1100,1400,1300,1550,1500,1300,1100,1000]
Rohit=[850,1300,1200,1300,1500,1600,1400,1400,1200,1100]
    
x=np.arange(len(Years))
print(x)
width=0.40
print(x-width)
print(x)

plt.bar(x-width,Virat,width=width,label="Virat Kholi's Runs")
plt.bar(x,Rohit,width=width,label="Rohit Sharma's Runs")
plt.xlabel("Years")
plt.ylabel("Runs")
plt.title("Runs Comparision")
plt.xticks(x,Years)
plt.legend()
plt.show()
