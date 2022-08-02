import numpy as np
import matplotlib.pyplot as plt
import time, sys

# parameter
nx = 41          # number of x grid point
dx = 2 / (nx-1)  # x interval
nt = 25          # number of timesteps
dt = .025        # delta t
c = 1            # wavespeed

# initial condition
u = np.ones(nx)
u[int(.5 / dx): int(1 / dx + 1)] = 2 # setting u = 2 if 0.5 <= x <= 1
# print(u)
# plt.plot(np.linspace(0,2,nx), u)
# plt.show()

un = np.ones(nx)  # initialize a temporary array

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
    # for i in range(nx):
        u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

plt.plot(np.linspace(0,2,nx), u)
plt.show()        
