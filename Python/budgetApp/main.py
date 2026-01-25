class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})


    def withdraw(self, amount, description=""):
        amount = - amount
        self.ledger.append({"amount":amount, "description":description}) 
        #TODO: return true is succeed else false

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total

def create_spend_chart(categories):
    pass

def main():
    food = Category('food')
    food.deposit(500)
    food.withdraw(100)
    print(food.get_balance())

if __name__ == '__main__':
    main()