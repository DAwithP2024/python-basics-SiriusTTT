# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_categories():
    print("\nAvailable Categories:")
    for i, category in enumerate(products, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = input("Please choose a category (enter the corresponding number): ")
            choice = int(choice)
            if 1 <= choice <= len(products):
                return choice - 1  # Return the zero-based index
            else:
                print("Invalid category number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_products(products_list):
    for i, (product, price) in enumerate(products_list, 1):
        print(f"{i}. {product} - ${price}")

def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == "desc"))
    return sorted_list

def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))  # Append in expected format

def display_cart(cart):
    print("\nYour Cart Contents:")
    total_cost = 0
    for product, price, quantity in cart:  # Adjust unpacking
        subtotal = price * quantity
        print(f"{product} - ${price} x {quantity} = ${subtotal}")
        total_cost += subtotal
    print(f"Total cost: ${total_cost}")
    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print("\nGenerating Receipt...")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, price, quantity in cart:
        print(f"{quantity} x {product} - ${price} = ${price * quantity}")
    print(f"Total: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    return len(name.split()) == 2 and all(part.isalpha() for part in name.split())

def validate_email(email):
    return '@' in email

def main():
    while True:
        name = input("Please enter your first and last name: ")
        if validate_name(name):
            break
        print("Invalid name. Please enter a valid name that includes a first and last name with only alphabets.")

    while True:
        email = input("Please enter your email address: ")
        if validate_email(email):
            break
        print("Invalid email. Please enter a valid email address.")

    cart = []

    while True:
        category_index = display_categories()
        category = list(products.keys())[category_index]
        print(f"\nYou selected {category}.")
        while True:
            display_products(products[category])
            print("\n1. Select a product to buy")
            print("2. Sort products by price")
            print("3. Go back to category selection")
            print("4. Finish shopping")
            option = int(input("Please choose an option: "))

            if option == 1:
                product_choice = int(input("Enter the product number: "))
                if 1 <= product_choice <= len(products[category]):
                    product = products[category][product_choice - 1]
                    quantity = int(input(f"Enter the quantity for {product[0]}: "))
                    add_to_cart(cart, product, quantity)
                    print(f"{product[0]} has been added to your cart.")
                else:
                    print("Invalid product number.")
            elif option == 2:
                sort_order = input("Enter 'asc' for ascending order, 'desc' for descending order: ")
                sorted_products = display_sorted_products(products[category], sort_order)
                display_products(sorted_products)
            elif option == 3:
                break
            elif option == 4:
                if cart:
                    total_cost = display_cart(cart)
                    address = input("Please enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. We hope you buy something from us next time. Have a nice day.")
                return
            else:
                print("Invalid option.")

if __name__ == "__main__":
    main()
