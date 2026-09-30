class Medicine:
    def __init__(self, name, price, stock, expiry):
        self.name = name
        self.price = float(price)
        self.stock = int(stock)
        self.expiry = str(expiry)  
        self.sold = 0  

    def display(self):
        print(f"Name: {self.name}, Price: Rs. {self.price:.2f}, Stock: {self.stock}, Expiry: {self.expiry}, Sold: {self.sold}")

    def sell(self, number):
        if number <= 0:
            print("Quantity to sell must be greater than 0.")
        elif number > self.stock:
            print(f"Not enough stock available. Current stock: {self.stock}")
        else:
            self.stock -= number
            self.sold += number
            print(f"Sold {number} unit(s) of '{self.name}'. Remaining stock: {self.stock}")
class MedicineStore:
    def __init__(self):
        self.medicines = []

    def add_medicine(self):
        name = input("Enter medicine name: ").strip()
        try:
            price = float(input("Enter medicine price: "))
            stock = int(input("Enter medicine stock: "))
        except ValueError:
            print("Invalid input! Price and stock must be numbers.")
            return

        expiry = input("Enter medicine expiry date (e.g. MM/YYYY): ").strip()
        new_med = Medicine(name, price, stock, expiry)
        self.medicines.append(new_med)
        print(f"Medicine '{name}' added successfully.\n")

    def display_all(self):
        if not self.medicines:
            print("No medicines available.\n")
            return
        print("\n--- Available Medicines ---")
        for med in self.medicines:
            med.display()
        print()

    def search_medicine(self):
        name = input("Enter medicine name to search: ").strip()
        for med in self.medicines:
            if med.name.lower() == name.lower():
                print("Medicine found:")
                med.display()
                print()
                return
        print(f"Medicine '{name}' not found.\n")

    def sell_medicine(self):
        name = input("Enter medicine name to sell: ").strip()
        for med in self.medicines:
            if med.name.lower() == name.lower():
                try:
                    number = int(input("Enter quantity to sell: "))
                except ValueError:
                    print("Invalid quantity! Must be an integer.\n")
                    return
                med.sell(number)
                print()
                return
        print(f"Medicine '{name}' not found.\n")

    def total_sales(self):
        total = sum(med.sold * med.price for med in self.medicines)
        print(f"\nTotal sales made: Rs. {total:.2f}\n")


# main program
store = MedicineStore()

while True:
    print("=" * 30)
    print("  PHARMACY MANAGEMENT SYSTEM")
    print("=" * 30)
    print("1. Add Medicine")
    print("2. Display All Medicines")
    print("3. Search Medicine")
    print("4. Sell Medicine")
    print("5. View Total Sales")
    print("6. Exit")
    print("=" * 30)

    choice = input("Enter your choice (1-6): ").strip()

    if choice == '1':
        store.add_medicine()
    elif choice == '2':
        store.display_all()
    elif choice == '3':
        store.search_medicine()
    elif choice == '4':
        store.sell_medicine()
    elif choice == '5':
        store.total_sales()
    elif choice == '6':
        print("Program exited successfully.")
        break
    else:
        print("Invalid choice! Please choose an option between 1 and 6.\n")



        
           