from matplotlib import pyplot as plt
import numpy as np
import flowtools

'''Area ratio (reading table1manual.txt)'''
with open("table1manual.txt", "r") as file:
    lines2 = file.readlines()

x_list = []
AAt_list = []

for line in lines2:
    if line != "" and line[0] != "x": 
        numbers = line.split(" ")
        x_list.append(float(numbers[0]))
        AAt_list.append(float(numbers[2]))



'''Measured pressure ratio (reading testfile.txt)'''
#Measured pressure ratio
with open("testfile.txt", "r") as file:
    lines = file.readlines()

mm_list = []
ppt_list = []

for line in lines:
    if line != "" and line[0] != "%": 
        line = line.strip()
        numbers = line.split("	      ") 
        mm_list.append(float(numbers[0]))
        ppt_list.append(float(numbers[1]))

#Quasi-1D theory
ppt1D_list = []
for i in range(len(AAt_list)):
    if AAt_list[i-1] < AAt_list[i]:
        ppt1D_number = flowtools.flowisentropic2(1.4, AAt_list[i], "sup")[2]
    else:
        ppt1D_number = flowtools.flowisentropic2(1.4, AAt_list[i], "sub")[2]
    ppt1D_list.append(ppt1D_number)


'''Mach number (from measured p/pt and flowtools)'''
#From measured pressure ratio
mach_list = []
for i in ppt_list:
    mach_number = float(flowtools.flowisentropic2(1.4, i, "pres")[0])
    mach_list.append(mach_number)

#Quasi-1D theory
mach1D_list = []
for i in range(len(ppt1D_list)):
    mach1D_number = float(flowtools.flowisentropic2(1.4, ppt1D_list[i], "pres")[0])
    mach1D_list.append(mach1D_number)



'''Plot'''
#A/At from table 1 in manual
plt.subplot(311)
plt.plot(x_list, AAt_list, "black", marker = "o", markersize = 5, markerfacecolor = "none", markeredgecolor = "black")
#plt.title("x [mm] vs A/A$_t$ [-]")
plt.xlabel("x [mm]")
plt.ylabel("A/A$_t$ [-]") 
plt.xlim(40, 200)
plt.ylim(1, 2)
plt.grid()

#p/pt from testfile.txt (measured pressure ratio) and p/pt from quasi-1D theory
plt.subplot(312)
plt.plot(mm_list, ppt_list, "r", marker = "+", markersize = 6) #From measured pressure ratio
plt.plot(x_list, ppt1D_list, "black", marker = "o", markersize = 5, markerfacecolor = "none", markeredgecolor = "black") #From quasi-1D theory
#plt.title("x [mm] vs p/p$_t$ [-] from testfile.txt (measured pressure ratio)")
plt.xlabel("x [mm]") 
plt.ylabel("p/p$_t$ [-]") 
plt.xlim(40, 200)
plt.ylim(0, 0.8)
plt.grid()
plt.legend(["Quasi-1D theory", "Measured pressure ratio"])

#M from p/pt measured and flowtools
plt.subplot(313)
plt.plot(mm_list, mach_list, "r", marker = "+", markersize = 6) #From measured pressure ratio
plt.plot(x_list, mach1D_list, "black", marker = "o", markersize = 5, markerfacecolor = "none", markeredgecolor = "black") #From quasi-1D theory
#plt.title("x [mm] vs Mach number [-]") 
plt.xlabel("x [mm]")
plt.ylabel("M [-]")
plt.xlim(40, 200)
plt.ylim(0.5, 2.5)
plt.grid()
plt.legend(["Quasi-1D theory", "Calculated from measured pressure ratio"])

plt.tight_layout()
plt.show()

