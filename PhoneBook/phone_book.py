def phone_book():

  global contents
  open = True
  contents = []

  class Entry:
    def __init__(self, name, phone, email):
      self.name = name
      self.phone = phone
      self.email = email

  def add_contact():
    global contents
    print("Enter contact information. Put 'none' to skip unknown values.")
    new_name = input("Contact name: ")
    new_phone = input("Contact phone: ")
    new_email = input("Contact email: ")
    new_entry = Entry(new_name, new_phone, new_email)
    contents.append(new_entry)

  def retrieve_contact():
    find_contact = input("Enter contact name: ")
    for i in contents:
      if (i.name == find_contact):
        print(i.name)
        print(i.phone)
        print(i.email)
        return
    print('Contact not found.')

  def remove_contact():
    delete_contact = input("Enter contact to remove: ")
    print("")
    for i in range(len(contents)):
      if (contents[i].name == delete_contact):
        print(contents[i].name)
        print(contents[i].phone)
        print(contents[i].email)
        verify = input('\nDelete this contact? Type "yes" to confirm. ')
        if (verify.lower() == "yes"):
          del contents[i]
          print('Contact removed.')
          return
    print('Contact not found.')

  def list_all():
    print("")
    for i in contents:
      print(i.name)
      print(i.phone)
      print(i.email)
      print("")


  print('Welcome to your phonebook.')

  while (open == True):
    option = input('Would you like to add, retrieve, or remove a contact? Type "list" to list all contacts. Type "close" to close. ')
    option = option.lower()
    if (option == "close"):
      open = False
    if (option == "add"):
      add_contact()
    if (option == "retrieve"):
      if (len(contents) == 0):
        print('Your phone book is empty.')
      else:
        retrieve_contact()
    if (option == "remove"):
      if (len(contents) == 0):
        print('Your phone book is empty.')
      else:
        remove_contact()
    if (option == "list"):
      if (len(contents) == 0):
        print('Your phone book is empty.')
      else:
        list_all()

phone_book()