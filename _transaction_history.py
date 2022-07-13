import csv
from _wallet_users import Users
from _wallet_ import Wallet

class Transaction(Users,Wallet):
    def __init__(self):
        Users.__init__(self,firstname='',lastname='',email='',wallet_address='',role=role[0])
        Wallet.__init__(self,firstname='',lastname='',email='',role='',balance='')

    def get_transactions():
            """Displays all transactions of all users """
            return Wallet.return_transaction_data()
        
    def create_history(self):
            """Creates an asset, with the user as the creator"""
            return create_asset(self.public)


trans = Transaction()
print(trans.get_transactions)