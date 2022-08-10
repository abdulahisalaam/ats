
# def prime(number):
#     flag = False
#     for num in range(2,number):
#         if number % num == 0:
#             flag = True
#             break
#     if flag:
#         return f'{number} is not a Prime Number'
#     else:
#         return f'{number} is a Prime Number'

# print(prime(15))
number = 15
def prime_check(number):
    p = any(n for n in [num for num in range(2,number)] if number % n == 0)
    if p:
        return False
    return True

print(prime_check(35))