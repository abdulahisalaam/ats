def loop():
    l=[1,2,3]
    for num in l:
        yield num
a =loop()

z = next(iter(a))
y = next(iter(a))
print(type(iter(a)))
print(z)
print(y)
