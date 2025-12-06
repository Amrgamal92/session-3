#  Create the dictionary
contacts = {}

# Add three contacts
contacts["Ali"] = "02-1234"
contacts["omar"] = "02-5678"
contacts["Amr"] = "02-9012"

#  Print all names in the contact book
print("Contact names:")
for name in contacts:
    print(name)

# Allow the user to search for a contact
search_name = input("\nEnter a name to search: ")

if search_name in contacts:
    print(f"Phone number for {search_name}: {contacts[search_name]}")
else:
    print("Contact not found.")