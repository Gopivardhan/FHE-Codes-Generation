```
import tenseal as ts

context = ts.context(ts.CKKS, 2**20, 2**20, 32)
context.generate_galois_keys()

a = ts.ckks_vector.from_py([1, 2, 3, 4], context)
b = ts.ckks_vector.from_py([5, 6, 7, 8], context)

c = a * b

decrypted_c = c.decrypt()

print(decrypted_c)
```