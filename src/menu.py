from os import system
from db_functions.login import LRegister



def l_signup_menu():
    system('cls')
    print("----------------------------------------")
    print("                  SIGNUP                ")
    print("----------------------------------------")
    print()
    print("=: Enter your details:")
    first = input("Enter you first name\n=> ")
    last = input("Enter you last name\n=> ").capitalize().strip()
    phone = int(input("Enter you phone number\n=> "))
    password = input("Enter you password\n=> ").strip()
    LRegister.signup(first, last, phone, password)
    print("You have signed up successfully!")
    print("Now login to your account")

    

def l_login_menu():
    system('cls')
    print("----------------------------------------")
    print("                  LOGIN                 ")
    print("----------------------------------------")
    print()
    print("=: Enter your details:")
    first = input("Enter you first name\n=> ")
    password = input("Enter you password\n=> ").strip()
    LRegister.login(first, password)
    print("Logged In successfully")



def m_signup_menu():
    system('cls')
    print("----------------------------------------")
    print("                  SIGNUP                ")
    print("----------------------------------------")
    print()
    print("=: Enter your details:")
    first = input("Enter you first name\n=> ")
    last = input("Enter you last name\n=> ").capitalize().strip()
    phone = int(input("Enter you phone number\n=> "))
    password = input("Enter you password\n=> ").strip()
    LRegister.signup(first, last, phone, password)
    print("You have signed up successfully!")
    print("Now login to your account")

    

def m_login_menu():
    system('cls')
    print("----------------------------------------")
    print("                  LOGIN                 ")
    print("----------------------------------------")
    print()
    print("=: Enter your details:")
    first = input("Enter you first name\n=> ")
    last = input("Enter you last name\n=> ").strip()
    phone = int(input("Enter you phone number\n=> "))
    password = input("Enter you password\n=> ").strip()
    LRegister.login(first, last, phone, password)
    print("Logged In successfully")


if __name__ == "__main__":
    pass 