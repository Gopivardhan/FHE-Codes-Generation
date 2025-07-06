
import tenseal as ts

# Create a CKKS context
context = ts CKKSContext(
    poly_modulus_degree=4096,
    coeff_modulus=[8192, 8192],
    scale=2**40
)

# Create a CKKS vector
a = ts.ckks_vector(context, 10)
a.set_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

b = ts.ckks_vector(context, 10)
b.set_values([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Encrypt the vectors
a_enc = a.encrypt()
b_enc = b.encrypt()

# Perform CKKS dot product
dot_product = a_enc.dot(b_enc)

# Decrypt the result
dot_product_dec = dot_product.decrypt()

print(dot_product_dec)
