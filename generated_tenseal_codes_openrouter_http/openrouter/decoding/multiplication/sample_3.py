
import tenseal as ts

context = ts.context(
    poly_modulus_degree=4096,
    coeff_modulus=[2**24, 2**24+2**23, 2**24+2**22+2**21],
    scale=2**30,
    security_level=3,
    mode=ts.ContextMode.GPU_FPGA

)

context.generate_public_key()
context.generate_secret_key()

vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vector2 = ts.ckks_vector(context, [5, 4, 3, 2, 1])

encrypted_vector1 = vector1.encrypt()
encrypted_vector2 = vector2.encrypt()

encrypted_result = encrypted_vector1 * encrypted_vector2

decrypted_result = encrypted_result.decrypt()

print(decrypted_result)
