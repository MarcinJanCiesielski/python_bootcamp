from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def vending_machine():
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    machine_on = True
    options = menu.get_items()[:-1].split("/")
    options.extend(["off", "report"])
    print(options)

    while machine_on:
        user_option = input(f"What would you like ({menu.get_items()[:-1]}): ")

        if user_option not in options:
            continue
        if user_option == "off":
            machine_on = False
            break
        elif user_option == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            brew: MenuItem = menu.find_drink(user_option)

            if not coffee_maker.is_resource_sufficient(brew):
                print("There is not enough resources to make the coffee")
            if not money_machine.make_payment(brew.cost):
                print("There is not enough money to prepare the coffee")
            coffee_maker.make_coffee(brew)
    
    print("Machine is OFF")

if __name__ == '__main__':
    vending_machine()
