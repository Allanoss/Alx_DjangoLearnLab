def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def get_choice():
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit() & 1 <= int(choice) <= 4:  # Checks if the input is a digit and within the correct range
            return int(choice)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")  # Keeps prompting for valid input

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = get_choice()

        if choice == 1:
            # Add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")
        elif choice == 2:
            # Remove an item
            if shopping_list:
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from the shopping list.")
                else:
                    print(f"{item} is not in the shopping list.")
            else:
                print("The shopping list is empty.")
        elif choice == 3:
            # View the shopping list
            if shopping_list:
                print("Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
