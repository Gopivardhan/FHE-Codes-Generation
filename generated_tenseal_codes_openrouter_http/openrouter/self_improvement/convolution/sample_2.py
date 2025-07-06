```
import tenseal as ts

# Initialize CKKS context
context = ts CKKSContext(scheme=ts.SCHEME_TYPECKKS, poly_modulus_degree=4096, scale=2**(-24))

# Load the context
context.global_scale = 2**24

# Create a CKKS vector
a = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = ts.ckks_vector(context, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Perform convolution
result = a.convolve(b)

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
```