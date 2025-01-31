import numpy as np
from scipy.integrate import odeint as solver
from BC.BC_Utilities import *

from BC.case_test import case_test as case
from plant.model import model as model
from postprocess.plot import plot as postprocess

[BC, Parameters] = case()

# Number of data points
n = int(Parameters['tf']/Parameters['ts'])

# time points
t = np.linspace(0,Parameters['tf'],n)
# resample BCs
y_BC = resample_dict(BC,t)
# store solution
Tcontents_degR = np.empty_like(t)
Tair_degR= np.empty_like(t)

# initial conditions
z0 = [Parameters['IC']['Tcontents0_degR'], Parameters['IC']['Tair0_degR']]
# record initial conditions
Tcontents_degR[0] = z0[0]
Tair_degR[0] = z0[1]


# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = solver(model,z0,tspan,args=(y_BC,i,Parameters,), full_output=False, printmessg=True)
    # store solution for plotting
    Tcontents_degR[i] = z[1][0]
    Tair_degR[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
postprocess(t, y_BC, Tcontents_degR, Tair_degR)