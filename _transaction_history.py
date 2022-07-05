import csv
from _wallet_users import Users
from _wallet_ import Wallet

class Transaction(Wallet,Users):
    def __init__(self):
        super(Transaction, self).__init__()

    def get_transactions():
            """Displays all transactions of all users """
            return Wallet.return_transaction_data(self)
        
    def create_history(self):
            """Creates an asset, with the user as the creator"""
            return create_asset(self.public_key,asset_name,unit_name,total,decimals,default_frozen,self.id)


trans = Transaction()
print(trans.get_transactions)