import json
import os

class OrderNode:
    def __init__(self, items):
        self.items = items
        self.next = None

class OrderQueue:
    def __init__(self, filename):
        self.front = None
        self.rear = None
        self.filename = filename
        self.load_orders()  # Load orders from file at initialization

    def enqueue(self, items):
        new_node = OrderNode(items)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.save_orders()  # Save orders after adding

    def dequeue(self):
        if not self.front:
            return None
        temp = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return temp.items

    def is_empty(self):
        return self.front is None

    def get_all_orders(self):
        orders = []
        current = self.front
        while current:
            orders.append(current.items)
            current = current.next
        return orders

    def save_orders(self):
        with open(self.filename, 'w') as file:
            current = self.front
            while current:
                file.write(json.dumps(current.items) + "\n")
                current = current.next

    def load_orders(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r') as file:
            for line in file:
                items = json.loads(line.strip())
                self.enqueue(items)  # Re-add each order from the file