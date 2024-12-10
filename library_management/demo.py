class Library:
    items_count =0

    def __init__(self, title: str, author: str, publication_year: int):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        Library.items_count += 1


    @classmethod
    def increment_item_count(cls):
        return Library.items_count
    

class Book(Library):
    book_discount = 10

    def __init__(self, title, author, publication_year, pages: int):
        super().__init__(title, author, publication_year)
        self.pages = pages


    @classmethod
    def set_discount_percentage(cls, discount):
        cls.book_discount += discount
        return cls.book_discount
    

class Magazine(Library):
    magazine_discount = 5

    def __init__(self, title, author, publication_year, issue: str):
        super().__init__(title, author, publication_year)
        self.issue = issue

    @classmethod
    def set_discount_percentage(cls, discount):
        cls.magazine_discount += discount
        return cls.magazine_discount


class DVD(Library):
    DVD_discount = 30

    def __init__(self, title, author, publication_year, duration: int):
        super().__init__(title, author, publication_year)
        self.duration = duration


    @classmethod
    def set_discount_percentage(cls, discount):
        cls.DVD_discount += discount
        return cls.DVD_discount

book1 = Book('Effective People', 'David', 2024, 250)
magazine1 = Magazine('Forbes', 'Elon', 2023, 'Feburary')
dvd1 = DVD('Appreciation', 'KSA', 2000, 30)

print(Library.increment_item_count())

Book.set_discount_percentage(20)
Magazine.set_discount_percentage(10)
DVD.set_discount_percentage(5)

print(Book.book_discount)
print(Magazine.magazine_discount)
print(DVD.DVD_discount)
