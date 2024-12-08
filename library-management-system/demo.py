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

    def return_book(self, title):
        if title == self.title:
            self.copies = self.copies + 1
        else:
            print('book not in library')
        

book1 = Book('The wise', 'David', 5)
