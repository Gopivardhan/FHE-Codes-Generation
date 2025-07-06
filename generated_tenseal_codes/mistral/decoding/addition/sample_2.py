import tenseal as ts

context = ts.context(ts.SEAL_CPU, True, 60)
key_generator = ts.CKKSKeyGenerator(context)
encoder = ts.CKKSEncoder(context)

public_key = key_generator.public_key()
relin_keys = [key_generator.relin_keys() for _ in range(context.depth()//2)]
private_key = key_generator.secret_key()

x = [1.0, 2.0, 3.0, 4.0]
y = [5.0, 6.0, 7.0, 8.0]

x_encrypted = encoder.encode(x, public_key)
y_encrypted = encoder.encode(y, public_key)

x_encrypted += y_encrypted

x_decrypted = encoder.decode(x_encrypted, private_key)

print(x_decrypted)