import numpy as np
import matplotlib.pyplot as plt

def linearconv(nx):
    dx = 2 / (nx - 1)
    nt = 20
    dt = .025
    c = 1
    sigma = .5

    dt = sigma * dx

    u = np.ones(nx)
    u[int(.5/dx):int(1/dx + 1)] = 2

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * (dt/dx) * (un[i] - un[i-1])

    plt.plot(np.linspace(0,2,nx), u)
    plt.show()


def linearconv_constant_dt(nx):
    dx = 2 / (nx - 1)
    nt = 20
    dt = .025
    c = 1

    u = np.ones(nx)
    u[int(.5/dx):int(1/dx + 1)] = 2

    un = np.ones(nx)

    for n in range(nt):
        un = u.copy()
        for i in range(1,nx):
            u[i] = un[i] - c * (dt/dx) * (un[i] - un[i-1])

    plt.plot(np.linspace(0,2,nx), u)
    plt.show()

# linearconv(41)
# linearconv(61)
# linearconv(71)
# linearconv(85)
# linearconv(101)
linearconv(121)