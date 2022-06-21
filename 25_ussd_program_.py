import pickle
def deposite_account():
    depo = int(input("Enter amount to Deposit"))
    return depo


def generate_account_no():
    acc_no = (input("Enter Account Number"))
    return acc_no

def check_balance(acc_no):
    
    dbfile = open('ussd','rb')
    header = pickle.load(dbfile)
    print(header.items())
    


    
    # result = [acc for acc in header.items() if acc['acc_no'] == acc_no]
    # print(result)

    # contents = []
    # f= open("ussd.txt","r")
    # f1= f.read()
    # contents.append(f1)

    # print(type(contents[0]))
    #return [acc for acc in contents if acc['acc_no'] == acc_no]

def get_details():
    contents = []
    f= open("ussd.txt","r")
    f1= f.read()
    contents.append(f1)
    print(contents)
    return contents

def make_transfer():
    get_details()



def Register_ussd():
    header = {}

    header['firstname'] = input("Enter Firstname: ")
    header['lastname']= input("Enter Lastname: ")
    header['account_b'] = 0.0 + deposite_account()
    header['pin']= '0000'
    header['acc_no']=generate_account_no()

    print(type(header))

    dbfile =open('ussd', 'ab')

    pickle.dump(header, dbfile)

    dbfile.close()

    # f = open("ussd.txt","a+")
    # f.write(f"{header},\n")
    # f.close()

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
        acc_no = input("Enter account number: ")
        check_balance(acc_no)
    elif option == 3:
        make_transfer()
    elif option == 4:
        get_details()
    else:
        print("Only positive integer are allowed")
        collect_ussd_option()

if __name__ == '__main__':
    collect_ussd_option()

