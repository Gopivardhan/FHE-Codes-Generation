
import tenseal as ts
import numpy as np

# Initialize context with 128-bit security level
context = ts.context(ts.SCHEME_TYPE.CKKS, 12, 64)

# Generate key pairs
context.generate_galois_keys()
context.generate_public_key()
context.generate_secret_key()

# Initialize public key
public_key = context.public_key()

# Initialize secret key
secret_key = context.secret_key()

# Initialize vectors
x = np.random.rand(4, 4)
y = np.random.rand(4, 4)

# Encrypt vectors
x_ = ts.ckks_vector(context, x)
y_ = ts.ckks_vector(context, y)

# Perform convolution operation
z_ = x_ * y_

# Decrypt the result
z = z_.decrypt(secret_key)

# Print the result
print(z)
