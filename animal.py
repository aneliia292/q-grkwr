class Animal:


    def __init__(self, name, species, legs):


        self.name = name
        self.species = species
        self.legs = legs


def voice(self):


    print (f"The {self.name} says something!")


def move(self):


    print (f"The {self.name} is moving!")


class Dog (Animal):


    def __init__(self, name, breed):


        super ().__init__ (name, "dog", 4)
        self.breed = breed


def bark(self):


    print (f"The {self.breed} dog {self.name} is barking!")


class Bird (Animal):


    def __init__(self, name, wingspan):


        super ().__init__ (name, "bird", 2)
        self.wingspan = wingspan


def fly(self):


    print (f"The bird {self.name} is flying!")


animal = Animal ("Animal", "unknown", 0)
animal.voice ()  # Вывод: The Animal says something!
animal.move ()  # Вывод: The Animal is moving!


dog = Dog ("Buddy", "Golden Retriever")
dog.voice()  # Вывод: The Buddy says something!
dog.move ()  # Вывод: The Buddy is moving!
dog.bark ()  # Вывод: The Golden Retriever dog Buddy is barking!


bird = Bird ("Sunny", 30)
bird.voice ()  # Вывод: The Sunny says something!
bird.move ()  # Вывод: The Sunny is moving!
bird.fly ()  # Вывод: The bird Sunny is flying!
