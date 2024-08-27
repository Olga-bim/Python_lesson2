import json
import os
from enum import Enum

contacts = []

file_path = "myContacts.json"

class Selection(Enum):
    ADD = 1
    DELETE = 2
    EDIT = 3
    SHOW = 4
    CLEAR =5
    SEARCH =6
    EXIT =7
def menu():
    for item in Selection: print(f'{item.value} -  {item.name}')
    return   Selection(int( input("your selection?")))

def getUserData(contacts):
    userName = input("Enter your name?")
    email = input("email?")
    contacts.append({"user": userName, "email": email})

def clearScreen():
      os.system('cls' if os.name == 'nt' else 'clear')

def showContacts(contacts):
    print("All contacts")
    print(contacts)


def searchContact(contacts):
    search_name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if search_name.lower() in contact['user'].lower():
            print(f"Name: {contact['user']}, Email: {contact['email']}")
            found = True
    if not found:
        print("No contact found with that name.")

def exit_app(contacts):
    with open('myContacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)        

def main():
     
     with open('myContacts.json', 'r') as file:
        contacts = json.load(file)
        print(contacts)

        while True:
  

            userSelection = menu()

            if userSelection == Selection.EXIT: 
                 exit_app()(contacts)
                 return
            if userSelection == Selection.ADD: 
                getUserData(contacts)
                pass
            if userSelection == Selection.DELETE: 
                # delete
                pass
            if userSelection == Selection.EDIT: 
                # print("edit")
                pass
            if userSelection == Selection.CLEAR: 
                clearScreen()
            if userSelection == Selection.SHOW: 
                showContacts(contacts)
            if userSelection == Selection.SEARCH:
                searchContact(contacts)
                



if __name__== "__main__":
        main()

