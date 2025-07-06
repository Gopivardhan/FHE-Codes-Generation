```
import tenseal as ts

# Create a CKKS context
context = ts.context(ts.SCHEME_TYPE.CKKS, 12, 320)

# Create a CKKS vector
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform CKKS multiplication
result = vec1 * vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
```