
import tenseal as ts

context = ts.context(scheme=ts.scheme_ckks, poly_mod_degree=4096, scale=2**22)
context.global_scale = 2**22
context.generate_galois_keys()

pt1 = ts.ckks_vector(context, 10)
pt1.set_value([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

pt2 = ts.ckks_vector(context, 10)
pt2.set_value([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

pt1 = pt1.encrypt()
pt2 = pt2.encrypt()

pt3 = pt1 * pt2
pt3 = pt3.decrypt()

print(pt3.get_value())
