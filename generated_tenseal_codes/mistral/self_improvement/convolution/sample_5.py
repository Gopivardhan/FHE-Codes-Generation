```python
import tenseal as ts
import numpy as np

# Set parameters for the CKKS scheme
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, plain_modulus=2**32)

# Create encryption parameters and a client context
encryptor = context.encryptor()

# Generate two random vectors to perform convolution on
vector1 = np.random.rand(128).astype(np.float32)
vector2 = np.random.rand(128).astype(np.float32)

# Encrypt the vectors using the CKKS scheme
encrypted_vector1 = ts.ckks_vector(encryptor, vector1)
encrypted_vector2 = ts.ckks_vector(encryptor, vector2)

# Perform the convolution operation on the encrypted vectors
result = encrypted_vector1 * encrypted_vector2

# Decrypt the result and print it
decryptor = context.decryptor()
decrypted_result = result.decrypt(decryptor)
print(decrypted_result)
```
Note: This code performs element-wise multiplication of two vectors, which is not the same as convolution. To perform convolution using CKKS scheme, you need to perform some additional steps such as zero-padding and circular shifting of one of the vectors. The above code is just an example of how to perform basic operations using TenSEAL library for CKKS scheme.