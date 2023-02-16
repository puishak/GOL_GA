# installing bifrost:
#   pip install git+https://github.com/Distributive/Bifrost


# DCP MODULE
from bifrost import dcp

##################
# INPUT SET
##################
b_set = range(12)
##################
# WORK FUNCTION
##################
"Compute left Riemann sum of exp(-x^2) from 0 to b with N subintervals."
def riemann_sum(b,N=100000):

  # packages required inside the work function must be imported inside the work function
  import numpy as np

  x = np.linspace(0,b,N+1)
  x_left_endpoints = x[:-1]
  Delta_x = b/N
  I = Delta_x * np.sum(np.exp(-x_left_endpoints**2))

  return I

##################
# JOB & CONFIG
##################
job = dcp.compute_for(b_set, riemann_sum)
job.requires('numpy')
job.compute_groups = [{'joinKey': 'demo', 'joinSecret': 'dcp'}]
job.public['name'] = "Numpy Riemann Sums Job, on DCP!"

##################
# EXEC
##################
results = job.exec()


print(results)

