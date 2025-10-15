class Student:
    # интерфейс Студент
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_course = []
        self.course_in_progress = []
        self.grades = {}

    # студенты ставят оценки лектору
    def rate_for_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.course_attached
            and course in self.course_in_progress
            and 0 <= grade <= 10
            ):

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    # средняя оценка лектору?
    @property
    def the_average_value(self):
        # the moment
        pass

    # интерфейс вывода класса студент
    def __str__(self):
        return f'''
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за домашнее задание: {self.the_average_value}
        '''

class Mentor:
    # Интерфейс Ментора
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.course_attached = []

class Lecturer(Mentor):
    # Интерфейс Лектора от Ментора
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Функция нахождения средней оценки; Функция может применяться повторно -> нужно это настроить;
    @property
    def average_grades(self):
        self.the_average_value = []
        for i in self.grades.values():
            for ii in i:
                self.the_average_value.append(ii)
        self.the_average_value = sum(self.the_average_value)/len(self.the_average_value)
        return self.the_average_value

    # Интерфейс вывода класса Лектор
    def __str__(self):
        return f"""
        Имя: {self.name}
        Фамилия: {self.surname}
        Средняя оценка за лекции: {self.average_grades}
        """

class Reviewer(Mentor):
    # Интерфеейс Проверяющего от Ментора
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_attached = []

    # Добавление оценки в список, если проходит проверку в начале
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.course_attached
            and course in student.course_in_progress
            ):

            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    ########## average №2 ##########
    @property
    def average_grades(self, student):
        self.the_average_value = []
        for i in student.grades.values():
            for sec in i:
                self.the_average_value.append(sec)
        self.the_average_value = sum(self.the_average_value)/len(self.the_average_value)
        return self.the_average_value

    # Интерфейс вывода Проверяющего с частью данных Студента
    def __str__(self):
        return f"""
        class: Reviewer
        self.name: {self.name}
        self.surname: {self.surname}
        self.course_attached: {self.course_attached}
        # student.grades -> averages_grades: {self.average_grades} # Нужно переделать логику обращения к параметру student из метода
        student.course_in_progress: {student.course_in_progress}
        student.finished_course: {student.finished_course}
        """

# Создание экземляраа Лектора с добавлением курса
lecturer = Lecturer('Ivan', 'Petrov')
lecturer.course_attached += ['Python']

# Создание экземляра Студента, с добавлением курсов и оценок за один курс; Добавление пройденного курса
student = Student('Roy', 'Toy', 'male')
student.course_in_progress += ['Python', 'Git']
student.rate_for_lecturer(lecturer, 'Python', 9.231)
student.rate_for_lecturer(lecturer, 'Python', 7.123)
student.rate_for_lecturer(lecturer, 'Python', 5.4)
student.rate_for_lecturer(lecturer, 'Python', 8.1)
student.finished_course+=['HTML']

# Создание экземляра Проверяющего с добавлением курса. Добавление оценок для Студента за курс
reviewer = Reviewer('Fedor', 'Pykin')
reviewer.course_attached += ['Python']
reviewer.rate_hw(student, 'Python', 10.44)
reviewer.rate_hw(student, 'Python', 9.123)
reviewer.rate_hw(student, 'Python', 6.32)
reviewer.rate_hw(student, 'Python', 3.22)

# Проверка от Netology №1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.course_attached)    # []
# print(reviewer.course_attached)    # []

# Запуск Классов
print(reviewer)
# print(reviewer.average_grades(student)) # Не забывай при обращении к функции или методоу ставить ()

# print(lecturer)
# print(lecturer.average_grades)

# print(student)