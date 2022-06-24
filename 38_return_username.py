def firstname():
    return input("Enter Your firstname: ").lower()
def lastname():
    return input("Entr your lastname: ").lower()

def suggest_username():
    a = firstname()[0:3]
    b = lastname()[0:3]
    return a+b

print(suggest_username().title())