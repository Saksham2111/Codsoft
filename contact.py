contacts = {}

def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"{name} has been added to your contacts.")

def view_contact(name):
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
    else:
        print(f"{name} not found in your contacts.")

def search_contact(name):
    for contact_name in contacts.keys():
        if name in contact_name:
            print(contact_name)

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View a contact")
        print("3. Search for contacts")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            name = input("Enter the name of the contact: ")
            view_contact(name)
        elif choice == '3':
            name = input("Enter a name or part of a name to search for: ")
            search_contact(name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
