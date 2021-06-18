
import numpy as np
array_1 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)
array_2 = np.random.uniform(0, 1000, size=(300, 200)).astype(np.intc)
a = 4
b = 3
c = 9

def compute_np(array_1, array_2, a, b, c):
   return np.clip(array_1, 2, 10) * a + array_2 * b + c

compute_np(array_1, array_2, a, b, c)

import compute_typed
compute_typed.compute(array_1, array_2, a, b, c)
