import tenseal as ts
import numpy as np

context = ts.context(ts.SEAL_DEFAULT_PARAMETERS)
key_generator = ts.CKKSKeyGenerator(context)
encoder = ts.CKKSEncoder(context)

public_key = key_generator.public_key()
secret_key = key_generator.secret_key()
relin_keys = [key_generator.create_relin_keys() for _ in range(context.depth()//2)]

x = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
y = np.array([5.0, 6.0, 7.0, 8.0], dtype=np.float32)

x_encrypted = encoder.encode(x, public_key)
y_encrypted = encoder.encode(y, public_key)

x_encrypted.scale()
y_encrypted.scale()

x_encrypted += y_encrypted

x_encrypted.relinearize(relin_keys)
x_encrypted.rescale()

decrypted_result = encoder.decode(x_encrypted, secret_key)

print(np.array(decrypted_result, dtype=np.float32))