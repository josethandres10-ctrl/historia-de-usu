from functions import add_item, show_items, get_statistics
from validations import validate_option

# Main menu function
def start_menu():
    running = True

    while running:
        try:
            option = int(input("""
Choose an option (1-4):
1. Add product
2. Show inventory
3. Calculate statistics
4. Exit
→ """))

            validate_option(option)

            if option == 1:
                add_item()
            elif option == 2:
                show_items()
            elif option == 3:
                get_statistics()
            elif option == 4:
                print("Closing system...")
                running = False
            else:
                print("Invalid option, try again\n")

        except ValueError:
            print("Error: please enter a valid number\n")


start_menu()