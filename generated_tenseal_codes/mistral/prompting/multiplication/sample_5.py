import tenseal as ts

context = ts.context(128, 10, 30, ts.SEAL_CACHE_TO_MEMORY, False)
encoder = ts.CKKSEncoder(context)

vector1 = ts.ckks_vector(context)
vector2 = ts.ckks_vector(context)

# Assume you have some float values assigned to input1 and input2
encoder.encode(input1, vector1)
encoder.encode(input2, vector2)

result = vector1 * vector2

# The result is a scaled product, you may want to rescale it
result.scale()

decoded_result = result.decode(encoder)