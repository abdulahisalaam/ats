
class Student:
    profile=[{'email':'awal@afex.com','firstname':'Awwal', 'lastname':'Adeleke', 'date':{'day':23, 'month':4, 'year':1990}, 'attendance':1},
        {'email':'abdulwal@afex','firstname':'Abdulwali', 'lastname':'Tajudeen', 'date':{'day':2, 'month':3, 'year':1991}, 'attendance':1},

        {'email':'abrah@afex.com','firstname':'Abraham', 'lastname':'Adekunle', 'date':{"day":11, 'month':7, 'year':1992}, 'attendance':1},
 
        {'email':'yusf@afex.com','firstname':'Yusuff', 'lastname':'oyedele', 'date':{'day':20, 'month':5, 'year':1993}, 'attendance':1},

        {'email':'ades@afex.com','firstname':'Adebusola', 'lastname':'Adeyeye', 'date':{'day':26, 'month':3, 'year':1994}, 'attendance':1},

        {'email':'bashy@afex.com','firstname':'Basheer', 'lastname':'Balogun', 'date':{'day':21, 'month':1, 'year':1995}, 'attendance':1},

        {'email':'saab@afex.com','firstname':'Abdullahi','lastname':'salaam', 'date':{'day':15, 'month':9, 'year':1990}, 'attendance':1},

        {'email':'faith@afex.com','firstname':'Faith', 'lastname':'Adeosun', 'date':{'day':13, 'month':10, 'year':1990}, 'attendance':1},

        {'email':'ahmad@afex.com','firstname':'Ahmad', 'lastname':'Sharafudeen','date':{'day':25, 'month':12, 'year':1990}, 'attendance':1},

        {'email':'luk@afex.com','firstname':'Lukman', 'lastname':'Abisoye', 'date':{'day':27, 'month':4, 'year':1990}, 'attendance':1},

        {'email':'tolu@afex.com','firstname':'Toluwanimi', 'lastname':'Ogunbiyi','date':{'day':30, 'month':11, 'year':1990}, 'attendance':1}]


    def __init__(self,firstname,lastname,attendance,day,month,year,email):
        self.firstname = firstname
        self.lastname = lastname
        self.day = day
        self.month = month
        self.year = year
        self.attendance = attendance
        self.email = email

    def increment_profile(self):
        data = self.set_data()
        self.profile.append(data)
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
#print(stud.set_data())