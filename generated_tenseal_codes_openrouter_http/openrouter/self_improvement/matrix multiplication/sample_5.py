```
import tenseal as ts

# Initialize CKKS context
context = ts.context(scheme=ts.Scheme.FHE,
                     poly_modulus_degree=4096,
                     coeff_mod_bit_sizes=[30, 30, 30, 30, 30])

# Generate and set the keys
context.generate_galois_keys()
context.generate_public_evaluation_key()
context.generate_secret_key()

# Initialize CKKS vectors
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Encrypt the vectors
a_enc = a.encrypted_vector()
b_enc = b.encrypted_vector()

# Perform matrix multiplication
c_enc = a_enc * b_enc

# Decrypt the result
c = c_enc.decrypt()

# Print the result
print(c)