
import tenseal as ts

# Generate a CKKS context
context = ts.CKKS(
    poly_modulus_degree=8192,
    security_level=3,
    scheme=ts.SCHEME_TYPE.BFV,
    mode=ts.MODE.GALois,
    eval_depth=3,
    parms_seed=123
)

# Encrypt a vector
encrypted_vector = ts.ckks_vector(context, [1, 2, 3, 4, 5])

# Encrypt another vector
encrypted_vector2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform CKKS convolution
encrypted_result = encrypted_vector.convolution(encrypted_vector2)

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)