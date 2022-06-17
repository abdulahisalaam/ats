def fibn(n):
    if n == 1:
        return n
    return fibn(n + 1)
print(fibn(5))