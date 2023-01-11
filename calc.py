import flowtools

Ar3 = 1.2606712328767122
Ar4 = 1.162164383561644

a = flowtools.flowisentropic2(1.4, Ar3, 'sub')
b = flowtools.flowisentropic2(1.4, Ar4, 'sub')
print("1")
print(a[2])
print(b[2])


mach3PreNSW = flowtools.flowisentropic2(1.4, Ar3, "sup")
mach4PreNSW = flowtools.flowisentropic2(1.4, Ar4, "sup")

print("2")
print(mach3PreNSW[2])
print(mach4PreNSW[2])

mach3postNSW = flowtools.flownormalshock2(1.4, mach3PreNSW[0], 'mach')
mach4postNSW = flowtools.flownormalshock2(1.4, mach4PreNSW[0], 'mach')
print('3')
print(mach3postNSW[2]*mach3PreNSW[2])
print(mach4postNSW[2]*mach3PreNSW[2])



#4 for downstream M


