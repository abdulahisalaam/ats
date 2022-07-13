#num = [1,2,3,4,5]
#for n in num:
#   print(n)

number=[1,2,3,4,5,6,7,8]
for i in number:
    if i % 2 == 0:
        print(i)

print('-------------------------------------------------')
index = 0
while index<len(number):
    if number[index]%2 == 0:
        print(number[index])
    index= index + 1

for x in list(range(10)):
    print(x)

def multiply(a,b):
    print(a*b)

print('-------------------------------------------------')
multiply(2,4)

print('-------------------------------------------------')
def square(x):
    return x**2

print('-------------- Square --------------')
square(4)