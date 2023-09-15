MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

machine ={
    "water": 300,
    "milk": 100,
    'coffee': 100,
    'money': 0
}

def print_report():
    print(f"Water: {machine['water']}ml")
    print(f"Milk: {machine['milk']}ml")
    print(f"Coffee: {machine['coffee']}g")
    print(f"Money: ${machine['money']}")

def check_resources(brew):
    brew_req = brew["ingredients"]
    for ing in brew_req:
        if brew_req[ing] > machine[ing]:
            return False, f"There is not enough {ing}"
    return True, ""

def process_coins():
    user_money = 0
    print("Please insert coins.")
    user_money += int(input("How many quarters?: ")) * 0.25
    user_money += int(input("How many dimes?: ")) * 0.1
    user_money += int(input("How many nickles?: ")) * 0.05
    user_money += int(input("How many pennies?: ")) * 0.01

    return user_money

def update_resources(brew):
    brew_req = brew["ingredients"]
    for ing in brew_req.keys():
        machine[ing] = machine[ing] - brew_req[ing]
    machine['money'] += brew["cost"]

def make_coffee(brew_name):
    user_money = 0
    is_ingredient = False
    is_ingredient, msg = check_resources(MENU[brew_name])
    if not is_ingredient:
        print(msg)
        return False
    
    user_money = process_coins()
    brew_cost = float(MENU[brew_name]['cost'])
    if user_money < brew_cost:
        print(f"There is not enough money.\nThe brew price is {brew_cost}\nTake your money back!")
        return False

    print(f"Here is your {brew_name} ☕. Enjoy!")
    if user_money > brew_cost:
        print(f"Here is {user_money - brew_cost} dollars in change.")
    
    update_resources(MENU[brew_name])

    return True


def vending_machine():
    machine_on = True
    options = list(MENU.keys())
    options.extend(["off", "report"])

    while machine_on:
        user_option = input(f"What would you like ({MENU.keys()}): ")

        if user_option not in options:
            continue
        if user_option == "off":
            machine_on = False
            break
        elif user_option == "report":
            print_report()
        else:
            make_coffee(user_option)
    
    print("Machine is OFF")
if __name__ == '__main__':
    vending_machine()
