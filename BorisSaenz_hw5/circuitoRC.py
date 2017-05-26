# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def funch(y0, y):
	chi_squared = (1.0/2.0)*sum(((y0-y)/1000.0)**2) #Al parecer diverge bastante rápido
	return np.exp(-chi_squared)

def funck(t,Q,ta):
	return Q*(1.0-np.exp(-t*ta)) #Parece ser también que /RC es más duro computacionalmente que ta = 1/RC

a = np.loadtxt("CircuitoRC.txt")
t = a[:,0]
q = a[:,1]



Qw = np.empty((0)) 
Tw = np.empty((0))
lw = np.empty((0))



Qw = np.append(Qw, 101)
Tw = np.append(Tw, 0.01)

yinit = funck(t, Qw[0], Tw[0])
lw = np.append(lw, funch(q,yinit))

it = 20000

for i in range(it):
    Rt = np.random.normal(Qw[i], 0.1) 
    Ct = np.random.normal(Tw[i], 0.1)

    yinit = funck(t, Qw[i], Tw[i])
    yn = funck(t, Rt, Ct)
    
    linit = funch(q,yinit)
    ln = funch(q,yn)

    alpha =  ln/linit
    if(alpha>=1.0):
        Qw  = np.append(Qw,Rt)
        Tw  = np.append(Tw,Ct)
        lw = np.append(lw, ln)
    else:
        beta = np.random.random()
        if(beta<=alpha):
            Qw = np.append(Qw,Rt)
            Tw = np.append(Tw,Ct)
            lw = np.append(lw, ln)
        else:
            Qw = np.append(Qw,Qw[i])
            Tw = np.append(Tw,Tw[i])
            lw = np.append(lw, linit)

Cr0 = Qw/10.0
Rr0 = 1.0/(Qw*Cr0)

rta = np.argmax(lw)

Tfun = Tw[rta]
Qfun = Qw[rta]

Cdef = Qw/10
Rdef = 1.0/(Cdef*Tw)





nm=plt.figure
fit = funck(t,Qfun, Tfun)

plt.scatter(t,q)
plt.title(('R=%.3fOhms, C= %.3f F' %(Rdef[rta], Cdef[rta])))
plt.xlabel("t [s]")
plt.ylabel("Q [q]")
plt.plot(t, fit, color ='r')

plt.savefig("pru.png")



tg = plt.figure()
sap = np.empty((0))
hehO = np.empty((0))


for i in range(len(Rdef)):
    sap= np.append(sap, funch(q, funck(t,Qw[i],Tw[i]) ))
plt.scatter(Rdef,sap)
plt.title("Verosimilitud vs R")
plt.ylabel("Verosimitud")
plt.xlabel("R")
plt.savefig("Vr.png")


yu = plt.figure()
plt.scatter(Cdef,sap)
plt.title("Verosimilitud vs C")
plt.ylabel("Verosimilitud")
plt.xlabel("Capacitancia")
plt.savefig("Vc.png")





fr = plt.figure()
plt.hist(Cdef, 100, normed=False)
plt.title("Histograma de la capacitancia")
plt.savefig("hC.png")



jk = plt.figure()
plt.scatter(Rdef,Cdef)
plt.title("Recorridos")
plt.ylabel("Recorrido resistencia")
plt.xlabel("Recorrido capacitancia")
plt.savefig("RrRc.png")

we = plt.figure()
plt.scatter(Tw,Qw)
plt.title("Recorrido variables reales")
plt.ylabel("Tau [1/s]")
plt.xlabel("Qmax [q]")
plt.savefig("Rqt.png")



yh = plt.figure()
plt.hist(Rdef, 50, normed = False)
plt.title("Histograma de la resistencia")
plt.savefig("hR.png")

















