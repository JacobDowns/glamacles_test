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

B_out = fd.File('project/output/B.pvd')
B_out.write(model.B)

H_out = fd.File('project/output/H.pvd')
H_out.write(model.H)

V_cg = fd.VectorFunctionSpace(model.mesh, 'CG', 1, dim=2)
ubar = fd.Function(V_cg)
udef = fd.Function(V_cg)

model.solver.solve()

ubar.interpolate(fd.as_vector([model.U.sub(0), model.U.sub(1)]))
udef.interpolate(fd.as_vector([model.U.sub(2), model.U.sub(3)]))

ubar_out = fd.File('project/output/ubar.pvd')
ubar_out.write(ubar)

udef_out = fd.File('project/output/udef.pvd')
udef_out.write(udef)