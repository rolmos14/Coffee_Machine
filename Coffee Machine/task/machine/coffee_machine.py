coffee_ingredients = {"water": 200,
                      "milk": 50,
                      "coffee beans": 15}

cups = int(input("Write how many cups of coffee you will need: "))

req_water = cups * coffee_ingredients["water"]
req_milk = cups * coffee_ingredients["milk"]
req_beans = cups * coffee_ingredients["coffee beans"]

print(f'For {cups} cups of coffee you will need:\n'
      f'{req_water} ml of water\n'
      f'{req_milk} ml of milk\n'
      f'{req_beans} g of coffee beans')
