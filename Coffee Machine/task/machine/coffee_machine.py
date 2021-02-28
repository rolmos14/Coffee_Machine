def print_state():
    print(f"The coffee machine has:",
          f"{avail_water} of water",
          f"{avail_milk} of milk",
          f"{avail_beans} of coffee beans",
          f"{avail_cups} of disposable cups",
          f"{avail_money} of money",
          sep="\n")


def main_menu():
    action = input("Write action (buy, fill, take): ")
    if action == "buy":
        buy_menu()
    elif action == "fill":
        fill_menu()
    else:  # action == "take"
        take_menu()


def buy_menu():
    def prepare_espresso():
        espresso_receipt = {"water": 250,
                            "coffee beans": 16,
                            "cups": 1,
                            "cost": 4}
        global avail_water, avail_beans, avail_cups, avail_money
        avail_water -= espresso_receipt["water"]
        avail_beans -= espresso_receipt["coffee beans"]
        avail_cups -= espresso_receipt["cups"]
        avail_money += espresso_receipt["cost"]

    def prepare_latte():
        latte_receipt = {"water": 350,
                         "milk": 75,
                         "coffee beans": 20,
                         "cups": 1,
                         "cost": 7}
        global avail_water, avail_milk, avail_beans, avail_cups, avail_money
        avail_water -= latte_receipt["water"]
        avail_milk -= latte_receipt["milk"]
        avail_beans -= latte_receipt["coffee beans"]
        avail_cups -= latte_receipt["cups"]
        avail_money += latte_receipt["cost"]

    def prepare_cappuccino():
        cappuccino_receipt = {"water": 200,
                              "milk": 100,
                              "coffee beans": 12,
                              "cups": 1,
                              "cost": 6}
        global avail_water, avail_milk, avail_beans, avail_cups, avail_money
        avail_water -= cappuccino_receipt["water"]
        avail_milk -= cappuccino_receipt["milk"]
        avail_beans -= cappuccino_receipt["coffee beans"]
        avail_cups -= cappuccino_receipt["cups"]
        avail_money += cappuccino_receipt["cost"]

    item = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if item == "1":
        prepare_espresso()
    elif item == "2":
        prepare_latte()
    else:  # item == "3"
        prepare_cappuccino()


def fill_menu():
    global avail_water, avail_milk, avail_beans, avail_cups
    avail_water += int(input("Write how many ml of water do you want to add: "))
    avail_milk += int(input("Write how many ml of milk do you want to add: "))
    avail_beans += int(input("Write how many grams of coffee beans do you want to add: "))
    avail_cups += int(input("Write how many disposable cups of coffee do you want to add: "))


def take_menu():
    global avail_money
    print(f"I gave you ${avail_money}")
    avail_money = 0


# Initial state
avail_water = 400
avail_milk = 540
avail_beans = 120
avail_cups = 9
avail_money = 550

# Print initial state
print_state()
print()  # empty line

# Call main menu and perform action
main_menu()

# Print final state
print()  # empty line
print_state()
