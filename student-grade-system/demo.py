class Student():

    number_of_students = 0

    def __init__(self, name, GPA):
        self.name = name
        self.GPA = GPA
        Student.number_of_students += 1


    def update_GPA(self, new_GPA):
        self.GPA = new_GPA



student1 = Student('Dave', 4.6)
student2 = Student('Ken', 4.0)
student3 = Student('Ron', 3.5)
student4 = Student('Jen', 3.3)

student2.update_GPA(5.0)

sum_of_GPA = student1.GPA + student2.GPA + student3.GPA + student4.GPA

print(sum_of_GPA / Student.number_of_students)