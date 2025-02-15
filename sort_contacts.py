import json

# Read the contacts JSON file
with open("/data/contacts.json", "r") as file:
    contacts = json.load(file)

# Sort by last_name, then by first_name
contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

# Write the sorted contacts to a new file
with open("/data/contacts-sorted.json", "w") as file:
    json.dump(contacts_sorted, file, indent=4)

print("Contacts sorted and saved in /data/contacts-sorted.json")
