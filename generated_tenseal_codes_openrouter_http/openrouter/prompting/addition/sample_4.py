
import tenseal as ts
context = ts.context(ts.dpn_noisy_stddev(0.5), poly_modulus_degree=4096, coeff_modulus=[2**64])
context.set_relaxation_parameters()
context.generate_galois_keys()
context.generate_public_key()
public_key = context.gal_key
context.global_scale = 2**63

# Define plaintext values
a = 5
b = 3

# Encrypt plaintext values
a_enc = ts.ckks_vector(context, [a])
b_enc = ts.ckks_vector(context, [b])

# Perform CKKS addition
result_enc = a_enc + b_enc

# Decrypt result
result_dec = result_enc.decrypt()

# Print the result
print(result_dec[0])
