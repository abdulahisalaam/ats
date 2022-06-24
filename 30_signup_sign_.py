import csv

def firstname():
    return input("What is your Firstname? : ")
def password():
    return input("Enter your password : ")
  
def confirm_password():
    return input("Confirm your password? : ")

def email():
    return input("Enter your email : ")

def write_data(**kwargs):
    header = ['firstname','password','email']
    with open("mydata02.csv", "w+", newline='\n') as d:
        handler = csv.DictWriter(d, fieldnames=header)
        handler.writerow(kwargs)


def validate_firstname(firstname):
    if not firstname.isalpha():
        print('Name must be an Alphabet!!!')
        return False
    return True


def validate_password(password):
    if  len(password) <= 6:
        print("print invalid password, it must contain at least 7 characters")
        return False
    return True


def validate_confirm_password(confirm_password,password):
    if not confirm_password == password:
        print("password mismatched !!!")
        return False
    return True
    

def validate_email(email):
    if not email.endswith('.com') and not'@' in data['email']:
        print('invalid email address!!!')
        return False
    return True    
    

def signup():

    global firstname
    global password 
    global confirm_password 
    global email 

    firstname = firstname()
    password = password()
    confirm_password = confirm_password()
    email = email()

    if not validate_firstname(firstname):
        print("Name must contain alphabets!!!")
        return False


    if not validate_password(password):
        print("password must be more than 6 character!!!")
        return False


    if not validate_confirm_password(confirm_password, password):
        print("password mismatch !!!!")
        return True 

    if not validate_email(email):
        print("Email must be in this format example@mail.com!!!")
        return True

    write_data(firstname=firstname,password=password,email=email)
    

def return_data():
    with open('mydata02.csv', 'r') as f:
        handler = csv.DictReader(f)
        return list(handler)

def login():
    password = password()
    email = email()
    data = return_data()
    for i in data:
        if i['password']== password and i['email']== email:
            print("Successfull Login !!!")
    

def body():
    print('welcome <------------>')
    print("Please Enter Option \n 1. SignUp Account-> \n 2. SignIn Account->\n")
    option = input("")
    if option == '1':
        signup()
    elif option == '2':
        login()
    else:
        body()

if __name__ == '__main__':
    body()
    