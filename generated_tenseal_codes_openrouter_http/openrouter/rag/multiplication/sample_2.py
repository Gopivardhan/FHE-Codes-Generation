Here is the Python code for CKKS multiplication:

```
import tenseal as ts

# Create CKKS context
context = ts.CKKSContext()
context.generate_galois_keys(8192)

# Create CKKS plaintext
plaintext = ts.ckks_vector(context, [1, 2, 3, 4, 5])

# Create another CKKS plaintext
plaintext2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform CKKS multiplication
result = plaintext * plaintext2

# Decrypt
decrypted = result.decrypt()

# Print result
print(decrypted)
```