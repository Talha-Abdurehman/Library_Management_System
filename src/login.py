import sqlite3

class LRegister:
    
    @classmethod
    def signup(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/librarians.db")
        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO librarian (first_name, last_name, phone, password) VALUES ('{first}', '{last}', '{phone}', '{password}' )")
        
        conn.commit()
        conn.close()
        
    @classmethod
    def login(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/librarians.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM librarian WHERE first_name = '{first}' AND last_name = '{last}' AND phone = '{phone}' AND password = '{password}' ")
        data = cursor.fetchone()
        
        if first in data \
            and last in data \
                and phone in data\
                    and password in data:
                        print("Your credentials Match! You can successfully Login")
        else:
            print("Account Not found!")
        
        conn.commit()
        conn.close()
        
         