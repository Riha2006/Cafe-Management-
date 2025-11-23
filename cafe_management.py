def show_menu(menu):
    print("------ Cafe Menu ------")
    for item_id, item_info in menu.items():
        print(f"{item_id}. {item_info['name']} - ${item_info['price']:.2f}")
    print("-----------------------")

def take_order(menu):
    order = {}
    while True:
        try:
            choice = input("Enter the item number to order (or 'q' to finish): ")
            if choice.lower() == 'q':
                break
            item_id = int(choice)
            if item_id not in menu:
                print("Invalid item number. Please try again.")
                continue
            quantity = int(input(f"Enter quantity for {menu[item_id]['name']}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            if item_id in order:
                order[item_id] += quantity
            else:
                order[item_id] = quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return order

def calculate_bill(order, menu):
    total = 0
    for item_id, quantity in order.items():
        total += menu[item_id]['price'] * quantity
    return total

def print_receipt(order, menu):
    print("\n------- Receipt -------")
    total = 0
    for item_id, quantity in order.items():
        name = menu[item_id]['name']
        price = menu[item_id]['price']
        cost = price * quantity
        total += cost
        print(f"{name} x {quantity} = ${cost:.2f}")
    print("-----------------------")
    print(f"Total: ${total:.2f}")
    print("Thank you for visiting!")

def main():
    menu = {
        1: {'name': 'Coffee', 'price': 2.50},
        2: {'name': 'Tea', 'price': 2.00},
        3: {'name': 'Sandwich', 'price': 5.00},
        4: {'name': 'Cake', 'price': 3.00},
        5: {'name': 'Juice', 'price': 4.00},
    }

    print("Welcome to the Cafe Management System!")
    while True:
        show_menu(menu)
        order = take_order(menu)
        if not order:
            print("No items ordered. Exiting.")
            break
        print_receipt(order, menu)

        more = input("Would you like to place another order? (y/n): ")
        if more.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
