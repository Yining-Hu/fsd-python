from customer import Customer

class Bank:
    def __init__(self):
        self.customer = Customer("John Smith")

    def main(self):
        self.menu()

    def read_amount(self, action):
        print("Amount to", action, end=' $')
        return float(input())

    def deposit(self):
        amount = self.read_amount("deposit")
        self.customer.deposit(amount)
        print("Amount {:.2f} deposited".format(amount))

    def withdraw(self):
        amount = self.read_amount("withdraw")
        if self.customer.is_sufficient(amount):
            self.customer.withdraw(amount)
            print("Amount {:.2f} withdrawn".format(amount))
        else:
            print("Insufficient funds!")

    def transfer(self):
        amount = self.read_amount("transfer")
        if self.customer.is_sufficient(amount):
            self.customer.transfer(amount)
            print("Amount {:.2f} transferred".format(amount))
        else:
            print("Insufficient funds!")

    def show(self):
        self.customer.show()

    def read_choice(self):
        return input("Start Banking (d/w/t/s/x): ")[0]

    def help(self):
        print("d - deposit")
        print("w - withdraw")
        print("t - transfer")
        print("s - show")
        print("x - exit")

    def menu(self):
        while True:
            c = self.read_choice()
            if c == 'x':
                break
            elif c == 'd':
                self.deposit()
            elif c == 'w':
                self.withdraw()
            elif c == 't':
                self.transfer()
            elif c == 's':
                self.show()
            else:
                self.help()

bank = Bank()
bank.main()