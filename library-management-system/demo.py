class Book:

    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self, title):
        if title in self.title and self.copies != 0:
            self.copies = self.copies - 1
        else:
            print('Out of stock')


book1 = Book('The wise', 'David', 5)
# book2 = Book('The heart', 'Maki', 3)

book1.borrow('The wise')
print(book1.copies)

