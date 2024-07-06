from users import Librarian, Member
from menu import login_menu()


# lib = Librarian("Talha", "Khan", "kasjdf", 123, '')
# lib.addBook("R.R Martin","Game of throne")
# lib.addBook("Erwin Schrodinger", "Game of Bones")
# lib.addBook("Margot Robbie", "Game of Tones")

# lib.display_books()

# member = Member("Abbas", "Khan", "kasjdf", 123, '')

# member.borrow_book(0)
# print("These are the books of the member")
# member.your_books()
# print()

# lib.display_books()


not_quit = True

while not_quit:
    
    
    
    # STRUCTURING AN INFINITE MENU FOR TRANSACTIONS
    print("----------------------------------------")
    print("   WELCOME TO LIBRARY MANAGEMENT APP")
    print("----------------------------------------")
    print()
    print("=: Choose one of the following:")
    print("1. Login")
    print("2. Signup")
    print("3. Exit")
    
    reg_choice = int(input("=> "))
    
    if reg_choice == 1:
        login_menu()
        first = input("Enter you first name\n=> ")
        last = input("Enter you last name\n=> ")
        phone = int(input("Enter you phone number\n=> "))
        password = input("Enter you password\n=> ")
        
    



