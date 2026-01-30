from Models.Homewerk import BankAccount


my_Account = BankAccount(1000)
your_Account = BankAccount(500)

our_Account = my_Account + your_Account
our_Account -= your_Account
print(our_Account)