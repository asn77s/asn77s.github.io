"""Shopping cart practice. Prices use integer cents for exact totals."""


def make_shelf():
    return {
        "Frosted Flakes": {"price": 299, "quantity": 2},
        "Eggs": {"price": 599, "quantity": 2},
        "sourdough loaf": {"price": 399, "quantity": 2},
    }


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
    while True:
        choice = input("\n1. Add item\n2. Remove item\n3. View total\n4. Quit\nChoose: ").strip()
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
        else:
            print("Invalid input. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
