from customer import Customer
from config import DTF,NOW

class Bank:
    def __init__(self):
        self.customers = []
        self.add_customers()
    
    def main(self):
        self.menu()
    
    def add_customers(self):
        for _ in range(3):
            self.customers.append(Customer())
    
    def read_choice(self):
        print("Bank menu (L/V/X): ", end="")
        return input().strip().upper()
    
    def customer(self, name):
        for c in self.customers:
            if c.match(name):
                return c
        return None
    
    def read_name(self):
        print("Enter Login Name: ", end="")
        return input().strip()
    
    def login(self):
        c = self.customer(self.read_name())
        if c:
            c.use()
        else:
            print("Customer does not exist")
    
    def view(self):
        for customer in self.customers:
            print(customer)
    
    def menu(self):
        print("Bank menu: " + NOW.strftime(DTF))
        while True:
            choice = self.read_choice()
            if choice == 'X':
                break
            elif choice == 'L':
                self.login()
            elif choice == 'V':
                self.view()
            else:
                self.help()
        print("Done")
    
    def help(self):
        print("Menu options")
        print("L = Login into customer menu")
        print("V = View all customers")
        print("X = exit")

# Running the main function
bank = Bank()
bank.main()