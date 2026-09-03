import matplotlib.pyplot as plt
import numpy as np

Years=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
Rohit=[2300,2400,2450,2700,2600,3100,3000,3200,3400,3700]
Virat=[2200,2300,2400,2600,2900,3000,3200,3300,3500,3600]

plt.plot(Years,Virat,'ro--',label="Virat Kholi")
plt.plot(Years,Rohit,color='Green',linestyle=':',marker='^',label="Rohit Sharma")
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Runs Comparision")
plt.grid(True)
plt.style.use("fivethirtyeight")
plt.legend()
plt.show() 

# for i in range(2):
#     plt.plot(np.random.rand(100),linewidth=1)

# plt.title("To much data can be confusing")
# plt.grid()
# plt.tight_layout()
# plt.show()