class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Simon("Simon", 3), Sally("Sally", 4), Tom("Tom", 1)]

#3 Instantiate the Pet class with all your cats use variable my_pets
pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
for pet in pets.animals:
    print(pet.walk())
