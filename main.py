from user_management import AuthManager
from menu import MenuManager
from order import OrderQueue

def main():
    user_filename = 'users.txt'
    menu_filename = 'menu.txt'  # File for storing menu items
    order_filename = "order.txt"
    auth_manager = AuthManager(user_filename)
    menu_manager = MenuManager(menu_filename)  # Initialize with menu filename
    order_queue = OrderQueue(order_filename)

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth_manager.register(username, password):
                print("Registration successful!")
            else:
                print("User already exists.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth_manager.login(username, password):
                print("Login successful!")
                while True:
                    print("\n1. Add Menu Item")
                    print("2. Remove Menu Item")
                    print("3. View Menu")
                    print("4. Sort Menu")
                    print("5. Update Menu")
                    print("6. Create Order")
                    print("7. View Orders")
                    print("8. Change Password")
                    print("9. Logout")
                    menu_choice = input("Choose an option: ")

                    if menu_choice == "1":
                        name = input("Enter item name: ")
                        price = float(input("Enter item price: "))
                        menu_manager.add_item(name, price)
                        print("Menu item added.")

                    elif menu_choice == "2":
                        name = input("Enter item name to remove: ")
                        if menu_manager.remove_item(name):
                            print("Menu item removed.")
                        else:
                            print("Item not found.")

                    elif menu_choice == "3":
                        menu = menu_manager.get_menu()
                        if menu:
                            print("\nMenu Items:")
                            for item in menu:
                                print(f"{item['name']}: ${item['price']:.2f}")
                        else:
                            print("Menu is empty.")

                    elif menu_choice == "4":
                        print("\n1, Sort by name")
                        print("2, Sort by price")
                        sort_choice = input("Choose the sorting method: ")
                        if sort_choice == "1":
                            menu_manager.sort_menu_by_name()
                            print("Menu sorted.")
                        elif sort_choice == "2":
                            menu_manager.sort_menu_by_price()
                            print("Menu sorted.")
                        else:
                            print("Wrong choice!")

                    elif menu_choice == "5":
                        name = input("Enter the name of the item to update: ")
                        new_name = input("Enter new name (or press Enter to keep current): ")
                        new_price = input("Enter new price (or press Enter to keep current): ")

                        # Convert new_price to float if provided, else None
                        new_price = float(new_price) if new_price else None
                        updated = menu_manager.update_item(name, new_name if new_name else None, new_price)

                        if updated:
                            print("Menu item updated successfully.")
                        else:
                            print("Item not found.")
                    elif menu_choice == "6":
                        items = []
                        while True:
                            item_name = input("Enter menu item name (or type 'done' to finish): ")
                            if item_name.lower() == 'done':
                                break
                            items.append({"name": item_name})  # Assuming each item has a name
                        order_queue.enqueue(items)
                        print("Order placed successfully!")

                    elif menu_choice == "7":
                        orders = order_queue.get_all_orders()
                        if orders:
                            print("\nOrders:")
                            for i, order in enumerate(orders):
                                print(f"Order {i + 1}: {order}")
                        else:
                            print("No orders placed.")

                    elif menu_choice == "8":
                        old_password = input("Enter old password: ")
                        new_password = input("Enter new password: ")
                        auth_manager.change_password(username, old_password, new_password)

                    elif menu_choice == "9":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid option.")
            else:
                print("You are not registered!")
        elif choice == "3":
            print("Exiting the application.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()