import json
import os

DATA_FILE = 'users.json'


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def authenticate(users):
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")
    if username in users and users[username]['pin'] == pin:
        print("Login successful!")
        return username
    else:
        print("Invalid credentials.")
        return None

def show_menu():
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

def atm_interface():
    users = load_data()

    username = authenticate(users)
    if not username:
        return

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            print(f"Balance: ₹{users[username]['balance']}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            users[username]['balance'] += amount
            users[username]['history'].append(f"Deposited ₹{amount}")
            print("Deposit successful.")
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= users[username]['balance']:
                users[username]['balance'] -= amount
                users[username]['history'].append(f"Withdrew ₹{amount}")
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            print("\nTransaction History:")
            for entry in users[username]['history']:
                print("-", entry)
        elif choice == '5':
            save_data(users)
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Try again.")

# Initial user setup (you can pre-fill for testing)
def create_user():
    users = load_data()
    username = input("Create a username: ")
    pin = input("Set a 4-digit PIN: ")
    if username in users:
        print("User already exists!")
    else:
        users[username] = {
            'pin': pin,
            'balance': 0.0,
            'history': []
        }
        save_data(users)
        print("User created successfully!")


if __name__ == '__main__':
    print("1. Create New User")
    print("2. Login to ATM")
    option = input("Choose an option: ")

    if option == '1':
        create_user()
    elif option == '2':
        atm_interface()
