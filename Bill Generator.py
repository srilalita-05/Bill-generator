def generate_bill():
    items = []
    total_amount = 0

    print("Welcome to the Bill Generator!")

    while True:
        item = input("Enter item name (or 'completed' to finish): ")
        if item.lower() == 'completed':
            break

        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))

        item_total = quantity * price
        total_amount += item_total

        items.append({'item': item, 'quantity': quantity, 'price': price, 'item_total': item_total})

    # Calculate GST (18%)
    gst_amount = total_amount * 0.18

    # Calculate discount (10%)
    discount_amount = total_amount * 0.10

    # Apply discount
    total_amount -= discount_amount

    # Display the bill
    print("\n********** Your Bill **********")
    print("Item\t\tQuantity\tPrice\t\tTotal")
    print("----------------------------------------")
    for item in items:
        print(f"{item['item']}\t\t{item['quantity']}\t\t${item['price']:.2f}\t\t${item['item_total']:.2f}")

    print("----------------------------------------")
    print(f"Total Amount:\t\t\t\t\t${total_amount:.2f}")
    print(f"GST (18%):\t\t\t\t\t${gst_amount:.2f}")
    print(f"Discount (10%):\t\t\t\t-${discount_amount:.2f}")
    print("----------------------------------------")
    print(f"Final Amount:\t\t\t\t\t${total_amount + gst_amount - discount_amount:.2f}")
    print("********** Thank you! **********\n")

# Run the bill generation function
generate_bill()
