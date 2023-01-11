from matplotlib import pyplot as plt

with open("data_for_report/Data_Test_3A.txt", "r") as file:
    lines3 = file.readlines()
with open("data_for_report/Data_Test_4A.txt", "r") as file:
    lines4 = file.readlines()
with open("data_for_report/Data_Test_5A.txt", "r") as file:
    lines5 = file.readlines()
mm_list = []
ppt3_list = []
ppt4_list = []
ppt5_list = []
xshock = [620, 535, 380]
for line in lines3:
    if line != "%" and line[0] != "%":
        line = line.strip()
        numbers = line.split("   ")
        mm_list.append(float(numbers[0]))
        ppt3_list.append(float(numbers[1]))

for line in lines4:
    if line != "%" and line[0] != "%":
        line = line.strip()
        numbers = line.split("   ")
        ppt4_list.append(float(numbers[1]))

for line in lines5:
    if line != "%" and line[0] != "%":
        line = line.strip()
        numbers = line.split("   ")
        ppt5_list.append(float(numbers[1]))




plt.plot(mm_list, ppt3_list , marker="+", markersize=6, color = 'red', label = "Measured pressure ratio 3")
plt.plot(mm_list, ppt4_list , marker="o", markersize=6, color = 'green', label = "Measured pressure ratio 4")
plt.plot(mm_list, ppt5_list, marker="s", markersize=6, color = 'blue', label = "Measured pressure ratio 5")
#plt.plot(xshock[0], 0.8163958499352209, label = "1")
#plt.plot(xshock[1], 0.7696071903994393, label = "1")

plt.vlines(xshock[0],.1,1, color = 'red', label = 'Theoretical Shock Wave 3')
plt.vlines(xshock[1],.1,1, color = 'green', label = 'Theoretical Shock Wave 4')
plt.vlines(xshock[2],.1,1, color = 'blue', label = 'Theoretical Shock Wave 5')
plt.xlabel("x [mm]")
plt.ylabel("p/p$_t$ [-]")
#plt.xlim(40, 200)
#plt.ylim(0, 0.8)
plt.grid()
plt.legend()

plt.show()