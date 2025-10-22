class MyClass:
    class_attribute = "Жто атрибут класса"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute

# Доступ к атрибуту класса через класс
print(MyClass.class_attribute) # это атрибут класса

# Создаём экземляр класса
instance1 = MyClass("Это атрибут экземляра 1")
instance2 = MyClass("Это атрибут экземляра 2")

# Доступ к атрибуту класса через экземляр (если экземляр его не переопределил)
print(instance1.class_attribute) # Вывод: Это атрибут класса
print(instance2.class_attribute) # Вывод: Это атрибут класса

# Доступ к атрибутам экземляра
print(instance1.instance_attribute) # Вывод: Это атрибут экземляра 1
print(instance2.instance_attribute) # Вывод: Это атрибут экземляра 2

# Изменяем атрибут класса через класс
MyClass.class_attribute = 'Изменённый атрибут класса'

# Видим изменение во всех экземлярах (которые его не переопределили)
print(instance1.class_attribute) # Вывод: Изменённый атрибут класса
print(instance2.class_attribute) # Вывод: Изменённый атрибут класса

# Переопределяем атрибут класса для одного экземляра
instance1.class_attribute = 'Атрибут класса: переопределённый для instance1'

# Теперь onstance1 имеет свой собственный атрибут с тем же именем
print(instance1.class_attribute) # Вывод: Атрибут класса: переопределённый для instance1
print(instance2.class_attribute) # Вывод: Изменённый атрибут класса (Не изменился)
print(MyClass.class_attribute) # Вывод: Изменённый атрибут класса (значение атрибута класса осталось прежним)