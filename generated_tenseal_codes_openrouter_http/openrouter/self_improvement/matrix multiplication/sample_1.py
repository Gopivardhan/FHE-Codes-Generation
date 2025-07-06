```
import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    polymer_degree=15,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30],
    scale=2**30,
    sec_level=3
)

# Create vectors
vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vector2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform multiplication
result = vector1 * vector2

# Decrypt and print the result
print(result.decrypt())
```