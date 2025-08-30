import json
import os

try : 
    with open("contacts.json", 'r') as contactsFile:
        contacts = json.load(contactsFile) 
except: 
    contacts = []

def add_contact(listContact):
    contact = {}
    contact["name"] = input("please enter Name of Contact: ")
    contact["number"] = (input("please enter Phone Number: "))
    listContact.append(contact)
    save_contacts(listContact)

def show_contacts(listContact):
    for i, contact in enumerate(listContact, start=1):
        print(f"{i}. {contact['name']} - Phone Number: {contact['number']}")

def find_contact(listContact,item):
    for contact in listContact :
        if contact["name"].lower() == item.lower() :
            return contact
    return False

def save_contacts(listContact):
    if len(listContact) > 0:
        with open("contacts.json", 'w') as contactsFile:
            json.dump(listContact, contactsFile, indent=4)
    else :
        if os.path.exists("contacts.json"):
            os.remove("contacts.json")

def edit_contact(item):
    new_name = input(f"edit Name ({item['name']}): ")
    new_number = input(f"edit Phonenumber ({item['number']}): ")
    if new_name.strip() :
        item["name"] = new_name
    if new_number.strip() :
        item["number"] = new_number
    print(f"Updated: {item['name']} - {item['number']}")
    print("Edit Seccessful")


while True :    
    print("1 - Add Contact")
    print("2 - Show Contacts")
    print("3 - Search Contact")
    print("4 - Delete Contact")
    print("5 - Edit by Name")
    print("6 - Exit")
    inputMenu = int(input("Choose your action: "))
    print(" ---------------- ")
    if inputMenu == 1 :
        add_contact(contacts)
        print("Successful")
        print(" ---------------- ")
    elif inputMenu == 2 :
        if len(contacts) > 0 :
            print("Show all contancts:\n")
            show_contacts(contacts)
        else:
            print("Contact is Empty!")
        print(" ---------------- ")
    elif inputMenu == 3 :
        print("Search Contact .... \n")
        searchItem = input("Search by Name is: ")
        search_contant = find_contact(contacts,searchItem)
        if search_contant :
            print(f"{search_contant['name']} - Phone Number: {search_contant['number']}")
            print(" ---------------- ")
        else :
            print("Not Found")
            print(" ---------------- ")
    elif inputMenu == 4 :
        deleteItem = input("Delete Contact by Name: ")
        delete = find_contact(contacts,deleteItem)
        if delete :
            confirm = input(f"Are you sure to delete {delete['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.remove(delete)
            save_contacts(contacts)
            print("Deleted!")
            print(" ---------------- ")
        else : 
            print("Not Found")
            print(" ---------------- ")
    elif inputMenu == 5 :
        print("Edit By Name")
        print(" ---------------- \n")
        editItem = input("Edit by Name is: ")
        edit = find_contact(contacts,editItem)
        if edit :
            edit_contact(edit)
            save_contacts(contacts)
            print(" ---------------- ")
        else :
            print("Not Found")
            print(" ---------------- ")
    else : break