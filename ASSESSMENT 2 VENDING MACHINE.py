items = {
    # SNACKS GROUP (9 items)
    "S1": ["Cheetos", 2.50, 5],
    "S2": ["Lays", 2.50, 5],
    "S3": ["Pringles", 4, 5],
    "S4": ["Cookies", 5, 0],
    "S5": ["Doritos", 3, 8],
    "S6": ["Popcorn", 5, 10],
    "S7": ["Oreo", 3, 10],
    "S8": ["Bourbon", 4, 7],
    "S9": ["Hide & Seek", 4, 5],
    # CHOCOLATE GROUP (5 items)
    "C1": ["Kit Kat", 3, 5],
    "C2": ["Twix", 1.75, 6],
    "C3": ["Bounty", 2.75, 7],
    "C4": ["Mars", 1, 5],
    "C5": ["Lollipops", 0.75, 0],
    # DRINKS GROUP (11 items)
    "D1": ["Coca Cola", 2.75, 6],
    "D2": ["Sprite", 3.50, 6],
    "D3": ["Water", 1, 10],
    "D4": ["Lemonade", 2.80, 8],
    "D5": ["Fanta", 3, 5],
    "D6": ["7 UP", 1.75, 0],
    "D7": ["Orange Juice", 7.75, 10],
    "D8": ["Cold Coffee", 9.75, 9],
    "D9": ["Iced Tea", 10.50, 6],
    "D10": ["Milkshake", 15.75, 5],
    "D11": ["Energy Drink", 8.50, 7],
}

# DISPLAYS THE MENU
def show_menu():
    print("\n=============== VENDING MACHINE ===============\n")
    print(f"{'Code':<6} {'Item':<20} {'Price':<10} {'Stock':<6}")
    print("-" * 50)
    for code in sorted(items.keys()):
        name, price, stock = items[code]
        print(f"{code:<6} {name:<20} {price:>7.2f} AED   {stock:<6}")
    print("-" * 50)
    print()

# FUNCTION USED TO HANDLE USER PAYMENT UNTIL FULL AMOUNT RECEIVED    
def take_payment(price):
    total_paid = 0
    while total_paid < price:
        try:
            money = float(input(f"Insert money ({price - total_paid:.2f} AED remaining): "))
            if money <= 0:
                print("Enter A Valid Amount.\n")
            else:
                total_paid += money
        except ValueError:
            print("Invalid Input. Try Again.")
    return total_paid - price

# SUGGESTS ANOTHER ITEM FROM THE SAME CATEGORY [S, C or D]
def suggest_item(choice):
    category = choice[0]
    for key in items:
        if (
            key[0] == category
            and key != choice
            and items[key][2] > 0
        ):
            return key
    return None

# PRINTS THE RECEIPT AFTER PURCHASE
def print_receipt(cart, total_cost, total_change):
    print("\n========== RECEIPT ==========\n")
    for name, price in cart:
        print(f"{name:<15} AED{price:.2f}")
    print("-" * 25)
    print(f"TOTAL:          AED{total_cost:.2f}")
    print()
    print(f"CHANGE:         AED{total_change:.2f}\n")
    print("Thank You For Your Purchase!\n")
    print("=============================\n")

# FUNCTION USED TO HANDLE THE PURCHASING PROCESS    
def purchase():
    cart = []
    total_change = 0
    while True:
        show_menu()
        code = input("Enter Item Code (or 0 To Exit): ").upper()
        print()
        if code == "0":
            break
        if code not in items:
            print("Invalid Code.\n")
            continue
        name, price, stock = items[code]
        if stock <= 0:
            print(f"{name} Is Out Of Stock.\n")
            continue
        change = take_payment(price)
        items[code][2] -= 1
        print(f"\nDispensed: {name}\n")
        print(f"Change: {change:.2f} AED\n")
        cart.append((name, price))
        total_change += change
        suggestion = suggest_item(code)
        if suggestion:
            s_name, s_price, _ = items[suggestion]
            print(f"You May Also Like: {s_name} ({s_price:.2f} AED)\n")
        more = input("Buy Another Item? (y/n): ").lower()
        print()
        if more != "y":
            break
    if cart:
        total_cost = sum(price for _, price in cart)
        print_receipt(cart, total_cost, total_change)
    else:
        print("No Items Purchased.\n")

# MAIN PROGRAM LOOP        
def main():
    while True:
        purchase()
        again = input("Use Machine Again? (y/n): ").lower()
        if again != "y":
            print()
            print("HAVE A NICE DAY!")
            break

        
if __name__ == "__main__":
    main()