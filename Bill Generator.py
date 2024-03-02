class BillGenerator:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = {'name': name, 'quantity': quantity, 'price': price}
        self.items.append(item)

    def generate_bill(self):
        total_amount = 0
        print("\n********** Your Bill **********")
        print("Item\t\tQuantity\tPrice")
        print("--------------------------------")
        for item in self.items:
            item_total = item['quantity'] * item['price']
            total_amount += item_total
            print(f"{item['name']}\t\t{item['quantity']}\t\t${item['price']:.2f}\t\t${item_total:.2f}")
        print("--------------------------------")
        print(f"Total Amount: ${total_amount:.2f}")
        print("********** Thank you! **********\n")

# Example usage:
if __name__ == "__main__":
    bill_generator = BillGenerator()

    # Add items to the bill
    bill_generator.add_item("Item 1", 2, 10.50)
    bill_generator.add_item("Item 2", 1, 5.75)
    bill_generator.add_item("Item 3", 3, 8.20)

    # Generate and print the bill
    bill_generator.generate_bill()
