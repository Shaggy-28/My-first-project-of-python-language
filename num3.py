# checking array dimesnion
import numpy as np

arr_1 = np.array([1,2,3])
arr_2 = np.array([[1,2,3],[3,4,5]])
arr_3 = np.array([[[1,2,3],[3,4,5],[3,4,5]]])
print(arr_1.ndim)
print(arr_2.ndim)
print(arr_3.ndim)