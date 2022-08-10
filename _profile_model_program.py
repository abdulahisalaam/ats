import csv
# init_dicts = [{"firstname":'Awwal', "lastname":'Adeleke', "day":23, "month":4, "year":1990, "attendance":1},

# {"firstname":'Abdulwali', "lastname":'Tajudeen', "day":2, "month":3, "year":1991, attendance:1},

# {"firstname":'Abraham', "lastname":'Adekunle', "day":11, "month":7, "year":1992, "attendance":1},
 
# {"firstname":'Yusuff', lastname:'oyedele', day:20, month:5, year:1993, attendance:1},

# {"firstname":'Adebusola', lastname:'Adeyeye', day:26, month:3, year:1994, attendance:1},

# {"firstname":'Basheer', last_name:'Balogun', day:21, month:1, year:1995, attendance:1},

# {"firstname":'Abdullahi',lastname:'salaam', day:15, month:9, year:1990, attendance:1},

# {"firstname":'Faith', lastname:'Adeosun', day:13, month:10, year:1990, attendance:1},

# {"firstname":'Ahmad', lastname:'Sharafudeen', day:25, month:12, year:1990, attendance:1},

# {"firstname":'Lukman', lastname:'Abisoye', day:27, month:4, year:1990, attendance:1},

# {"firstname":'Toluwanimi', lastname:'Ogunbiyi', day:30, month:11, year:1990, attendance:1}]

# #a)
def dict_increment():
    keys =['firstname','lastname','day','month','attendance','height','weight']
    data = {}
     
    data['firstname']=input("Enter firstname: ")
    data['lastname']=input("Enter lastname: ")
    data['day']=input("Enter day: ")
    data['month']=input("Enter month: ")
    data['attendance']=input("Enter attendance: ")
    data['height']=input("Enter height: ")
    data['weight']=input("Enter weight")
    

    with open("output.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(keys)
        csv_writer.writerows(data[keys])

    print('new profile is added successful')

print(dict_increment())

def read_profile_records():
    dict_from_csv = {}

    with open('output.csv', newline='') as inp:
        reader = csv.DictReader(inp)
        for row in reader:
            rows= row
    return rows
    
#print(read_profile_records())

def check_min_age(*fn):
    pass 
#print(check_min_age(read_profile_records()))

def check_max_age():
    pass

def print_cal_bmi():
    pass

def profile_system():
    pass
def calculate_birth_year():
    pass