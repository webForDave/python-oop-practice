class Library:

    def __init__(self):
        pass


    @classmethod
    def calculate_fine(cls, overdue_days, fine_rate):
        cls.overdue_days = overdue_days
        cls.fine_rate = fine_rate
        return cls.overdue_days * cls.fine_rate
    

print(Library.calculate_fine(5, 2))