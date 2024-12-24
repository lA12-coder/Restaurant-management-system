import json
import os

class MenuNode:
    def __init__(self, name, price):
        self.data = name
        self.price = price
        self.next = None
        self.prev = None

class MenuManager:
    def __init__(self, filename):
        self.head = None  # head is initialized to None
        self.filename = filename
        self.load_menu()  # Load menu items from file at initialization

    def add_item(self, name, price):
        new_node = MenuNode(name, price)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.save_menu()  # Save after adding an item

    def remove_item(self, name):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == name:
                # Check if there is only one node
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    # If the first item is deleted, move the head to the next node
                    if current == self.head:
                        self.head = current.next
                self.save_menu()  # Save after removing an item
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def load_menu(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                item_data = json.loads(line.strip())
                self.add_item(item_data['name'], item_data['price'])

    def save_menu(self):
        with open(self.filename, 'w') as file:
            current = self.head
            if current is None:
                return
            while True:
                file.write(json.dumps({"name": current.data, "price": current.price}) + "\n")
                current = current.next
                if current == self.head:
                    break

    def get_menu(self):
        menu_items = []
        if not self.head:
            return menu_items
        current = self.head
        while True:
            menu_items.append({"name": current.data, "price": current.price})
            current = current.next
            if current == self.head:
                break
        return menu_items

    def sort_menu_by_name(self):
        if not self.head:
            return

        menu_items = self.get_menu()

        # Implement insertion sort algorithm
        n = len(menu_items)
        for i in range(1, n):
            key = menu_items[i]
            j = i - 1
            while j >= 0 and menu_items[j]["name"] > key["name"]:
                menu_items[j + 1] = menu_items[j]
                j -= 1
            menu_items[j + 1] = key

        self.head = None  # Clear the existing list
        for item in menu_items:
            self.add_item(item["name"], item["price"])  # Re-add sorted items

    def sort_menu_by_price(self):
        if not self.head:
            return

        menu_items = self.get_menu()

        # Insertion sort by price
        n = len(menu_items)
        for i in range(1, n):
            key = menu_items[i]
            j = i - 1
            while j >= 0 and menu_items[j]["price"] > key["price"]:
                menu_items[j + 1] = menu_items[j]
                j -= 1
            menu_items[j + 1] = key

        self.head = None  # Clear the existing list
        for item in menu_items:
            self.add_item(item["name"], item["price"])

    def update_item(self, name, new_name=None, new_price=None):
        if not self.head:
            return False

        current = self.head
        while True:
            if current.data == name:
                if new_name is not None:
                    current.data = new_name
                if new_price is not None:
                    current.price = new_price
                self.save_menu()  # Save after updating an item
                return True
            current = current.next
            if current == self.head:
                break
        return False