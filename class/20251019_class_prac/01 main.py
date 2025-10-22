# Упражнение 1: Решение
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.course_in_progress = []

    def add_course(self):
        if self.add_course:
            self.course_in_progress.append(self.course)
        return self.course_in_progress
    
    def __str__(self):
        return f'Студент: {self.name}, Курс: {self.course_in_progress}'
    
student1 = Student('Slava', 'Python')
student2 = Student('Aigul', 'C++')

student1.add_course()
student2.add_course()

print(student1)
print(student2)

# Упражнение 2: Решение
class Example:
    items = []

    def __init__(self):
        self.items = []

#запуск программы
example1 = Example()
example2 = Example()

# Вывод атрибута класса, относящихся ко всем объектам, если он не перезаписан
print(f'Атрибут класса: {Example.items}')

# Вывод атрибута объектов, для каждого уникальный, если перезаписан
print(f'Атрибут объекта 1: {example1.items}')
print(f'Атрибут объекта 2: {example2.items}')

# Доступ к атрибуду класса через объект
print(f'Доступ к атрибуту класса через объект 1: {example1.items}') # Но тут сложно понять, к чему сейчас получаю доступ, так как атрибут один, и ссылаться на какой будет пока не пойму, пока не попробую сослаться
print(f'Доступ к атрибуту класса через объект 2: {example2.items}') # Но тут сложно понять, к чему сейчас получаю доступ, так как атрибут один, и ссылаться на какой будет пока не пойму, пока не попробую сослаться

# Добавление информации в атрибут объекта
for i in range(5):
    example1.items.append(i)
print(example1.items)

# Проверю что атрибут класса не поменялся
print(Example.items) # Да, атрубит класса не поменялся, а вот если поменяю его, то изминение каснётся всех произведённых от него объектов

for i in range(6,11):
    Example.items.append(i)
print(Example.items)

# В общем всё проверил, работает как и ожидалось

# Упражнение 3: Ответ
'''
Важно проверять тип объекта внутри метода потому что он может не соответсоввать тому типу данных который может исполнить метод. Так же важно проверять принадлежность к конкретному классу, потому что метод, в который подаются данные может быть выполнен, но если данные не соответствуют по содержанию, то метод отработает не корректно.
'''


# Хороший пример правильной проверки через isinsance
# if isinstance(lecturer, Lecturer) and course in lecturer.course_attached:
    # безопасно работать с lecturer