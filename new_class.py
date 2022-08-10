import csv
from user_profile import User
class Profile(User):
    def __init__(self,firstname ='',lastname ='',email ='',attendance ='',day ='',month ='',year =''):
        super().__init__(firstname,lastname,email,attendance,day,month,year)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('profile.csv', 'r') as f:
            reader = csv.DictReader(f)
            profile_records = list(reader)

        for data in profile_records:
            Profile(
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            email=data.get('email')
            )
    
    def set_data(self):
        self.firstname = self.get_firstname()
        self.lastname = self.get_lastname()
        self.email = self.get_email()
        self.attendance = self.get_attendance()
        self.day = self.get_day()
        self.month = self.get_month()
        self.year = self.get_year()
        #create a new class constructor and pass the details
        data = dict(firstname = self.firstname, lastname = self.lastname, attendance = self.attendance, day = self.day, month = self.month, year = self.year,email = self.email)
        return data

    def search(self,email):
        for data in self.profile:
            if data['email'] == email:
                return data

    def delete_profile(self, email):
        data = Student.search(self, email)
        self.profile.remove(data)
        print(f"This profile {data} deleted successfully.")
        print('\n')
        return self.profile
    
    def update_profile(self, email):
        print('\n')
        option = input(f"Enter options:" 
        f"\n\t1.Update email:"
        f"\n\t2....... Firstname:"
        f"\n\t3....... Lastname:"
        f"\n\t4....... Day of Birth:"
        f"\n\t5....... Month of Birth:"
        f"\n\t6....... Year of Birth:"
        f"\n\t7....... Attendance:\t\t\t\n")

        data = Student.search(self, email)
        indx = self.profile.index(data)

        if option == '1':
            self.profile[indx]['email'] = self.get_new_email()
            return self.profile[indx]
        elif option == '2':
            self.profile[indx]['firstname'] = self.get_new_firstname()
            return self.profile[indx]
        elif option == '3':
            self.profile[indx]['lastname']  = self.get_new_lastname()
            return self.profile[indx] 
        elif option == '4':
           self.profile[indx]['day'] = self.get_new_day()
           return self.profile[indx]
        elif option == '5':
           self.profile[indx]['month'] = self.get_month()
           return self.profile[indx]
        elif option == '6':
           self.profile[indx]['year'] = self.get_attendance()
           return self.profile[indx]
        elif option == '7':
            self.profile[indx]['attendance'] = self.get_new_attendance()
            return self.profile[indx]
        return f'Profile {self.profile[indx]} updated successful!!!'
                
    def display_one(self,email):
        data = self.search(email)
        return data
    
    def get_email(self):
        return input('Enter your Email: ')

    def get_birth(self):
        return dict(self.get_day(),self.get_month(),self.get_year())

    def return_profile(self):
        return self.profile

    def get_firstname(self):
        return input("Enter firstname: ")

    def get_lastname(self):
        return input("Enter lastname: ")

    def get_day(self):
        return int(input("Enter day: "))
    
    def get_month(self):
        return int(input("Enter month: "))

    def get_year(self):
        return int(input("Enter year: "))
    
    def get_firstname(self):
        return input("Enter firstname: ")

    def get_attendance(self):
        return int(input("Enter attendance: "))

    
    def get_new_email(self):
        return input('Enter your New Email: ')

    def get_new_firstname(self):
        return input("Enter New firstname: ")

    def get_new_lastname(self):
        return input("Enter your new lastname: ")

    def get_new_day(self):
        return int(input("Enter your new day: "))
    
    def get_new_month(self):
        return int(input("Enter New month: "))

    def get_new_year(self):
        return int(input("Enter year: "))

    def get_new_attendance(self):
        return int(input("Enter New attendance: "))

profile = Profile()