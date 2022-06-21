import sqlite3
def deposite_account():
    pass

def check_balance(acc_no:int):
    contents = []
    f= open("ussd.txt","r")
    f1= f.read()
    contents.append(f1)
    print(contents)
    return contents

def Register_ussd():

    con = sqlite3.connect("ussd.db")

    con.execute("CREATE TABLE customer (
	        Acc_no n(10),
	        Firstname CHAR(30),
	        Lastname CHAR(30),
	        Acc_balance	decimal(7,2),
            Pin n(4) DEFAULT 0000,
	        PRIMARY KEY("Acc_no" AUTOINCREMENT);"
            )
            
    firstname = input("Enter Firstname: ")
    lastname = input("Enter Lastname: ")
    con.execute("""INSERT INTO customer(Firstname,Lastname,acc_balance,Pin) 
    VALUES (?,?,?,?)""", (Firstname,Lastname,acc_balance,Pin))
    con.commit()
    con.close()

def collect_ussd_option():
    print('Enter Option ')
    print('1. Register')
    print('2. Check Balance')
    print('3. Make Transfer')
    print('4. Buy Airtime')
    option = int(input('Enter: '))

    if option == 1:
        Register_ussd()
    elif option == 2:
        acc_no = int(input("Enter Account No. "))
        check_balance(acc_no)
    elif option == 3:
        generate_account_no()
    elif option == 4:
        pass
    else:
        print("Only positive integer are allowed")
        collect_ussd_option()


collect_ussd_option()

