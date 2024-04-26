#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют
# от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется
# (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает
# список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о
# животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь
# специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для
# `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение
# информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было
# "постоянное состояние" между запусками программы.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест.")

class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} гав")

class Cat(Animal):
    def make_sound(self):
        print(f"{self.name} мяу")

class Cow(Animal):
    def make_sound(self):
        print(f"{self.name} мууу")

animals = [Dog("Дружок", 3), Cat("Мурка", 2), Cow("Зорька", 5)]
for animal in animals:
    animal.make_sound()

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        """Звук, характерный для птиц."""
        print(f"{self.name} поет.")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        """Звук, характерный для млекопитающих."""
        print(f"{self.name} издает звук.")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        """Звук, характерный для рептилий."""
        print(f"{self.name} шипит.")

eagle = Bird("Орел", 5, 2.0)
sparrow = Bird("Воробей", 1, 0.1)
cat = Mammal("Мурка", 2, "серый")
dog = Mammal("Дружок", 3, "черный")
cow = Mammal("Зорька", 5, "рыжая")
snake = Reptile("Каа", 2, "гладкая")
turtle = Reptile("Тортилла", 12, "хордовая")

animals = [eagle, sparrow, cat, dog, snake, turtle]
for animal in animals:
    animal.eat()
    animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

zoo = Zoo()
zoo.add_animal(eagle)
zoo.add_animal(cat)
zoo.add_animal(dog)
zoo.add_animal(snake)
zoo.add_animal(turtle)

keeper = ZooKeeper("Петя")
vet = Veterinarian("Маша")

zoo.add_staff(keeper)
zoo.add_staff(vet)

keeper.feed_animal(eagle)
vet.heal_animal(snake)

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
animal_sound(zoo.animals)