```
import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts-relin=11,
    ts-poly_mod_degree=256,
    ts-mode=ts.CKKS
)

# Generate a 2D vector
a = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
b = ts.ckks_vector(context, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

# Perform matrix multiplication
c = a @ b

# Decrypt the result
decrypted_c = c.decrypt()

# Print the result
print(decrypted_c)
```