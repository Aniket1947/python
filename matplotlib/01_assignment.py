import matplotlib.pyplot as plt

Years=[2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
Years1=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013]
Virat=[200,300,450,500,650,700,850,1000,1000,900]
Rohit=[250,250,550,550,550,750,750,1100,900,950]
Sehwag=[290,250,490,450,690,650,890,850,1050,990]

plt.plot(Years,Virat,'ro--',label="Virat Kholi")
plt.plot(Years,Rohit,color='Green',linestyle=':',marker='^',label="Rohit Sharma")
plt.plot(Years,Sehwag,'b*-.',label="Virendra Sehwag")

plt.xlabel("Year")
plt.ylabel("Runs Scored")
plt.title("Runs Comparision")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.style.use("fast")

plt.show()