from library import Library 
from book import Book
from menu import login_menu

class _User:
    def __init__(self, first:str, last:str, email:str, phone:int, password:str) -> None:
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        self.password = password
    

class Librarian(_User):
    
    def addBook(self, author:str, title:str):
        somebook = Book(author, title)
        Library.add_book(somebook)

        
    def deleteBook(self, bookName:str):
        Library.delete_book(bookName)
        
        
    def display_books(self):
        Library.show_book()
        
        
    def get_book(self, author:str, title:str):
            # b refers to each book in the booklist which is an object
        Library.give_book(author,title)

    
  

class Member(_User):
    
    loaned_books = []
    
    def borrow_book(self, book_no:int):
        borrowed_book = Library.borrow(book_no)
        self.loaned_books.append(borrowed_book)
    
    def return_book(self, book_no:int):
        pass
        
        
    
        
    def your_books(self): 
        for b in self.loaned_books:
            print(f"Author: {b.author}")
            print(f"Title: {b.title}")




if __name__ == "__main__":
    pass
    
