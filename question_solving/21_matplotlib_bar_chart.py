#Simple Bar chart

# import matplotlib.pyplot as plt

# Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]
# Virat = [450,650,900,600,300,1200,1050,690,750,800]

# plt.bar(Years,Virat,label="Virat Kholi Runs")
# plt.xlabel("Years")
# plt.ylabel("Runs Scored")
# plt.title("Virat Kholi Run's")
# plt.legend()
# plt.tight_layout()
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# Virat = [450,650,900,600,300,1200,1050,690,750,800]
# Rohit = [500,800,650,900,1000,450,200,450,900,700]

# player=[Virat,Rohit]

# x=np.arange(len(Years))
# width=0.35

# plt.bar(x-width/2,Virat,width=width,label="Viart Kholi")
# plt.bar(x+width/2,Rohit,width=width,label="Rohit Sharma")

# for i in range(len(Years)):
#     plt.text(x[i] - width/2, Virat[i], str(Virat[i]),
#              ha="center", va="bottom", fontsize=9)
#     plt.text(x[i] + width/2, Rohit[i], str(Rohit[i]),
#              ha="center", va="bottom", fontsize=9)
    
# plt.xlabel("Years")
# plt.ylabel("Runs Scored")
# plt.title("Runs Scored By Player")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.xticks(x,Years)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# Virat  = [450,650,900,600,300,1200,1050,690,750,800]
# Rohit  = [500,800,650,900,1000,450,200,450,900,700]
# Sachin = [700,900,1000,650,1100,440,1300,200,900,600]

# x=np.arange(len(Years))
# width=0.25

# plt.bar(x-width,Virat,width=width,label="Virat Kholi Run's")
# plt.bar(x,Rohit,width=width,label="Rohit Sharma Run's")
# plt.bar(x+width,Sachin,width=width,label="Sachin Tendulkar Run's")

# for i in range(len(Years)):
#     plt.text(x[i]-width,Virat[i]+10,str(Virat[i]),ha='center',va='bottom',fontsize=9)
#     plt.text(x[i],Rohit[i]+10,str(Rohit[i]),ha='center',va='bottom',fontsize=9)
#     plt.text(x[i]+width,Sachin[i]+10,str(Sachin[i]),ha='center',va='bottom',fontsize=9)

# plt.xlabel("Years")
# plt.ylabel("Runs Scored")
# plt.title("Yearly Run Scored By the Player")
# plt.legend()
# plt.xticks(x,Years)
# plt.tight_layout()
# plt.grid(axis='y', linestyle='--', alpha=0.8)
# plt.show()

#########################################################################################################

# import matplotlib.pyplot as plt
# import numpy as np


# Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# Virat  = [450,650,900,600,300,1200,1050,690,750,800]
# Rohit  = [500,800,650,900,1000,450,200,450,900,700]
# Sachin = [700,900,1000,650,1100,440,1300,200,900,600]
# Dhoni  = [300,500,700,800,600,900,400,650,500,750]

# x=np.arange(len(Years))
# width=0.20

# plt.bar(x-1.5*width,Virat,width=width,label="Virat Kholi Runs")
# plt.bar(x-0.5*width,Rohit,width=width,label="Rohit Sharma Runs")
# plt.bar(x+0.5*width,Sachin,width=width,label="Sachin Tendulkar Runs")
# plt.bar(x+1.5*width,Dhoni,width=width,label="MS Dhoni Runs")

# for i in range(len(Years)):
#     plt.text(x[i]-1.5*width,Virat[i]+10,str(Virat[i]),ha='center',va='bottom',fontsize=8)
#     plt.text(x[i]-0.5*width,Rohit[i]+20,str(Rohit[i]),ha='center',va='bottom',fontsize=8)
#     plt.text(x[i]+0.5*width,Sachin[i]+10,str(Sachin[i]),ha='center',va='bottom',fontsize=8)
#     plt.text(x[i]+1.5*width,Dhoni[i]+10,str(Dhoni[i]),ha='center',va='bottom',fontsize=8)

# plt.xlabel("Years")
# plt.ylabel("Runs Scored")
# plt.title("Yearly Runs Scored By Player")
# plt.legend()
# plt.grid(axis='y',linestyle='--',alpha=0.8)
# plt.tight_layout()
# plt.xticks(x,Years)
# plt.show()

#########################################################################################################

# import matplotlib.pyplot as plt
# import numpy as np

# Years = [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010]

# Virat  = [450,650,900,600,300,1200,1050,690,750,800]
# Rohit  = [500,800,650,900,1000,450,200,450,900,700]
# Sachin = [700,900,1000,650,1100,440,1300,200,900,600]
# Dhoni  = [300,500,700,800,600,900,400,650,500,750]
# Rahul  = [600,750,800,700,650,850,900,500,650,780]

# x = np.arange(len(Years))
# width = 0.16

# plt.bar(x - 2*width, Virat,  width, label="Virat Kohli")
# plt.bar(x - width,   Rohit,  width, label="Rohit Sharma")
# plt.bar(x,           Sachin, width, label="Sachin Tendulkar")
# plt.bar(x + width,   Dhoni,  width, label="MS Dhoni")
# plt.bar(x + 2*width, Rahul,  width, label="Rahul Dravid")

# # ⭐ Add values on bars Use this for displaying values.
# for container in plt.gca().containers:
#     plt.bar_label(container, padding=3, fontsize=8)

# plt.xlabel("Years")
# plt.ylabel("Runs")
# plt.title("Runs Scored by Players")
# plt.xticks(x, Years)
# plt.legend()
# plt.tight_layout()
# plt.show()

#########################################################################################################
#Horizontal Bar Chart
import matplotlib.pyplot as plt
import numpy as np

Players=["Rohit","Virat","Sachin","Dhoni"]
Runs=[800,670,890,650]

plt.barh(Players,Runs)
for i in range(len(Players)):
    plt.text(Runs[i]-100,i,str(Runs[i]),ha='center')
plt.xlabel("Runs")
plt.ylabel("Players")
plt.title("Runs Scored By the player")
plt.legend()
plt.tight_layout()
plt.show()

#########################################################################################################
#########################################################################################################
#########################################################################################################