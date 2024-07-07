import sqlite3

class BookOps:
    
    @classmethod
    def add_book(cls,author:str, title:str, price:float):
        conn = sqlite3.connect("db/books.db")
        cursor = conn.cursor()
        
        insert_query = '''INSERT INTO book_info (author, title, price) VALUES (?,?,?)'''
        insert_info = (author, title, price)
        cursor.execute(insert_query, insert_info)
        conn.commit()
    
    @classmethod
    def remove_book(cls,author:str, title:str):
        conn = sqlite3.connect("db/books.db")
        cursor = conn.cursor()
        
        insert_query = '''DELETE FROM book_info WHERE author=? AND title=?'''
        insert_info = (author, title)
        cursor.execute(insert_query, insert_info)
        conn.commit()

        
    @classmethod
    def login(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/librarians.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM librarian WHERE first_name = '{first}' AND last_name = '{last}' AND phone = '{phone}' AND password = '{password}' ")
        data = cursor.fetchall()
        
        conn.commit()
        
        for d in data:
            if first == d[1] \
                and last == d[2] \
                    and phone == d[3]\
                        and password == d[4]:
                            print("Your credentials Match! You can successfully Login")
            else:
                print("Account Not found!")
 
 
 
    @classmethod
    def mem_signup(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/members.db")
        cursor = conn.cursor()
        
        cursor.execute(f"INSERT INTO member (first_name, last_name, phone, password) VALUES ('{first}', '{last}', '{phone}', '{password}' )")
        
        conn.commit()

            
    @classmethod
    def mem_login(cls,first:str, last:str, phone:int, password:str):
        conn = sqlite3.connect("db/members.db")
        cursor = conn.cursor()
        
        cursor.execute(f"SELECT * FROM member WHERE first_name = '{first}' AND last_name = '{last}' AND phone = '{phone}' AND password = '{password}' ")
        data = cursor.fetchall()
        
        conn.commit()
        
        for d in data:
            if first == d[1] \
                and last == d[2] \
                    and phone == d[3]\
                        and password == d[4]:
                            print("Your credentials Match! You can successfully Login")
            else:
                print("Account Not found!")




if __name__ == "__main__":
    
    
        
      BookOps.remove_book("R.R Martin", "Game of Thrones")   