from firedrake import *
from firedrake_adjoint import *

# Define the mesh and function space
mesh = UnitSquareMesh(10, 10)
V = FunctionSpace(mesh, "CG", 1)

# Define the source function f
f = Function(V)
f.assign(Constant(1.0))

# Define the boundary condition
bc = DirichletBC(V, Constant(0), "on_boundary")

# Define the trial and test functions
u = TrialFunction(V)
v = TestFunction(V)

# Define the Poisson problem
a = dot(grad(u), grad(v)) * dx
L = f * v * dx

# Solve the Poisson problem
u = Function(V)
solve(a == L, u, bcs=bc)

# Define a functional for which we want to compute the derivative
# Here we choose J = 0.5 * ||u||^2
J = assemble(0.5 * dot(grad(u), grad(u)) * dx)

# Compute the derivative dJ/df
dJ_df = compute_gradient(J, Control(f))

# Output the derivative
print(dJ_df.dat.data)