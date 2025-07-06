
import tenseal as ts

# Initialize context
context = ts.context(
    scale=2**15,
    poly_mod_degree=257,
    precision=40,
    modes=[ts.LOose]
)

# Encrypt vectors
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform matrix multiplication
result = a.dot(b)

# Decrypt result
decrypted_result = result.decrypt()

# Print result
print(decrypted_result)
