import firedrake as fd
import numpy as np
import matplotlib.pyplot as plt
from model import SpecFO

"""
Generate randomized synthetic ice sheets and solve for velocity.
"""

data = np.load('project/solution_data/data.npy')

plt.imshow(data[1000,1,:,:])
plt.colorbar()
plt.show()
quit()

nx=100 
ny=100
dx=100e3
dy=100e3

model = SpecFO(nx, ny, dx, dy)

N = 2500
S0 = np.random.uniform(500., 4000., N)
sigmas = np.random.uniform(2.5, 10., N)
plot = False
data = []

for i in range(N):
    print(i)

    B, H = model.get_geometry1(B0 = 500., S0 = S0[i], sigma=sigmas[i])
    model.set_field(model.B, B)
    model.set_field(model.H, H)

    model.solver.solve()

    ubar0 = model.get_field(model.U.sub(0))
    ubar1 = model.get_field(model.U.sub(1))
    udef0 = model.get_field(model.U.sub(2))
    udef1 = model.get_field(model.U.sub(3))

    X = np.stack([
        B, H, ubar0, ubar1, udef0, udef1
    ])
    data.append(X)

    if plot:
        plt.subplot(3,2,1)
        plt.imshow(B)
        plt.colorbar()

        plt.subplot(3,2,2)
        plt.imshow(H)
        plt.colorbar()

        plt.subplot(3,2,3)
        plt.imshow(ubar0)
        plt.colorbar()

        plt.subplot(3,2,4)
        plt.imshow(ubar1)
        plt.colorbar()

        plt.subplot(3,2,5)
        plt.imshow(udef0)
        plt.colorbar()

        plt.subplot(3,2,6)
        plt.imshow(udef1)
        plt.colorbar()

        plt.show()

    model.U.assign(model.U*0.)

data = np.array(data)
print(data.shape)
np.save('project/solution_data/data.npy', data)