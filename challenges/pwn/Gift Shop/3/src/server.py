import sys

flag = "flag-f5PbQgAxhVwpOTiK"

inventory = [0, 0, 0, 0]

def print_inventory():
    print("What would you like to buy?")
    print("1. Souvenir postcard - $0.99")
    print("2. Plushie - $15.99")
    print("3. T-shirt - $29.99")
    print("4. Collector Flag - $99.99")
    print("5. Exit")

def print_menu(balance):
    print(f"You have ${balance:.2f} to spend.")
    print("What would you like to do?")
    print("1. View inventory")
    print("2. Purchase items")
    print("3. Unpackage flag")
    print("4. Exit")

def main():
    print()
    print("Welcome to the gift shop!")
    balance = 60
    choice = ""

    while choice != "4":
        print_menu(balance=balance)
        choice = input("Enter your choice: ")

        ## VIEW INVENTORY
        if choice == "1":
            print("You currently have:")
            print(f"{inventory[0]} postcard" + ("s" if inventory[0] > 1 else ""))
            print(f"{inventory[1]} plushie" + ("s" if inventory[1] > 1 else ""))
            print(f"{inventory[2]} t-shirt" + ("s" if inventory[2] > 1 else ""))
            print(f"{inventory[3]} flag" + ("s" if inventory[3] > 1 else ""))
            print()

        ## PURCHASE ITEMS
        if choice == "2":
            print_inventory()
            item = input("Enter your choice: ")

            if item < "1" or item > "4":
                print("Invalid choice")
                print()
                continue

            try:
                quantity = float(input("Enter quantity: "))
            except:
                print("Invalid quantity")
                print()
                continue

            if quantity <= 0:
                print("Invalid quantity")
                print()
                continue

            if item == "1":
                if (quantity * 0.99) > balance:
                    print("Not enough money")
                    continue
                else:
                    balance -= quantity * 0.99
                    inventory[0] += quantity
                    print(f"You bought {quantity} postcard" + ("s" if quantity > 1 else ""))
            elif item == "2":
                if (quantity * 15.99) > balance:
                    print("Not enough money")
                    continue
                else:
                    balance -= quantity * 15.99
                    inventory[1] += quantity
                    print(f"You bought {quantity} plushie" + ("s" if quantity > 1 else ""))
            elif item == "3":
                if (quantity * 29.99) > balance:
                    print("Not enough money")
                    continue
                else:
                    balance -= quantity * 29.99
                    inventory[2] += quantity
                    print(f"You bought {quantity} t-shirt" + ("s" if quantity > 1 else ""))
            elif item == "4":
                if (quantity * 99.99) > balance:
                    print("Not enough money")
                    continue
                else:
                    balance -= quantity * 99.99
                    inventory[3] += quantity
                    print(f"You bought {quantity:.2f} flag" + ("s" if quantity > 1 else ""))
            else:
                print("Invalid choice")
            print()

        ## UNPACKAGE FLAG
        elif choice == "3":
            if inventory[3] == 0:
                print("You do not have any flags.")
                print()
            elif inventory[3] > 0:
                print(f"Unpackaging {inventory[3]} flag...")
                print(flag)
                print("Thank you for shopping with us!")
                sys.exit()
            

main()
print("Thank you for shopping with us!")