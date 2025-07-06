
import tenseal as ts

# Create a CKKS context
context = ts.context(
    scheme=ts.Scheme.CKKS,
    poly_modulus_degree=8192,
    poly_modulus=ts.MPI(4096),
    coeff_modulus=[ts.MPI(2000) for _ in range(8)],
    security_level=128
)

# Initialize the context
context.relinearization_parameters().setup(context)

# Create two vectors
vector1 = ts.ckks_vector(context, [1, 2, 3, 4])
vector2 = ts.ckks_vector(context, [5, 6, 7, 8])

# Perform the convolution
result = ts.ckks_convolution(context, vector1, vector2)

# Decrypt the result
decrypted_result = result.decrypt().to_python()

# Print the result
print(decrypted_result)
