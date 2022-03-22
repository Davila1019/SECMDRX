import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)
theta= np.arange(0,2*np.pi,0.01)
phi= np.arange(0,np.pi,0.01)
theta,phi=np.meshgrid(theta,phi)
r=np.sqrt(9)
x= r*np.sin(phi)*np.cos(theta)
y= r*np.sin(phi)*np.sin(theta)
z=r*np.cos(phi)
ax.plot_surface(x,y,z, color='blue')

plt.show()
