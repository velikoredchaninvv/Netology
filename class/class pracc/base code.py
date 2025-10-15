class Student:
    def __init__(self, name, course, grade):
        self.name = name
        self.course = course
        self.grade = grade
        self.finished_course = []
        self.course_in_progress = []
        self.grades = {}

    def add_grade(self, subject, grade):
        pass

    def __str__(self):
        return f'''
        self.name = {self.name}
        self.course = {self.course}
        self.grade = {self.grade}
        '''
    
student = Student('Slava', 'Python', 20)
print(student)