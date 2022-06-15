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
    listo = []
    
    dict_profile = {}
        
    for key in keys:
        dict_profile[key]=input("Enter " + key)
    listo.append(dict_profile)

    keyy = listo[0].keys()

    a_file = open("output.csv", "w")
    dict_writer = csv.DictWriter(a_file, keyy)
    dict_writer.writeheader()
    dict_writer.writerows(listo)
    a_file.close()

    print('new profile is added successful')

#print(dict_increment())

def read_profile_records():
    dict_from_csv = {}

    with open('output.csv', mode='r') as inp:
        reader = csv.DictReader(inp)
        for row in reader:
            (row['firstname'], row['lastname'],row['day'],row['month'],row['attendance'],row['height'],row['weight'])
    return row
    
print(read_profile_records())

def check_min_age():
    pass

def check_max_age():
    pass

def print_cal_bmi():
    pass

def profile_system():
    pass
def calculate_birth_year():
    pass