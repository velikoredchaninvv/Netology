'''This method assumes that the Teacher class has a method for adding grade to a student'''

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = {} # Dictionary for save grades for defference discipline

    def add_grade(self, subject, grade):
        """Adding grade for a subject"""
        self.grades[subject] = grade
    
    def __str__(self):
        grades_str = ', '.join([f'{subject} : {grade}' for subject, grade in self.grades.items()])
        return f'Имя -> {self.name}, Курс -> {self.course}, Оценки -> {grades_str}'
    
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def set_grade(self, student, grade):
        '''Grading a student'''
        student.add_grade(self.subject, grade)
        return(f'Преподаватель {self.name} поставил студенту {student.name} оценку {grade} по предмету {self.subject}')

# Пример использования
student1 = Student('Slava', 'Python')
teacher1 = Teacher('Ivan Petrovich', 'ООП: Инкапсуляция')

teacher1.set_grade(student1, 5)
teacher1.set_grade(student1, 4)

print(student1)
# print(teacher1)