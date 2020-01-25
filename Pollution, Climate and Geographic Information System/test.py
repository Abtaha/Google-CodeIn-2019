import numpy as np
from scipy.interpolate import griddata, interp2d
import matplotlib.pyplot as plt


a = [40.7789, 42.9486, 42.7431, 43.1167]
b = [-73.9692, -78.7369, -73.8092, -77.6767]
grid_x, grid_y = np.mgrid[-80:-71:(((-71)-(-80))/float(10000)), 40:45:((45-40)/float(10000))]
#grid_x, grid_y = np.meshgrid(a,b)

A = [[ 40.7789, -73.9692],
[ 42.9486, -78.7369],
[ 42.7431, -73.8092],
[ 43.1167, -77.6767]]


x = [x[1] for x in A]
y = [x[0] for x in A]
points = np.array((x, y)).T
values = np.array([ 8.69447733, 12.25476095,  8.2312761,   9.03395435])


interpolated = griddata(points, values, (grid_x, grid_y), method='nearest')

plt.imshow(interpolated.T, extent=(-80, -71, 40, 45), origin='lower', cmap="coolwarm", alpha=0.5)
plt.colorbar()
plt.show()