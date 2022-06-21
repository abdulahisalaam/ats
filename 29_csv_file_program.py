import csv
import io

def data_csv():
    data = {}

    data['firstname'] = input("What is your Firstname? : ")

    data['lastname'] = input("What is your Lastname? : ")

    data['m_name'] = input("What is your middlename? : ")

    data['age'] = input("How old are your? : ")

    data['occupation'] = input("What your occupation? : ")

    data['date_of_birth'] = input("Enter your date of birth: ")

    data['gender'] = input("what your gender? : ")

    data['marital_status'] = input("Are you married or single? : ")

    data['email'] = input("Enter e-mail address? : ")

    with open("mydata.csv", "w", newline='') as d:
        header = ['firstname','lastname','m_name','age','occupation','date_of_birth','gender','marital_status','email']
        handler = csv.DictWriter(d, fieldnames=header)
        handler.writeheader()
        handler.writerow(data)

def read_data():

    with open("mydata.csv") as f:
        handler= csv.DictReader(f)
        for k,v in enumerate(handler):
            print(k,v)
        


def filter_input():

    keyy = int(input("Enter 1 to search with Firstname->\n Enter 2 to search with Lastname-> \n Enter 3 to search with Middlename-> \nEnter 4 to search occupation-> \n Enter 5 to search with date of birth-> \n Enter 6 to search with gender-> \n Enter 7 to search with Marital Status->"))
    if keyy ==1:
        f_name =input('Enter Firstname: ')
        return f_name
    elif keyy ==2:
        l_name=input('Enter Lastname: ')
        return l_name
    elif keyy == 3:
        m_name=input('Enter Middlename: ')
        return m_name
    elif keyy == 4:
        age=input('Enter age: ')
        return age
    elif keyy == 5:
        occupation=input('Enter occupation: ')
        return occupation
    elif keyy == 6:
       date_of_birth =input('Enter date of birth: ')
       return date_of_birth
    elif keyy ==7:
        gender =input('Enter your gender: ')
        return date_of_birth
    elif keyy ==8:
        marital_status =input('Enter your gender: ')
        return marital_status
    elif keyy ==9:
        email =input('Enter your Email: ')
    else:
        filter_data()

def filter_data():
    search_key = filter_input()
    with io.open('mydata.csv', 'r', newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['f_name'] == row[search_key]:
                print(row[f_name]) 


    



def body():
    print('welcome <------------>')
    option = int(input("Please Enter 1 to save your data:\n 2 to read your data: \n 3 to search your data:\n"))
    if option == 1:
        data_csv()
    elif option == 2:
        read_data()
    elif option == 3:
        filter_data()
    else:
        body()

if __name__ == '__main__':
    body()
    


