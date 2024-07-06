import sqlite3

class LRegister:
    
    @classmethod
    def signup(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/librarians.db")
        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO librarian (first_name, last_name, phone, password) VALUES ('{first}', '{last}', '{phone}', '{password}' ) )")
        
        conn.commit()
        conn.close()
        
    @classmethod
    def login(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/librarians.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM librarian WHERE first_name = '{first}' AND last_name '{last}' AND phone = '{phone}' AND password = '{password}'  )")
        data = cursor.fetchone()
        
        conn.commit()
        conn.close()