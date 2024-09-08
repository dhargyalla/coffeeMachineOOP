from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#menu_item = MenuItem()
menu_model = Menu()
coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()

is_on = True
while is_on:
    options = menu_model.get_items()
    user_choice = input(f"What would like to have? {options} ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_model.find_drink(user_choice)
        if coffee_maker_obj.is_resource_sufficient(drink):
            # payment = money_machine_obj.process_coins()
            if money_machine_obj.make_payment(drink.cost):
                coffee_maker_obj.make_coffee(drink)









