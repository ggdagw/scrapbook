import numpy as np

# Define a simple class
class Params:
   def __init__(self,d=10):
      self.d = d
# and an instance of that class
myparams = Params()

array_1 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)
array_2 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)
a = 4
b = 3
c = 9

def compute_np(array_1, array_2, a, b, c):
   return np.clip(array_1, 2, 10) * a + array_2 * b + c

compute_np(array_1, array_2, a, b, c)

import compute_typed
# pass the instance of the class to our cythonised function
compute_typed.compute(array_1, array_2, myparams, a, b, c)
