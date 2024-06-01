import numpy as np

a1 = np.arange(6).reshape(2, 3)
print(a1)
# [[0 1 2]
#  [3 4 5]]

a2 = np.arange(6, 18, 2).reshape(2, 3)
print(a2)
# [[ 6  8 10]
#  [12 14 16]]

print(a1 * a2)
# [[ 0  8 20]
#  [36 56 80]]
