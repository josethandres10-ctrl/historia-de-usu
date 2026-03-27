from services import *
from validations import *
from files import save_csv, load_csv

# Function that controls the whole system
def run_system():
    active = True

    while active:
        try:
            choice = int(input("""
Select an option (1-9):
1) Add item
2) View inventory
3) Find item
4) Edit item
5) Remove item
6) View stats
7) Export to CSV
8) Import from CSV
9) Quit
→ """))

            validationNum(choice)

            if choice == 1:
                addProduct()

            elif choice == 2:
                showInventory()

            elif choice == 3:
                searchProduct()

            elif choice == 4:
                updateProduct()

            elif choice == 5:
                deleteProduct()

            elif choice == 6:
                calculateStatistics()

            elif choice == 7:
                save_csv(inventory, "data_inventory.csv")

            elif choice == 8:
                loaded_data = load_csv("data_inventory.csv")

                if loaded_data:
                    print("Merging data with current inventory...")
                    inventory.extend(loaded_data)

            elif choice == 9:
                print("System closed successfully 👋")
                active = False

            else:
                print("\nInvalid selection, try again")

        except ValueError:
            print("\nOnly numbers are allowed")


run_system()