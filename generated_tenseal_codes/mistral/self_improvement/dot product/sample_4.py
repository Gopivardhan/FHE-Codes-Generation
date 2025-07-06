```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 2)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

result = encrypted_vector1 * encrypted_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.scale)
print(decrypted_result.value)
```
Note: The scale of the result will depend on the scales of the input vectors. In this example, the scale of the result will be 2^120 (since the scales of the input vectors are both 2^60). The value printed will be the dot product of the input vectors divided by their product scale (i.e., 325 / 2^120).