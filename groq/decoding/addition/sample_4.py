import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1.0, 2.0, 3.0, 4.0]
vec2 = [5.0, 6.0, 7.0, 8.0]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted addition operation
encrypted_sum = encrypted_vec1 + encrypted_vec2

# Decrypt the result
decrypted_sum = encrypted_sum.decrypt()

# Compute the final result
final_result = sum(decrypted_sum)

# Print the final result
print(final_result)
