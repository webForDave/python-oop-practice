class LibraryItem:

    def __init__(self, title: str, author: str, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year


    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}"
    
    
class Book(LibraryItem):

    def __init__(self, title, author, publication_year, pages: int):
        super().__init__(title, author, publication_year)
        self.pages = pages

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Pages: {self.pages}"
    

class Magazine(LibraryItem):

    def __init__(self, title, author, publication_year, issue: str):
        super().__init__(title, author, publication_year)
        self.issue = issue


    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Issue: {self.issue}"
    

class DVD(LibraryItem):

    def __init__(self, title, author, publication_year, duration: int, rating: str):
        super().__init__(title, author, publication_year)
        self.duration = duration
        self.rating = rating

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Duration: {self.duration} mins, Rating: {self.rating}"
    

book1 = Book('Effective People', 'David', 2024, 250)
magazine1 = Magazine('Forbes', 'Elon Musk', 2010, 'The Future Of Tech')
dvd1 = DVD('Appreciation', 'KSA', 2004, 3, 'PG')

print(book1.get_details())
print(magazine1.get_details())
print(dvd1.get_details())
