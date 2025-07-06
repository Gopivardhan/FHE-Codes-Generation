import tenseal as ts
import numpy as np

# Initialize the context
context = ts.context(
    ts.dpnsv=1024, 
    poly_modulus_degree=4096, 
    scale=2**23
)

# Re-compile the context
context.compile()

# Create a CKKS vector
x = ts.ckks_vector.from_py(np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), context)

# Create another CKKS vector
y = ts.ckks_vector.from_py(np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), context)

# Convolution operation
z = ts.convolve(x, y, context)

# Decrypt the result
z = z.decrypt()

# Print the result
print(z)