class Library:
    # CREATED A SET BOOKSLIBARARY which will store all the books
    book_list = []
    
    @classmethod
    def add_book(cls, book:object):
        cls.book_list.append(book)
    
    @classmethod
    def show_book(cls):
        index = 1
        
        for book in cls.book_list:
            print(index, end= ". ")
            book.display()
            index += 1
    
    @classmethod
    def give_book(cls, author:str, title:str):
        
        for b in Library.book_list:
            if author == b.get_author() and title == b.get_title():
                b.display()
                break
            else:
                print("Not Found")

    @classmethod
    def delete_book(cls, book):
        cls.book_list.remove(book)
    
    @classmethod
    def borrow(cls, book_no:int):
        
        to_borrow = cls.book_list[book_no]
        cls.book_list.pop(book_no)
        
        return to_borrow
    

    






