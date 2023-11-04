class BankAccount:

    history = []

    def __init__(self, balance, int_rate, trans):
        self._balance = balance
        self.__int_rate = int_rate
        self.__trans = trans

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print(f'Внесение наличных на счет: {amount}')
        self.history.append('Внесение наличных')

    def withdraw(self, amount):
        self.__balance = self__balance = amount
        print(f'Снятие наличных: {amount}')
        self.history.append('Снятие наличных ')

    def add_interest(self):
        self.__balance = self.__balance * self.__int_rate / 100 + self.__balance
        print(f'Начисляем проценты по вкладу: {self.__balance * self.__int_rate / 100}')
        self.history.append('Начисление процентов')

    def history_list(self):
        for i in self.history:
            print('-', i)

account = BankAccount(100000, 0.05, 1)
account.deposit(15000)
account.withdraw(7500)
account.add_intereset()
account.history_list()

