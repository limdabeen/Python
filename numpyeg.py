import numpy as np

array_4x3 = np.random.rand(4, 3)
print(array_4x3)

array_5x5 = np.arange(25).reshape(5, 5)
print(array_5x5)

arrays_2_4x4 = np.arange(32).reshape(2, 4, 4)
print(arrays_2_4x4)

identity_array = np.eye(10)
print(identity_array)