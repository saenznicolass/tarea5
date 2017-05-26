import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm



ar1 = np.loadtxt("arch1.txt")
ar2 = np.loadtxt("arch2.txt")
a = np.loadtxt("Canal_ionico.txt")
b = np.loadtxt("Canal_ionico1.txt")
c = np.loadtxt("resultados.txt")

x1 = a[:,0]
x2 = b[:,0]
y1 = a[:,1]
y2 = b[:,1]

x3 = c[0][0]
y3 = c[0][1]
ra = c[0][2]

px1 = c[1][0]
py1 = c[1][1]
ra1 = c[1][2]


# imprimir con %, usar Circle, artist y fill 

fig = plt.gcf()
ax = fig.gca()
plt.scatter(x1,y1)
plt.scatter([x3], [y3], color = 'b')
d = plt.Circle((x3,y3), ra, fill = False)
ax.add_artist(d)
plt.title(('x = %.3f, y = %.3f, R = %.3f' %(x3, y3, ra)))
plt.savefig("fig1.png")


h = plt.figure()
fig = plt.gcf()
ax = fig.gca()
plt.scatter(x2,y2)
plt.scatter([px1], [py1], color = 'r')
e = plt.Circle((px1,py1), ra1, fill = False)
ax.add_artist(e)
plt.title(('x = %.3f, y = %.3f, R = %.3f' %(px1, py1, ra1)))
plt.savefig("fig2.png")


f = plt.figure()
plt.hist2d(ar1[:,0], ar1[:,1], bins = 100,)
plt.title('Histograma 1')
plt.savefig("hist1.png")

g= plt.figure()
plt.hist2d(ar2[:,0], ar2[:,1], bins = 200)
plt.title('Histograma 2')
plt.savefig("hist2.png")







