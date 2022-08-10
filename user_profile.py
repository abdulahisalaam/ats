import csv


class User:
    def __init__(self, username = '',password = '',confirm_password = '',email = ''):
        self.username = username
        self.password = password
        self.email = email 
        self.confirm_password = password  

    def write_data(self,**kwargs):
        header = ['username','password','email']
        with open("profile.csv", "w+", newline='\n') as d:
            handler = csv.DictWriter(d, fieldnames=header)
            handler.writeheader()
            handler.writerow(kwargs)

    #Validators
    def validate_username(self,username):
        report = username.__len__() >= 6
        if report:
            return True
        else:
            print('Invalid Username')
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
        if  self.password == self.confirm_password:
            return True
        else:
            print("password does not mismatched !!!")
            return False
    
    def validate_email(self,email):
        if self.email.endswith('.com') and '@' in self.email:
            return True
        else:
            print('invalid email address!!!')
            return False

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
        with open('profile.csv', 'r') as f:
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
    