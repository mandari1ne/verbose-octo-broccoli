import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция z(x, y) = x^0.25 + y^0.25
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z1 = x**0.25 + y**0.25

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('График функции z(x, y) = x^0.25 + y^0.25')
plt.show()

# Функция z(x, y) = x^2 - y^2
z2 = x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z2, cmap='magma')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('График функции z(x, y) = x^2 - y^2')
plt.show()

# Функция z(x, y) = 2*x + 3*y
z3 = 2*x + 3*y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z3, cmap='plasma')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('График функции z(x, y) = 2*x + 3*y')
plt.show()

# Функция z(x, y) = x^2 + y^2
z4 = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z4, cmap='inferno')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('График функции z(x, y) = x^2 + y^2')
plt.show()

# Функция z(x, y) = 2 + 2*x + 2*y - x^2 - y^2
z5 = 2 + 2*x + 2*y - x**2 - y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z5, cmap='cividis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('График функции z(x, y) = 2 + 2*x + 2*y - x^2 - y^2')
plt.show()