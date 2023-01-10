# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:23:42 2023

@author: alexi
"""
import matplotlib.pyplot as plt
import flowtools
import math 

'''Theoretical Calculations'''
# Exp. M4, M5, Pos Shock (all mm)
# 3A 15.0 10.0 - 630.0
# 4A 15.0 10.0 - 530.0
# 5A 15.0 10.0 - Second Throat
# 3B 18.0 10.0 - 630.0
# 4B 18.0 10.0 - 530.0
# 5B 18.0 10.0 - Second Throat

# A
hk2 = 14.6
dhdx = 0.01692
h0 = 8
xshock = [630, 530, 410]

# B
# hk2 = 11.8
# dhdx = 0.02472
# h0 = 2.2
# xshock = [630, 530, 410]

# distance between two throats
length = 760-410
# x step size in mm
step = 10
x_list = []
AAt_list = []
ppt_list = []
Tppt_list = [[],[],[]]
mach = []
PPTNSW = []

x = 410 
AAt = h0/hk2

for i in range(int(math.ceil(length/step))+1):   
    AAt = (h0+ x*dhdx )/hk2
    x_list.append(x)
    AAt_list.append(AAt)
    x += step

# ppt calculations for all three experiment 3, 4, 5
for j in range(3):
    mach = 1
    for i in range(len(x_list)):
        if i*step + 410 < xshock[j]:
            value = flowtools.flowisentropic2(1.4, AAt_list[i], 'sup')
        elif i*step + 410 == xshock[j]:
            print("NSW")
            value = flowtools.flownormalshock2(1.4, mach, 'mach')
            value = list(value)
            value[2] = float(value[2])*float(value[6]) # this calculates (static P 2)/(total P 2) after NSW
            print(value[2])
        else:
            value = flowtools.flowisentropic2(1.4, AAt_list[i], 'sub')
        mach = value[0]
        Tppt_list[j].append(float(value[2]))


#for i in range(len(x_list)): 
#    value = flowtools.flownormalshock2(1.4, mach, "mach")
#    mach = value[0]
#    PPTNSW.append(value[2])
#print(PPTNSW)

'''Measured pressure ratio (reading DATA)'''
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

plt.subplot(111)
plt.plot(x_list, AAt_list, marker = 'o', markersize = 5, color = 'black',
         markerfacecolor = 'none', markeredgecolor = 'black')
plt.plot(x_list, Tppt_list[0], marker = 'o', markersize = 5, color = 'green',
         markerfacecolor = 'none', markeredgecolor = 'green')
plt.plot(x_list, Tppt_list[1], marker = 'o', markersize = 5, color = 'blue',
         markerfacecolor = 'none', markeredgecolor = 'blue')
plt.plot(x_list, Tppt_list[2], marker = 'o', markersize = 5, color = 'red',
         markerfacecolor = 'none', markeredgecolor = 'red')
plt.xlabel('x [mm]')
plt.ylabel('A/A$_t$, P/p$_t$ [-]')
plt.xlim(400,770)
plt.vlines(xshock[0],1,1.5, color = 'green', label = 'Theoretical Shock Wave 3')
plt.vlines(xshock[1],1,1.5, color = 'blue', label = 'Theoretical Shock Wave 4')
plt.vlines(xshock[2],1,1.5, color = 'red', label = 'Theoretical Shock Wave 5')
plt.legend(["A/AT", "3 T P/PT", "4 T P/PT", "5 T P/PT",])
plt.grid()
plt.show()



"""#Matthias' comments

prettiest justification was boundary layers

boundary layer ~ cm scale

When flow is slow bl is thick
as flow accelerates bl becomes thinner

this causes the area change through the thorat to be less than expected causing the M_experiemtnal < M_theoretical)
except at throat (ask swastik), opposite can be said for after the M 



"""
