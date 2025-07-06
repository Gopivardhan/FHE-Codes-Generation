```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 10)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

# Encrypt input vectors
vector_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector_2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encrypted_vector_1 = encryptor.encrypt(vector_1)
encrypted_vector_2 = encryptor.encrypt(vector_2)

# Perform convolution
convolution_result = ts.convolve(encrypted_vector_1, encrypted_vector_2)

# Decrypt and print the result
decrypted_result = decryptor.decrypt(convolution_result)
print(decrypted_result)
```
Note: This code assumes that the length of the input vectors is equal to the size of the CKKS polynomial modulus ring (in this case, 8192). If the length of the input vectors is less than the size of the modulus ring, you can pad the vectors with zeros before encrypting them. Also, the `convolve` function performs circular convolution, so the output vector length will be equal to the length of the input vectors. If you want to perform linear convolution, you will need to pad the input vectors with zeros to ensure that the output vector length is correct.