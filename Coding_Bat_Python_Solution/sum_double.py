def sum_double(a, b):
    if a == b:
        double = a+b
        return 2*double
    if a != b:
        return a + b


print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))


def sum_double2(a, b):
    if a == b:
        return 2*(a+b)
    if a != b:
        return a + b


print(sum_double2(1, 2))
print(sum_double2(3, 2))
print(sum_double2(2, 2))