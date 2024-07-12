contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact for {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = {name: info for name, info in contacts.items() if search_term in name or search_term in info['phone']}
    
    if not found_contacts:
        print("No contacts found.")
        return
    
    print("\nSearch Results:")
    for name, info in found_contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print("Contact not found.")
        return
    
    phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
    email = input(f"Enter new email (current: {contacts[name]['email']}): ")
    address = input(f"Enter new address (current: {contacts[name]['address']}): ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact for {name} updated successfully!")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name not in contacts:
        print("Contact not found.")
        return
    
    del contacts[name]
    print(f"Contact for {name} deleted successfully!")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
