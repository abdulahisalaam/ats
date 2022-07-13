import math
num = int(input("Enter the number of terms: "))
eu_sum = 0
for i in range(1, (num + 1)):
    euler_sum = eu_sum + 1/math.factorial(i)

print("The sum of series is ", euler_sum)