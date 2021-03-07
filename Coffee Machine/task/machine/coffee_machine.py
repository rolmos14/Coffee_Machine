def buy_menu():

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

    receipts = {"1": ("espresso", 4),
                "2": ("latte", 7),
                "3": ("cappuccino", 6)}

    def enough_resources(receipt):
        for resource in resources:
            if resources[resource] >= receipt[resource]:
                continue
            else:
                print(f"Sorry, not enough {resource}!")
                return False
        return True

    def prepare(receipt):
        global resources
        for resource in resources:
            # Take receipt quantities from existing resources
            resources[resource] -= receipt[resource]

    def add_cash(money):
        global cash
        cash += money

    # Create receipts menu prompt dynamically based on existing receipts
    receipts_menu = ""
    for receipt_key, receipt_value in receipts.items():
        receipts_menu += receipt_key + " - " + receipt_value[0] + ", "

    item = input("\nWhat do you want to buy? " + receipts_menu + "back - to main menu: ")

    if item != "back" and enough_resources(eval(receipts[item][0])):
        print("I have enough resources, making you a coffee!")
        # Prepare the receipt and add cash
        prepare(eval(receipts[item][0]))
        add_cash(receipts[item][1])


def fill_menu():
    global resources
    resource_unit = {"water": "ml",
                     "milk": "ml",
                     "coffee beans": "grams",
                     "disposable cups": ""}
    print()
    for resource in resources:
        resources[resource] += \
            int(input(f"Write how many {resource_unit[resource]} of {resource} do you want to add: "))


def take_menu():
    global cash
    print(f"I gave you ${cash}")
    cash = 0


def print_state():
    print("\nThe coffee machine has:")
    for resource, quantity in resources.items():
        print(f"{quantity} of {resource}")
    print(f"${cash} of money")


def main_menu():
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        buy_menu()
    elif action == "fill":
        fill_menu()
    elif action == "take":
        take_menu()
    elif action == "remaining":
        print_state()
    return action


# Initial state
resources = {"water": 400,
             "milk": 540,
             "coffee beans": 120,
             "disposable cups": 9}

cash = 550

while True:
    # Call main menu and perform action
    action = main_menu()
    if action == "exit":
        break
    print()  # empty line
