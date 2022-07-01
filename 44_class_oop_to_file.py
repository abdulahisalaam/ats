
import csv
class Student:
    profile ='profile.csv'

    def __init__(self,firstname,lastname,attendance,day,month,year,email):
        self.firstname = firstname
        self.lastname = lastname
        self.day = day
        self.month = month
        self.year = year
        self.attendance = attendance
        self.email = email

    def create_profile(self):
        data = self.set_data()
        with open("profile.csv", "w", newline='') as f:
            header = ['Email','Firstname','Lastname','Day','Month','Year','Attendance']
            handler = csv.DictWriter(f, fieldnames = header)
            if handler.__len__() == 0:
                handler.writeheader()
                handler.writerow(data)
            else:
                handler.writerow(data)
        print(f"Your profile is created Successfully {data['firstname']} {data['lastname']}")
        return self.search(data['email'])

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

    def display_profiles(self):
        print(f"The amount of student Profile is {self.profile.__len__()}")
        return self.profile 
                
    def display_one(self,email):
        data = self.search(email)
        print(f"Firstname: {data['firstname']} ")
        print(f"Lastname: {data['lastname']} ")
        print(f"Date of birth: {data['date']}")
        print(f"Attendance: {data['attendance']} ")
        print(f"Email: {data['email']}")
    
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

stud = Student('','',0, 0, 0, 0, 0)

#print(stud.display_profiles())
#print(stud.update_profile(stud.get_email()))
#print(stud.delete_profile(stud.get_email()))
#print(stud.search(stud.get_email()))
print(stud.set_data())