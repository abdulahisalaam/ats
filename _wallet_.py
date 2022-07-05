import csv
from datetime import datetime
from mnemonic import Mnemonic
from _wallet_users import Users

class Wallet(Users):

    def __init__(self,firstname='',lastname='',password ='',email ='',wallet_address= '',role='',balance=''):
        super().__init__(firstname,lastname,password,email,wallet_address,role)

    def get_users_data(self):
        return super().return_data() 

    def generate_mnemonic(self):
        my_mnemonic = Mnemonic("english")
        words = my_mnemonic.generate(128)
        seed = Mnemonic.to_seed(words, passphrase="")
        return seed
        #entropy = Mnemonic.to_entropy(words)  

    def write_wallet_data(self,**kwargs):
        header = ['Firstname','Lastname','Email','Password','Wallet_Address','Balance','Role']
        with open("wallet.csv", "a+", newline='\n') as d:
            handler = csv.DictWriter(d, fieldnames=header)
            if len(self.return_wallet_data()) == 0:
                handler.writeheader()
                handler.writerow(kwargs)
            else:
                handler.writerow(kwargs)

    def return_wallet_data(self):
        with open('wallet.csv', 'r') as f:
            handler = csv.DictReader(f)
            return list(handler)
    
    def create_wallet(self,email):
        data = super().search(email)
        data.update({'Wallet_Address':self.generate_mnemonic(),'Balance':0.0,})
        self.write_wallet_data(Firstname = data['Firstname'], Lastname = data['Lastname'], Password = data['Password'],Email = data['Email'], Wallet_Address = data['Wallet_Address'], Balance = data['Balance'],Role = data['Role'])
        return f"{data['Firstname']} {data['Lastname']} Wallet Created Successfully!!!\n Wallet Address: {data['Wallet_Address']}"

    def search_wallet(self, email):
        for data in self.return_wallet_data():
            if data['Email'] == email:
                 return data

    def credit_wallet(self,email):
        data = self.search_wallet(email)
        amount = float(input("Enter Amount to be deposited: "))
        old_balance = float(data['Balance'])
        new_balance = old_balance + amount
        r = csv.DictReader(open('wallet.csv'))
        return f"Amount Deposited: {amount}\nOld Balance: {old_balance}\nCurrent Balance: {new_balance}"
        
    
    def get_fund_receiver(self, email):
        return self.search_wallet(email)

    def check_withdraw(self,value,amount):
        if value >= amount:
            return True
        else:
            return False

    def record_transaction(self,**kwargs):
        header = ['S_Firstname','S_Lastname','S_Email','Amount','Role','Time','R_Email','R_Firstname','RRole']
        with open("transaction.csv", "a+", newline='\n') as d:
            handler = csv.DictWriter(d, fieldnames=header)
            if len(self.return_transaction_data()) == 0:
                handler.writeheader()
                handler.writerow(kwargs)
            else:
                handler.writerow(kwargs)
        return kwargs

    def tranfer_fund(self,sender_email,receiver_email):
        s_data = self.search_wallet(sender_email)
        r_data = self.search_wallet(receiver_email)

        amount = float(input("Enter Amount You Want to Transfer: "))
        if self.check_withdraw(float(s_data['Balance']),amount):
            remain = float(s_data['Balance']) - amount
            float(r_data['Balance']) + amount
            print(f" {s_data['Firstname']} {s_data['Lastname']} Your current balance is {remain} ")
            
            self.record_transaction(S_Firstname = s_data['Firstname'],S_Lastname = s_data['Lastname'],S_Email = s_data['Email'],Amount = amount,Role= s_data['Role'],Time = datetime.now(),R_Email = r_data['Email'],R_Firstname = r_data['Firstname'],RRole = r_data['Role'])
            return f"Transfer of #{amount} from {s_data['Firstname']} to {r_data['Firstname']} was successful"
        return f"Insufficient Funds at {datetime.now()}"

    def get_balance(self,email):
        self.return_data()
    
    def return_transaction_data(self):
        with open("transaction.csv","r") as f:
            handler = csv.DictReader(f)
            return list(handler)
                


w = Wallet()
#print(w.get_users_data())
# print(w.create_wallet('salaamabdul@afex.com'))
# print(w.search_wallet('ahmadsharf@afex.com'))
# print(w.credit_wallet('ahmadsharf@afex.com'))
#print(w.tranfer_fund('ahmadsharf@afex.com', 'salaamabdul@afex.com'))
print(w.return_transaction_data())

        