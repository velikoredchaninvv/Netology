''' Можно создать отдельный класс или словарь для хранения оценок, а затем передавать его в экземляр класса Student'''

class GradeBook:
    def __init__(self):
        self.grades = {} # {student_name : {subject: grade}}
    
    def add_grade(self, student_name, subject, grade):
        if student_name not in self.grades:
            self.grades[student_name] = {}
        self.grades[student_name][subject] = grade
    
    def get_grades(self, student_name):
        return self.grades.get(student_name, {})
    
class Student:
    def __init__(self, name, course, grade_book):
        self.name = name
        self.course = course
        self.grade_book = grade_book

    def get_grades(self):
        return self.grade_book.get_grades(self.name)
    
    def __str__(self):
        grades = self.get_grades()
        grades_str = ', '.join([f'{subject}: {grade}' for subject, grade in grades.items()])
        return f'Имя: {self.name}, Курс: {self.course}, Оценки: {grades_str}'
    
class Teacher:
    def __init__(self, name, subject, grade_book):
        self.name = name
        self.subject = subject
        self.grade_book = grade_book

    def set_grade(self, student_name, grade):
        self.grade_book.add_grade(student_name, self.subject, grade)
        print(f'Преподаватель {self.name} поставил студенту {student_name} оценку {grade} по предмету {self.subject}')
        
# Пример использования
grade_book = GradeBook()
student1 = Student('Slava', 'Python', grade_book)
teacher1 = Teacher('Ivan Petrovich', 'Python', grade_book)

teacher1.set_grade('Slava', 5)
teacher1.set_grade('Slava', 4)
teacher1.set_grade('Slava', 3)

print(student1)