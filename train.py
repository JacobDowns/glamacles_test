import firedrake as fd
import numpy as np
import matplotlib.pyplot as plt
from model import SpecFO
import torch
from torch.utils.data import TensorDataset, DataLoader

"""
Generate randomized synthetic ice sheets and solve for velocity.
"""

data = np.load('project/solution_data/data.npy')

nx=100 
ny=100
dx=100e3
dy=100e3

model = SpecFO(nx, ny, dx, dy)

X = torch.tensor(data, dtype=torch.float32).cuda()
dataset = TensorDataset(X[:,[0,1],:,:], X[:,2:,:,:])
data_loader = DataLoader(dataset, batch_size=1, shuffle=True)