class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})


    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            amount = - amount
            self.ledger.append({"amount":amount, "description":description}) 
            return True
        else:
            return False
        #TODO: return true is succeed else false

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry["amount"]
        return total

        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        result = ""
        stars = ''
        for i in range((30-len(self.name))//2):
            stars += '*'
        result += stars
        result += self.name
        if len(self.name) % 2 == 1:
            result += "*"
            result += stars
        else:
            result += stars
        result += "\n"

        for entry in self.ledger:
            money = "%.2f" % float(entry["amount"])
            #assuming max amount is 99999.00(7 characters)
            spaces = ""
            if len(entry["description"]) > 23:
                desc_len = 23
            else:
                desc_len = (len(entry["description"]))
            length = 30-(len(str(money)) + desc_len)
            for i in range(length):
                spaces +=" "
            result += entry["description"][0:23]
            result += spaces
            result += money
            result += "\n"
        result += f"Total: {self.get_balance()}"
        return(result)
            

def create_spend_chart(categories):
    spent_per_category = []

    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                spent += abs(entry["amount"])
        spent_per_category.append(spent)

    total_spent = sum(spent_per_category)

    percentages = []
    for spent in spent_per_category:
        percent = int((spent/total_spent)*100)
        percent = (percent//10) * 10
        percentages.append(percent)

    

    chart = "Percentage spent by category\n"

    for level in range(100,-1, -10):
        chart += str(level).rjust(3) + "|"
        
        for p in percentages:
            if p >= level:
                chart += " o "
            else: chart += "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + '\n'

    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

        
 
def main():
    food = Category('Food')
    food.deposit(1000, 'deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    clothing.deposit(500, 'deposit')
    clothing.withdraw(6.43, 'groceries')
    clothing.withdraw(1.43, 'restaurant and more food for dessert')

    auto = Category('Auto')
    auto.deposit(500, 'car')
    auto.withdraw(3.5, 'windshield')
    auto.withdraw(1.0, 'tyre')

    categories = [food, clothing, auto]
    print(create_spend_chart(categories))
    
if __name__ == '__main__':
    main()