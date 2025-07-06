import tenseal as ts
import numpy as np

# Set up the context
context = ts.context(ts.MKLSEALContextBuilder().build(
    scale=2**15,
    poly_modulus_degree=4096,
    coefficient_modulus=[
        2**15, (1 << 10) + 2,
        (1 << 11) + 2, (1 << 12) + 2,
        (1 << 13) + 2, (1 << 14) + 2,
        (1 << 15) + 2
    ],
    mode=ts.ContextMode.GPU
))

# Encrypt the input
input_vector = ts.ckks_vector(context, np.random.rand(16, 16).astype(np.float32))
encrypted_input = input_vector.encrypt()

# Define the convolution kernel
kernel_vector = ts.ckks_vector(context, np.random.rand(3, 3).astype(np.float32))
kernel_vector.encrypt()

# Perform the convolution
output_vector = ts.ckks_vector(context, np.zeros((14, 14)).astype(np.float32))
for i in range(14):
    for j in range(14):
        for k in range(3):
            for l in range(3):
                output_vector[i, j] += encrypted_input[i + k, j + l] * kernel_vector[k, l]

# Decrypt the output
decrypted_output = output_vector.decrypt()

# Print the result
print(decrypted_output)