import csv
import time

def username():
    return input("What is your username? : ")
def password():
    return input("Enter your password : ")
def phone_no():
    return input("Enter your phone No.: ")
def marital_s():
    return input("Enter Single or Married: ")
def age():
    return input('How old are you? :')
def gender():
    return input('Enter Male or Female: ')
def confirm_password():
    return input("Confirm your password? : ")

def email():
    return input("Enter your email : ")

def write_data(**kwargs):
    header = ['username','password','email','age','marital_s','gender','phone_no']
    #username,password,email,age,marital_s,gender,=phone_no
    with open("sigin_signup.csv", "a") as d:
        handler = csv.DictWriter(d, fieldnames=header)
        if len(return_data()) == 0:
            handler.writeheader()
            handler.writerow(kwargs)
        else:
            handler.writerow(kwargs)


def validate_username(username):
    if not username.isalpha():
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
    #check = [ck for ck in email if not '@' in email and not email.endswith('.com') ]
    #return check
    if not email().endswith('.com') and not'@' in email():
        print('invalid email address!!!')
        return False
    return True    
    

def signup():
    username = input('Enter your name: ')
    password = input('Enter your password: ')
    confirm_password= input("Confirm your password: ")
    email = input("Enter Your Email: ")
    age = input("Enter Your : ")
    marital_s = input("Enter Single or Married: ")
    phone_no = input("Enter Your Phone No.: ")
    gender = input("Enter Your Gender Male or Female: ")


    if not validate_username(username):
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

    write_data(username=username,password=password,email=email,age=age,marital_s=marital_s,gender=gender,phone_no=phone_no)

    print("Congratulation You Have Successfully SignUp")
    time.sleep(3)
    option=input('1.To SignIn Page')
    if option == '1':
        print("Pls Continue to SignIn")
        login()
    else:
        signup()
    

def return_data():
    with open('sigin_signup.csv', 'r') as f:
        data = csv.DictReader(f)
        return list(data)
def pick_option():
    data = return_data()
    a =[account for account in data if account['password']== password and account['email']== email] 
    print('\n')
    current_password = a[0]['password']
    passcode = input("Enter Password To Update Profile")
    if current_password == passcode:
        print('Choose Modify Option:')
        option= input('\n\t1.Username->\n\t2.Password->\n\t 3.Email->\n\t 4.Age->\n\t 5.Marital Status->\n\t 6.Gender->\n\t7.Phone No.->')
        if option == '1':
            a[0]['username'] = username()
            return a[0]['username']
        elif option == '2':
            a[0]['password']= password()
            return a[0]['password']
        elif option == '3':
            a[0]['email']= email()
            return a[0]['email']
        elif option == '4':
            a[0]['age'] = age()
            return a[0]['age']
        elif option == '5':
            a[0]['marital_s'] = marital_s()
            return a[0]['marital_s']
        elif option == '6':
            a[0]['gender'] = gender()
            return a[0]['gender']
        elif option == '7':
            a[0]['phone_no'] = phone_no()
            return a[0]['phone_no']


def login():
    data = return_data()
    email = input('Enter Email: ')
    password = input('Enter Password: ')

    data = return_data()
    a =[account for account in data if account['password']== password and account['email']== email] 
    print("Successfull Login {}, You Are Welcome!!!".format(a[0]['username']))
    # print('\n')
    #pick_option()

def modify(option):
    data = return_data()
    a =[account for account in data if account['password']== password and account['email']== email]
    # print(a[0][f'{key}'])
    
def body():
    print('welcome <------------------------>')
    print("Please Enter Option [1 to 2]: \n\t 1. SignUp Account-> \n\t 2. SignIn Account->\n")
    option = input("  \t")
    if option == '1':
        signup()
    elif option == '2':
        login()
    elif option == '3':
        Modify()
    

if __name__ == '__main__':
    body()
    