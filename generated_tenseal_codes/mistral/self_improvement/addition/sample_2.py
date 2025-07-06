```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 2)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

result = encrypted_vector1 + encrypted_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.tolist())
```
Note: The above code assumes that the `tenseal` library is already installed and imported. The `tolist()` method is used to convert the `ComplexVector` object returned by the `decrypt()` method to a Python list. The size of the vectors and the parameters used to create the context are just examples and can be adjusted according to the specific requirements of the task.