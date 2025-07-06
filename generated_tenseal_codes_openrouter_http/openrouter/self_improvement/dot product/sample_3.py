```python
import tenseal as ts

# Initialize the CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    number_of_slots=256,
    scale=1 << 30,
    precision=30,
    eval_depth=3,
    seed=0
)
context.global_setup()
context.keygen()

# Define two vectors
v1 = [1, 2, 3, 4, 5]
v2 = [6, 7, 8, 9, 10]

# Encrypt the vectors
encrypted_v1 = ts.ckks_vector(context, v1)
encrypted_v2 = ts.ckks_vector(context, v2)

# Perform the dot product operation
encrypted_result = encrypted_v1 * encrypted_v2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)
```