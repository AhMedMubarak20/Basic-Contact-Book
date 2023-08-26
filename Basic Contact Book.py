contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
    else:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")





