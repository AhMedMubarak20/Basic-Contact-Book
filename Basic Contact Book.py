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
Project 22: Image Downloader

python
Copy code
import requests

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print("Image downloaded.")

image_url = input("Enter the image URL: ")
file_name = input("Enter the desired file name: ")
download_image(image_url, file_name)
Feel free to ask for more project code whenever you're ready!





