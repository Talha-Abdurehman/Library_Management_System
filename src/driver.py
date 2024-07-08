from users import Librarian, Member
from menu import l_login_menu, l_signup_menu, m_login_menu, m_signup_menu




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
    print("1. Librarian")
    print("2. Member")
    print("3. Exit")
    
    first_choice = int(input("=> "))
    
    if first_choice == 1:
        print("----------------------------------------")
        print("                 HELLO                  ")
        print("----------------------------------------")
        print()
        print("=: Choose one of the following:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        
        l_choice = int(input("=> "))
        
        if l_choice == 1:
            l_login_menu()
        
        elif l_choice == 2:
            l_signup_menu()
        
        else:
            exit()
        
        
    if first_choice == 2:
        print("----------------------------------------")
        print("                 HELLO                  ")
        print("----------------------------------------")
        print()
        print("=: Choose one of the following:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        
        m_choice = int(input("=> "))
            
        if m_choice == 1:
            m_login_menu()
        
        elif m_choice == 2:
            m_signup_menu()
        
        else:
            exit()
        
            
        
        
        
        
    



