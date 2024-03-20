class Bank:
    def __init__(self):
        self.balance = 1000

    def readAmount(self,action):
        return float(input(f'Amount to ${action} $'))

    def deposit(self):
        amount = self.readAmount("deposit")
        self.balance += amount
        print("Amount %.2f deposited%n", amount)

    def withdraw(self): 
        amount = self.readAmount("withdraw")
        if (self.balance >= amount):
            self.balance -= amount
            print("Amount %.2f withdrawn%n", amount)
        else:
            print("Insufficient funds!")

    def show(self):
        print(f"Starting balance ${self.balance:.2f}")

    def read_choice(self):
        return input("Start Banking (d/w/s/x): ")[0]

    def help(self):
        print("d - deposit")
        print("w - withdraw")
        print("s - show")
        print("x - exit")

    def main(self):
        choice = self.read_choice()

        while choice!='x':
            match choice:
                case 'd':
                    self.deposit()
                case 'w':
                    self.withdraw()
                case 's':
                    self.show()
                case _:
                    self.help()

            print("Continue Banking(d/w/s/x): ")
            choice = self.read_choice()

bank = Bank()
bank.main()