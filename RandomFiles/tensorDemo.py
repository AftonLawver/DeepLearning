# In pytorch, everything is done in a tensor
# You might be familiar with numpy arrays, which are basically the same thing.
# we can convert between the two.
# A tensor can have multiple dimensions, or just 1.

# Note that a single number is often referred to as a scalar. (Zero - dimensional tensor)

# Most commonly, a tensor with one dimension is referred to as a vector.
# A tensor with two dimensions is called a matrix.
# A tensor with three dimensions is called a cuboid.
# The number of dimensions a tensor has is called its rank.
# Ranks
# 0 - Scalar
# 1 - Vector
# 2 - Matrix
# 3 - High Dimension Tensor


import torch

# create a 2d tensor
# torch.empty creates a tensor of size x, y and fills it will uninitialized data.
# uninitialized = values that were already in the memory block before.
x = torch.empty(2,3)
print(x)

# create a 2d tensor that contains random values
y = torch.rand(2,3)
print(y)

# create a tensor that is filled with zeros
z = torch.zeros(2,2)
print(z)

a = torch.ones(2,2)
print(a)

b = torch.rand(2,2)
c = torch.rand(2,2)
print("\nTENSOR B\n")
print(b)
print("\nTENSOR C\n")
print(c)

d = torch.add(b,c)
# d = b + c
print("\nTENSOR D AFTER FIRST ADDITION.\n")
print(d)

# can do an inplace addition as well
# every function that has an underscore after it is an inplace operation
print("\nTENSOR D AFTER SECOND ADDITION.\n")
d.add_(b)
print(d)

# can also use subtraction, multiplication, and division operations the same way.

# can do slicing operations on tensors
# get first row
my_tensor = torch.rand(5,3)
print("\nMY TENSOR BEFORE SLICE")

print(my_tensor)
print("\nMY TENSOR AFTER SLICE: 1ST ROW")
print(my_tensor[:, 0])

# get the actual value of the tensor element by using .item()
print(my_tensor[0:1, 0:1].item())














