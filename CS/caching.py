def fib(n):
    return fib_c(n, {})


def fib_c(n, cache):
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_c(n-1, cache)+fib_c(n-2, cache)
    return cache[n]
