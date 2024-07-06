class User():
    def __init__(self, first:str, last:str, email:str, password:str) -> None:
        self.first = first
        self.last = last
        self.email = email
        self.password = password


class Librarian(User):
    
    def display(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print(self.password)
    

if __name__ == "__main__":
    
    librarian = Librarian("Talha","Khan","tk124@gmail.com","123455")
    librarian.display()