import tenseal as ts

context = ts.context(128, 60, [30, 40, 50], ts.SEAL_PLAINTEXT_MODULUS)
encoder = ts.CKKSEncoder(context)

vector1 = [1.0, 2.0, 3.0]
vector2 = [4.0, 5.0, 6.0]

input_scale = 2**(-50)
enc_vector1 = encoder.encode(vector1, input_scale)
enc_vector2 = encoder.encode(vector2, input_scale)

vector1_ckks = ts.ckks_vector(context, enc_vector1)
vector2_ckks = ts.ckks_vector(context, enc_vector2)

result = vector1_ckks * vector2_ckks
decoder = ts.CKKSDecoder(context)
decoded_result = decoder.decode(result)

print(decoded_result[0])