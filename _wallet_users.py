import re
import csv


class Users:
    roles = ["user","lead","admin"]

    def __init__(self,firstname='',lastname='',password='',email='',wallet_address=None,role=roles[0]):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.wallet_address = wallet_address
        self.email = email
        self.user = role
    
    def validate_name(self,username):
        report = username.__len__() >= 6
        if report:
            return True
        else:
            print('Invalid Name, Name must be Atleast 6 letter long')
            return False
    
    def validate_password(self,password):
            lower = any(c.islower() for c in password)
            upper = any(c.isupper() for c in password)
            digit = any(c.isdigit() for c in password)
            length = password.__len__() >= 6
            report = lower and upper and digit and password.__len__() >= 6

            if report:
                return True
            elif not lower:
                print("Password must contain Lower Case letter")
                return False
            elif not upper:
                print("Password must contain Upper Case letter")
                return False
            elif not digit:
                print("password must contain digit")
                return False
            elif not length:
                print("Password should Atleast have 6 character")
                return False
            else:
                print('Invalid Password')
                return False
          

    def validate_confirm_password(self,confirm_password,password):
        if  password == confirm_password:
            return True
        else:
            print("password does not mismatched !!!")
            return False
    
    def validate_email(self,email):
        regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
        if re.fullmatch(regex, email):
            return True
        else:
            print('invalid email address e.g abc@example.com!!!')
            return False

    def get_email(self):
        return input('Enter your Email: ')

    def get_firstname(self):
        return input("Enter firstname: ")

    def get_lastname(self):
        return input("Enter your lastname: ")
    
    def get_password(self):
        return input("Enter your password: ")
    
    def get_confirm_password(self):
        return input("Enter Your Password to Confirm: ")
    
    def set_data(self):
        while True:
            fstname = self.get_firstname().upper()
            if self.validate_name(fstname):
                self.firstname = fstname
                break
        
        while True:
            lstname = self.get_lastname().upper()
            if self.validate_name(lstname):
                self.lastname = lstname
                break
        
        while True:
            passw = self.get_password()
            if self.validate_password(passw):
                self.password = passw
                break
        
        while True:
            com_passw = self.get_confirm_password()
            if self.validate_confirm_password(com_passw,self.password):
                self.password = com_passw
                break
        
        while True:
            mail = self.get_email().lower()
            if self.validate_email(mail):
                self.email = mail
                break            

        self.wallet_address = self.generate_mnemonic()
        #create a new class constructor and pass the details
        data = dict(Firstname = self.firstname, Lastname = self.lastname,Wallet_Address = self.wallet_address,Email = self.email, Role=self.roles)
        return data
    
    def search(self,email):
        for data in self.return_data():
            if data['Email'] == email:
                 return data
    
    def delete_profile(self,wallet_address):
        data = search(self.wallet_address)
        self.profile.remove(data)
        print(f"This profile {data} deleted successfully.")
        print('\n')
        return self.profile
    
    def write_data(self,**kwargs):
        header = ['Firstname','Lastname','Password','Email','Role']
        with open("users.csv", "a+", newline='\n') as d:
            handler = csv.DictWriter(d, fieldnames=header)
            if len(self.return_data()) == 0:
                handler.writeheader()
                handler.writerow(kwargs)
            else:
                handler.writerow(kwargs)

    def user_signup(self):
        wallet_address = self.generate_mnemonic()
        if self.validate_username(self.username):
            username = self.username
        if self.validate_password(self.password):
            password = self.password
        elif self.validate_confirm_password(self.confirm_password,self.password):
            confirm_password = self.confirm_password
        elif self.validate_email(self.email):
            email = self.email
        
        self.write_data(Firstname=self.firstname,Lastname=self.username,Password=self.password,Email=self.email,Role = self.roles)
        return f"SignUp Successful {self.username}"    

    def signup(self):
        if self.validate_username(self.username):
            username = self.username
        if self.validate_password(self.password):
            password = self.password
        elif self.validate_confirm_password(self.confirm_password,self.password):
            confirm_password = self.confirm_password
        elif self.validate_email(self.email):
            email = self.email
        
        self.write_data(username=self.username,password=self.password,email=self.email)
        return f"SignUp Successful {self.username}"

    def return_data(self):
        with open('users.csv', 'r') as f:
            handler = csv.DictReader(f)
            return list(handler)

    def signin(self):
        data = self.return_data()
        for i in data:
            if i['password']== self.password and i['email']== self.email:
                print(f"Successfully Login {i['username']}!!!")
                return True
            else:
                print("Invalid Password and Email !!!")
                return False

#s = Users()
#s.set_data()
#print(s.search('kola@afex.com'))
#print(s.return_data())
#s.write_data(Firstname='abdullahi',Lastname='salaam',Password='Salaam@12',Email='salaamabdul@afex.com',Role = 'user')
