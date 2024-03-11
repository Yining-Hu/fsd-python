class Bank:
    def __init__(self):
        pass

    def main():
        inpt = input("Amount to deposit $")
        deposit = float(inpt)
        print("Amount $%.2f deposited" % deposit)

        inpt = input("Amount to withdraw $")
        withdraw = float(inpt)
        print("Amount $%.2f withdrawn" % withdraw)

if __name__ == "__main__":
    Bank.main()
