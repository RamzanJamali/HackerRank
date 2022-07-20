#Task
#Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for. 
# For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for name is not found, print Not found instead.


phonebook = {}
# only first name and phone number is entered
phonebook_size = int(input())

# Add contacts to dictionary
for i in range(phonebook_size):
    contact = input()
    contact_list = contact.split()
    contact_name = contact_list[0]
    contact_number = int(contact_list[1])
    phonebook[contact_name] = contact_number
    
# Search for contacts
while True:  
    # Get first_name of contact
    try:  
        search_contact = input()
        if len(search_contact) == 0:
            break
    except:
        break
    # Search and return phone number if there is any
    try:
        contact_found = phonebook[search_contact]
        output = "{}={}".format(search_contact,contact_found)
        print(output)
        
    except:
        print("Not found")
