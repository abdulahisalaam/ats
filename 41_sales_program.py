
from tabulate import tabulate
def sales_record():

    records = [[1234, 20, 220,320,425,530],
                [1235, 20, 20,320,425,530 ],
                [1236, 20, 20,320,425,530 ],
                [1237, 20, 20,320,425,430 ],
                [1238, 20, 20,20,25,30 ],
    ]
    
    total = sum([records[0][0],records[0][1],records[0][2],records[0][3]])
    

    head = ["Sales_Per_No.", "product1", "product2","product3", "product4","product5","Total Sales"]

    # sum([records[0][0],records[0][1],records[0][2],records[0][3]])

    print(tabulate(records,headers=head, tablefmt="fancy_grid"))
    # print(total)

sales_record()