
class Balance:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return f"{self._balance:.2f}"

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

balance = Balance(500)

balance.deposit(1000)
balance.withdraw(150)
print(balance.balance)
    