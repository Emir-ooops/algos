import numpy as np
from numpy.linalg import inv
A = np.matrix('1 -3; 2 5')
A_inv = np.linalg.inv(A)
print(A_inv)