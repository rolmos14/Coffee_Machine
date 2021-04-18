class CoffeeMachine:

    # Receipts
    espresso = {"water": 250,
                "milk": 0,
                "coffee beans": 16,
                "disposable cups": 1}
    latte = {"water": 350,
             "milk": 75,
             "coffee beans": 20,
             "disposable cups": 1}
    cappuccino = {"water": 200,
                  "milk": 100,
                  "coffee beans": 12,
                  "disposable cups": 1}

    # Receipt number and price
    receipts = {"1": ("self.espresso", 4),
                "2": ("self.latte", 7),
                "3": ("self.cappuccino", 6)}

    # Resource units
    resource_units = {"water": "ml",
                      "milk": "ml",
                      "coffee beans": "grams",
                      "disposable cups": ""}

    def __init__(self, water, milk, beans, cups, cash):
        # Initial state
        self.resources = {"water": water,
                          "milk": milk,
                          "coffee beans": beans,
                          "disposable cups": cups}
        self.resource_iter = None
        self.filling_resource = None
        self.cash = cash
        self.state = "Choosing action"
        print("Write action (buy, fill, take, remaining, exit): ")

    def __str__(self):
        remaining_resources = "\nThe coffee machine has:\n"
        for resource, quantity in self.resources.items():
            remaining_resources += f"{quantity} of {resource}\n"
        remaining_resources += f"${self.cash} of money\n"
        return remaining_resources

    def add_cash(self, cash):
        self.cash += cash

    def take_cash(self):
        print(f"\nI gave you ${self.cash}\n")
        self.cash = 0

    def enough_resources(self, receipt):
        for resource in self.resources:
            if self.resources[resource] >= receipt[resource]:
                continue
            else:
                print(f"Sorry, not enough {resource}!\n")
                self.state = "Choosing action"
                return False
        return True

    def prepare(self, receipt):
        for resource in self.resources:
            # Take receipt quantities from existing resources
            self.resources[resource] -= receipt[resource]

    def buy(self, selection):
        if self.state == "Choosing action":
            # Create receipts menu prompt dynamically based on existing receipts
            receipts_menu = ""
            for receipt_key, receipt_value in self.receipts.items():
                # Filter self. from receipts dictionary
                receipts_menu += receipt_key + " - " + receipt_value[0][5:] + ", "
            self.state = "Choosing coffee type"
            print("\nWhat do you want to buy? " + receipts_menu + "back - to main menu: ")
        elif selection == "back":
            self.state = "Choosing action"
            print()  # empty line
        elif self.enough_resources(eval(self.receipts[selection][0])):
            print("I have enough resources, making you a coffee!\n")
            # Prepare the receipt and add cash
            self.prepare(eval(self.receipts[selection][0]))
            self.add_cash(self.receipts[selection][1])
            self.state = "Choosing action"

    def fill(self, quantity):
        if self.state == "Choosing action":
            # Initialize iterator for resources
            self.resource_iter = iter(self.resource_units)
            # Select first resource to fill
            self.filling_resource = next(self.resource_iter)
            self.state = "Filling machine"
            print(f"\nWrite how many {self.resource_units[self.filling_resource]} "
                  f"of {self.filling_resource} do you want to add: ")
        else:
            # Fill current resource
            self.resources[self.filling_resource] += int(quantity)
            try:
                # Select next resource to fill
                self.filling_resource = next(self.resource_iter)
                print(f"Write how many {self.resource_units[self.filling_resource]} "
                      f"of {self.filling_resource} do you want to add: ")
            except StopIteration:
                # Finish filling when no more resources left
                print()  # empty line
                self.state = "Choosing action"

    def action(self, selection):

        if selection == "buy" or self.state == "Choosing coffee type":
            self.buy(selection)
        elif selection == "fill" or self.state == "Filling machine":
            self.fill(selection)
        elif selection == "take":
            self.take_cash()
        elif selection == "remaining":
            print(self)

        if self.state == "Choosing action":
            print("Write action (buy, fill, take, remaining, exit): ")


coffee_maker = CoffeeMachine(400, 540, 120, 9, 550)

# Get user input until exit
while True:
    user_input = input()
    if user_input == "exit":
        break
    coffee_maker.action(user_input)
