def recursion(x):
    if x == 1:
        return 1
    else:
        return (x * (recursion(x-1)))

x=int(input("Enter a non-negative integer: "))
print(f"The factorial of {x} is {recursion(x)}")