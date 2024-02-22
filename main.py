import data
import cashier
import sandwich_maker

from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

class Cashier:
    def __init__(self):
        self.some_attribute = ""

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        large_dollars = int(input("how large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total_cents = large_dollars * 100 + half_dollars * 50 + quarters * 25 + nickels * 5
        total_dollars = total_cents / 100
        return total_dollars

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False

class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < amount:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if self.check_resources(order_ingredients):
            for ingredient, amount in order_ingredients.items():
                self.machine_resources[ingredient] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")
                return True
            else:
                print("Sorry, there is not enough resources to make the sandwich.")
                return False
    def show_report(self):
        for resource, amount in self.machine_resources.items():
            print(f"{resource.capitalize()}: {amount} {'ounce(s)' if resource == 'cheese' else 'slice(s)'}")

    def main():
        machine = sandwich_maker_instance  # Correct instance variable name

        while True:
            user_input = input("What would you like? (small/medium/large/off/report): ").lower()

            if user_input == "off":
                break
            elif user_input == "report":
                machine.show_report()
            elif user_input in data.recipes:
                sandwich_size = user_input
                order_ingredients = data.recipes[sandwich_size]["ingredients"]

                if machine.check_resources(order_ingredients):
                    print("Please insert coins.")
                    coins_inserted = machine.process_coins()
                    sandwich_cost = data.recipes[sandwich_size]["cost"]

                    if machine.transaction_result(coins_inserted, sandwich_cost):
                        machine.make_sandwich(sandwich_size, order_ingredients)
                        continue
                else:
                    print("Sorry, there is not enough resources to make the sandwich.")
            else:
                print("Invalid input. Please enter a valid option.")

    if __name__ == "__main__":
        main()
