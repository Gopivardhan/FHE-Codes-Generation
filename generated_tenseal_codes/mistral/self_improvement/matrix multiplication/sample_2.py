```python
import tenseal as ts

# Set the context parameters for CKKS scheme
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 10, 1, 2)

# Create encryption parameters and a key encapsulation key
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

# Encrypt two matrices A and B as CKKS vectors
A_encrypted = [encryptor.encrypt(value) for value in A.flatten()]
B_encrypted = [encryptor.encrypt(value) for value in B.flatten()]

# Create CKKS vectors from the encrypted matrices
A_ckks = ts.ckks_vector(context, A_encrypted)
B_ckks = ts.ckks_vector(context, B_encrypted)

# Perform matrix multiplication using CKKS scheme
C_ckks = A_ckks * B_ckks

# Decrypt the result and convert it back to a numpy array
C_decrypted = decryptor.decrypt_batch(C_ckks.get_values())
C = np.reshape(C_decrypted, (A.shape[0], B.shape[1]))

# Print the result
print(C)
```
Note: Replace `A` and `B` with your actual matrices, and make sure their dimensions are compatible for matrix multiplication. Also, import numpy as np if you haven't already.