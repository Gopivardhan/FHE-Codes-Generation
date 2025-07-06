```
import tenseal as ts

# Create CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096, 
    coeff_modulus=[2**15, 2**16, 2**17], 
    scale=2**(-16), 
    secret_key=[ts.CKKSKey(2**15, 2**16, 2**17), ts.CKKSKey(2**15, 2**16, 2**17)], 
    relay_degree=12, 
    mode=ts.CKKSContext.FHE_MODE_GSW

# Create CKKS vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform CKKS matrix multiplication
result = vec1 * vec2

# Decrypt result
decrypted_result = result.decrypt()

# Print result
print(decrypted_result)
```