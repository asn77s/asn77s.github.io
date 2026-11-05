"""Shopping cart practice. Prices use integer cents for exact totals."""


import random


PRODUCT_NAMES = ['Frosted Flakes', 'Eggs', 'sourdough loaf', 'Milk', 'Apples', 'Bananas', 'Rice', 'Pasta', 'Chicken', 'Cheese', 'Orange juice', 'Yogurt']


def make_shelf():
    # Generate prices once per session, from $1.00 to $9.99.
    return {name: {"price": random.randint(100, 999), "quantity": 2}
            for name in PRODUCT_NAMES}


def add_item(shelf, cart, name):
    if name not in shelf:
        return "Item not found."
    if shelf[name]["quantity"] == 0:
        return "Item is out of stock."
    cart[name] = cart.get(name, 0) + 1
    shelf[name]["quantity"] -= 1
    return "Item added."


def remove_item(shelf, cart, name):
    if name not in cart:
        return "That item is not in your cart."
    cart[name] -= 1
    shelf[name]["quantity"] += 1
    if cart[name] == 0:
        del cart[name]
    return "Item removed."


def total_cost(shelf, cart):
    return sum(shelf[name]["price"] * quantity for name, quantity in cart.items())


def main():
    shelf = make_shelf()
    cart = {}
    print("Prices are randomized from $1.00 to $9.99 and stay fixed until reset.")
    while True:
        choice = input("\n1. Add item\n2. Remove item\n3. View total\n4. Quit\n5. Reset cart and prices\nChoose: ").strip()
        if choice == "1":
            for name, item in shelf.items():
                print(f"{name}: ${item['price'] / 100:.2f} ({item['quantity']} available)")
            name = input("Enter the item name exactly as shown: ").strip()
            print(add_item(shelf, cart, name))
        elif choice == "2":
            print("Cart:", cart)
            name = input("Item name to remove (one unit): ").strip()
            print(remove_item(shelf, cart, name))
        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            for name, quantity in cart.items():
                print(f"{name} x{quantity}: ${shelf[name]['price'] * quantity / 100:.2f}")
            print(f"Total: ${total_cost(shelf, cart) / 100:.2f}")
        elif choice == "4":
            print("Have a nice day!")
            break
        elif choice == "5":
            shelf = make_shelf()
            cart = {}
            print("Cart reset. New prices generated and stock restored.")
        else:
            print("Invalid input. Choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
