def fibn(n):
    if n == 1:
        return n
    else:
        return n * fibn(n - 1)
print(fibn(5))