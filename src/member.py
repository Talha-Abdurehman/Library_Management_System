from users import _User
class Member(_User):
    
    loaned_books = []
    
    def borrow_book(self, book_no:int):
        borrowed_book = Library.borrow(book_no)
        self.loaned_books.append(borrowed_book)
    
    def return_book(self, book_no:int):