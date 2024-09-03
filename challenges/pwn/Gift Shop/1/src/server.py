import sys

flag = "flag-dB48zVY2RZvjSnjb"

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
    print("4. Return items")
    print("5. Exit")

def main():
    print()
    print("Welcome to the gift shop!")
    balance = 60
    choice = ""

    while choice != "5":
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
                quantity = int(input("Enter quantity: "))
            except:
                print("Invalid quantity")
                print()
                continue

            if item == "1":
                balance -= quantity * 0.99
                inventory[0] += quantity
                print(f"You bought {quantity} postcard" + ("s" if quantity > 1 else ""))
            elif item == "2":
                balance -= quantity * 15.99
                inventory[1] += quantity
                print(f"You bought {quantity} plushie" + ("s" if quantity > 1 else ""))
            elif item == "3":
                balance -= quantity * 29.99
                inventory[2] += quantity
                print(f"You bought {quantity} t-shirt" + ("s" if quantity > 1 else ""))
            elif item == "4":
                balance -= quantity * 99.99
                inventory[3] += quantity
                print(f"You bought {quantity} flag" + ("s" if quantity > 1 else ""))
            else:
                print("Invalid choice")
            print()


        ## RETURN ITEMS
        elif choice == "4":

            print("You currently have:")
            print(f"1. {inventory[0]} postcard" + ("s" if inventory[0] > 1 else ""))
            print(f"2. {inventory[1]} plushie" + ("s" if inventory[1] > 1 else ""))
            print(f"3. {inventory[2]} t-shirt" + ("s" if inventory[2] > 1 else ""))
            print(f"4. {inventory[3]} flag" + ("s" if inventory[3] > 1 else ""))

            try:
                item = input("Enter your choice: ")
            except:
                print("Invalid choice")
                print()
                continue

            if item < "1" or item > "4":
                print("Invalid choice")
                print()
                continue

            try:
                quantity = int(input("Enter quantity: "))
            except:
                print("Invalid quantity")
                print()
                continue

            if item == "1":
                balance += quantity * 0.99
                inventory[0] -= quantity
                print(f"You returned {quantity} postcard" + ("s" if quantity > 1 else ""))
            elif item == "2":
                balance += quantity * 15.99
                inventory[1] -= quantity
                print(f"You returned {quantity} plushie" + ("s" if quantity > 1 else ""))
            elif item == "3":
                balance += quantity * 29.99
                inventory[2] -= quantity
                print(f"You returned {quantity} t-shirt" + ("s" if quantity > 1 else ""))
            elif item == "4":
                balance += quantity * 99.99
                inventory[3] -= quantity
                print(f"You returned {quantity} flag" + ("s" if quantity > 1 else ""))
            else:
                print("Invalid choice")
            print()


        ## UNPACKAGE FLAG
        elif choice == "3":
            if inventory[3] <= 0:
                print("You do not have any flags.")
                print()
            elif inventory[3] > 0:
                print(f"Unpackaging {inventory[3]} flag" + ("s" if inventory[3] > 1 else "") + "...")
                print(flag)
                print("Thank you for shopping with us!")
                sys.exit()

        else:
            print("Invalid choice")
            print()
            

main()
print("Thank you for shopping with us!")