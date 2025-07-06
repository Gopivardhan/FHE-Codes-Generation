import tenseal as ts

context = ts.context(128, 60, 30)

matrix_a = ts.ckks_matrix(3, 3, context)
matrix_b = ts.ckks_matrix(3, 3, context)

# Assuming matrix_a and matrix_b are initialized with some values

result = ts.ckks_matrix(3, 3, context)

ts.matrix_multiply(result, matrix_a, matrix_b)

# The result matrix now contains the product of matrix_a and matrix_b in encrypted form.