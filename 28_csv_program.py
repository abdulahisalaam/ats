import csv
# with open('data.csv', 'r') as f:
#     handler = csv.reader(f)
#     for row in handler:
#         print(row)
#         for i in row:
#             print(i)

# with open("data.csv","w+") as f:
#     handler = csv.writer(f)
#     handler.writerow(['abdultruth','kolawole','20','male'])

# with open("datadict.csv") as f:
#     handler= csv.DictReader(f)
#     for k,v in enumerate(handler):
#         print(k,v)


with open("datadict2.csv", "w", newline="") as f:
    header = ['f_name','l_name','gender','age']
    handler = csv.DictWriter(f, fieldnames=header)
    handler.writeheader()
    handler.writerow({'f_name':'awal','l_name':'adeleke','gender':'male','age':'30'})

