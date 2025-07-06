
import tenseal as ts

# Create a CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    coeff_modulus=[
        2**61 - 1,
        (2**32) * (2**61 - 1),
        (2**64) * (2**61 - 1)
    ],
    scale=2**30
)

# Create a CKKS vector
vector = ts.ckks_vector(context, [1, 2, 3, 4, 5])

# Create another CKKS vector
vector2 = ts.ckks_vector(context, [5, 4, 3, 2, 1])

# Perform CKKS addition
result = vector + vector2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
