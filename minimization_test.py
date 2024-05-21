import firedrake as fd
import numpy as np
import matplotlib.pyplot as plt
from model import SpecFO

nx=100 
ny=100
dx=100e3
dy=100e3

model = SpecFO(nx, ny, dx, dy)
B, H = model.get_geometry()
model.set_field(model.B, B)
model.set_field(model.H, H)

ubar_x = fd.File('project/output/ubar_x.pvd')
ubar_y = fd.File('project/output/ubar_y.pvd')
for i in range(25000):

    fd.assemble(model.R, tensor=model.dU)
    if i % 100 == 0:
        print(i, (model.dU.dat.data[0]**2).sum())
        ubar_x.write(model.U.sub(0), idx=i)
        ubar_y.write(model.U.sub(1), idx=i)

    model.U.assign(model.U + 1e-12*model.dU)