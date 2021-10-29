from scipy.integrate import quad
import numpy as np
def f(x):
  return np.exp(-1*x) * np.sin(3*x)
r,e=quad(f,0,2*np.pi)
print(r)