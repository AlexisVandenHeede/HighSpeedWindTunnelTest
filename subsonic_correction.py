import flowtools
from matplotlib import pyplot as plt



'''Step 1 - Measure reference pressure ratio at x_0, ppt_x0'''
px0pt = 0.893 #0.781381 #Measured reference pressure ratio at x = 0 (change this to the correct value) 
#0.776 is the lowest it goes without giving an error (if you go lower then in flowtools you are taking the square root of a negative number somewhere in the calculation)



'''Step 2 - Calculate local M and A(x_0) / A* using flowtools.py'''
M_x0 = flowtools.flowisentropic2(1.4, px0pt, "pres")[0]
Ax0Astar = flowtools.flowisentropic2(1.4, px0pt, "pres")[4]



'''Step 3 - Determine A(x_0) / A_t from given wind tunnel geometry'''
Ax0At = 1.175 #Using x_0 = 44.8 [mm] (first entry in Chapter 4, Table 1)


'''Step 4 - Find A_t / A* (correction coefficient)'''
coeff = Ax0Astar / Ax0At



'''Step 5 - For each value of x, determine A(x) / A_t from given wind tunnel geometry'''
with open("table1manual.txt", "r") as file:
    lines = file.readlines()

x_list = []
AAt_list = []

for line in lines:
    if line != "" and line[0] != "x": 
        numbers = line.split(" ") 
        x_list.append(float(numbers[0]))
        AAt_list.append(float(numbers[2]))



'''Step 6 - For each value of x, calculate A(x) / A*'''
AAstar_list = []
for i in AAt_list:
    AAstar_list.append(float(coeff * i))
    print(float(coeff * i))

print("coeff =", coeff)


'''Step 7 - For each value of x, find M(x) and p(x)/p_t using flowtools.py'''
M_list = []
ppt_list = []
for i in AAstar_list:
    M = flowtools.flowisentropic2(1.4, i, "sub")[0]
    M_list.append(M)
    ppt = flowtools.flowisentropic2(1.4, i, "sub")[2]
    ppt_list.append(ppt)
    print(M)



'''Plot'''
plt.plot(x_list, M_list, "black", marker = "o", markersize = 5, markerfacecolor = "none", markeredgecolor = "black")
plt.plot(x_list, ppt_list, "red", marker = "o", markersize = 5, markerfacecolor = "none", markeredgecolor = "red")
plt.xlabel("x [mm]")
plt.ylabel("M [-], p/p$_t$ [-]")
plt.xlim(40, 200)
plt.ylim(0, 1.1)
plt.grid()
plt.legend(["Mach number", "Pressure ratio"])
plt.show()







