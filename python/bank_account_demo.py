from bank_account import BankAccount

account1 = BankAccount("1234", 1000)
print(account1)

account1.deposit(10)

account1.withdraw(1)

print(account1.get_balance())
