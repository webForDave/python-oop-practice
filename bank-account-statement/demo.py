class BankAccount():

    number_of_accounts = 0
    
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        # increment number of accounts after every instance created
        BankAccount.number_of_accounts += 1

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance < amount:
            return 'Insufficient funds'
        self.balance -= amount


    def check_balance(self):
        return self.balance
    

account1 = BankAccount(12345, 'Dave', 10000)
account2 = BankAccount(67890, 'Kenny', 5000)
account3 = BankAccount(14567, 'John', 60000)
account4 = BankAccount(56678, 'Doe', 0)
