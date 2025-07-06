import tenseal as ts

# Setup TenSEAL context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2**40

# Signal (input vector) and kernel (filter)
signal = [1, 2, 3, 4, 5]
kernel = [1, 0, -1]  # Like a Sobel edge filter

# Encrypt kernel once
enc_kernel = ts.ckks_vector(context, kernel)

# Apply convolution using dot product over sliding windows
output = []
for i in range(len(signal) - len(kernel) + 1):
    window = ts.ckks_vector(context, signal[i:i+len(kernel)])
    res = window.dot(enc_kernel)
    output.append(res.decrypt()[0])  # Each dot product gives 1 value

print("Encrypted 1D Convolution Output:", output)
