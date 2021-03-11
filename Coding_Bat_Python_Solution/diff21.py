def diff21(n):
    if n <= 21:
        return 21 - n
    else:
        return (n - 21) * 2


print(diff21(19))
print(diff21(10))
print(diff21(21))


def diff21(n):
    if (n < 21) or (n == 21):
        return 21 - n
    else:
        return (n - 21) * 2
