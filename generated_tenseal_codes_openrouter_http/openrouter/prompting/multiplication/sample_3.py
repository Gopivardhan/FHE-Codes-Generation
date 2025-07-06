
import tenseal as ts

context = ts.context(ts.core.CoreSemiring(), poly_modulus_degree=4096, coefficient_modulus=[2**24, 2**30, 2**36], scale=2**30)
context.set_relaxation_parameters(15, 15, 8)
context.generate_galois_keys()
context.generate_powers_of_two_mods()

A = ts.ckks_vector(context, [1, 2, 3, 4, 5])
B = ts.ckks_vector(context, [6, 7, 8, 9, 10])

A_enc = A.encrypted()
B_enc = B.encrypted()

C_enc = A_enc * B_enc

C_dec = C_enc.decrypt()

print(C_dec)
