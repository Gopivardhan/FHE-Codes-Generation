
import tenseal as ts

# Create CKKS context
context = ts.context(scheme=ts.Scheme.BFV, poly_modulus_degree=4096, coeff_mod_bit_sizes=[30, 30, 30, 30, 30])
context.generate_galois_keys()
context.generate_public_key()
context.generate_secret_key()

# Create CKKS vectors
v1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
v2 = ts.ckks_vector(context, [5, 4, 3, 2, 1])

# Encrypt vectors
v1_enc = v1.encrypt()
v2_enc = v2.encrypt()

# Perform CKKS dot product
dot_product = v1_enc.dot(v2_enc)

# Decrypt dot product
dot_product_dec = dot_product.decrypt()

# Print dot product
print(dot_product_dec)
