import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)


x = np.linspace(-4, 4, 500)
y = np.linspace(-4, 4, 500)
e = np.linspace(-4, 4, 500)

X, Y = np.meshgrid(x,y)
def z(x,y):
    return np.cos(np.sqrt(x**2 + y**2))

# ax.contourf(X,Y,z(X,Y))
ax.plot_surface(X, Y, z(X,Y), color='red')
plt.show()
