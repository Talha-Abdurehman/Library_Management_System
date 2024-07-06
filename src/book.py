class Book:
    
    def __init__(self, author:str, title:str):
        self.author = author
        self.title = title
        
    def get_title(self):
        return self.title
        
    def get_author(self):
        return self.author
        
    
    def display(self):
        print(f"Author: {self.author}")
        print(f"   title: {self.title}")
        print()
    
    
    