
granted = False
def grant():
    global granted
    granted = True

def login(name,password):
    file = open("login_details.txt","r")
    success = False
    for dat in file:
        a,b = dat.split(",")
        b = b.strip()
        if(a==name and b==password):
            success= True
            break
    file.close()
    if success:
        print(f"You have login successful {name}")
        grant()
    else:
        print("Wrong username or password!")

def register_user(name,password):
    file = open("login_details.txt","a")
    file.write("\n"+name+", "+password)
    file.close()
    grant()

def authenticate(option):
    if option=="login":
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name & password to register: ")
        name=input("Enter your name: ")
        password=input("Enter your password: ")
        register_user(name,password)


def start_function():
    global option
    print("*** Welcome Afex Tech Stars ***")
    option= input("Do you want to Login or Register (login, reg) :  ")

    if(option != "login" and option != "reg"):
        start_function()

start_function()
authenticate(option)
if(granted):
    print("*** Welcome to Afex Tech Stars ***")
    print(f"Congratulation !!!")

