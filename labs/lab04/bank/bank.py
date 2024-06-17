class Bank:
    def __init__(self):
        self.balance = 1000

    def main(self):
        print("Start Banking(d/w/s/x): ")
        choice = input().strip()

        while choice!='x':
            match choice:
                case 'd':
                    amount = float(input("Amount to deposit $"))
                    self.balance += amount
                    print(f'Amount deposited ${amount:.2f}')
                case 'w':
                    amount = float(input("Amount to withdraw $"))
                    if self.balance >= amount:
                        self.balance -= amount
                        print(f'Amount withdrawn ${amount:.2f}')
                    else:
                        print("Insufficient funds")
                case 's':
                    print(f'Starting balance ${self.balance:.2f}')
                case _:
                    print("Unknown choice!")

            print("Continue Banking(d/w/s/x): ")
            choice = input().strip()

if __name__ == "__main__":
    Bank().main()