# UVa 1230 - MODEX
# UVa 374 - Big Mod


def binpow(a, b, m):
    a %= m
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res


if __name__ == "__main__":
    print(binpow(2, 3, 5))
    print(binpow(2, 2147483647, 13))
    print(binpow(2374859, 3029382, 36123))
