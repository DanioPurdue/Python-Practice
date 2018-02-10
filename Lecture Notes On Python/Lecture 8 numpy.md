# numpy

```python
import numpy as np
x = np.empty([3,2], dtype = int) #initialize regardless of the content

x = np.zeros(5) #1d array of 5 elements
	np.range(start, stop, step, dtype)
x = np.arange(10, 20,2, dtype = float)
ndarray.ndim
ndarray.shape

#3d reshape
a = np.arange(24)
b = a.reshape(2,4,3)
a[range[2,7,2]] # a[[2, 4, 6]]
a[1, 2] #two dimensions

```

## Ellipsis

access columns

```python
a[..., 1] #the items in the second columns
```

boolean indexing

```python
bools = x >5#boolean mask
x[bools]
```

operations:

elements wise operations are normal operators

np.dot(a * b) will perform the matrix multiplication



matrix operation

```python
a.sum()
a.min()

a.sum(axis=0)#do the summuation along the columns
a.min(axis=1)#do the min among the rows
a.cumsum(axis=1)
```

