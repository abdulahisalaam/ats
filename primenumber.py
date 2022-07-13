numbers = [1 for n in range(1,1000)]
# To take input from the user


for key,value in enumerate(numbers):
    for p in range(2,key):
        if key % p == 0:
            numbers[key] = 0
            break
        elif key % p != 0:
            numbers[key] = 1
print(numbers) 