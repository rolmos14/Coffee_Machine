coffee_ingredients = {"water": 200,
                      "milk": 50,
                      "coffee beans": 15}

avail_water = int(input("Write how many ml of water the coffee machine has: "))
avail_milk = int(input("Write how many ml of milk the coffee machine has: "))
avail_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
req_cups = int(input("Write how many cups of coffee you will need: "))

# Required ingredients
req_water = req_cups * coffee_ingredients["water"]
req_milk = req_cups * coffee_ingredients["milk"]
req_beans = req_cups * coffee_ingredients["coffee beans"]

# Remaining ingredients after making required cups
rem_water = avail_water - req_water
rem_milk = avail_milk - req_milk
rem_beans = avail_beans - req_beans

if rem_water >= 0 and rem_milk >= 0 and rem_beans >= 0:
    add_cups = min(rem_water // coffee_ingredients["water"],
                   rem_milk // coffee_ingredients["milk"],
                   rem_beans // coffee_ingredients["coffee beans"])
    print("Yes, I can make that amount of coffee",
          f"(and even {add_cups} more than that)" if add_cups else "")
else:
    min_cups = min(avail_water // coffee_ingredients["water"],
                   avail_milk // coffee_ingredients["milk"],
                   avail_beans // coffee_ingredients["coffee beans"])
    print(f"No, I can make only {min_cups} cups of coffee")
