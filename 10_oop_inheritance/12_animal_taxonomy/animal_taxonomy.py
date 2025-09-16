class Animal():
    def __init__(self , name , species):
        self.name = name
        self.species = species
    def eat():
        a = "Eating"
    def sleep():
        a = "Sleep"
    def move():
        a = "Move somewhere"
    def make_sound():
        a = "making soung"
    
class Dog(Animal):
    def __init__(self, name, species , breed):
        super().__init__(name, species)
        self.breed = breed
    def make_sound(self):
        return "Woof! Woof!"
    def move(self):
        return "Running on four legs"
    def bark(self):
        return self.name , " is barking loudly!"
    def fetch(self):
        return self.name , " is fetching the ball!"

class Cat(Animal):
    def __init__(self, name, species , coat_color):
        super().__init__(name, species)
        self.coat_color = coat_color
    def make_sound(self):
        return "Meow! Meow!"
    def move(self):
        return "Stalking silently"
    def purr(self):
        return self.name , " is purring contentedly"
    def climb(self):
        return self.name , " is climbing up the tree"

class Bird(Animal):
    def __init__(self, name, species , wingspan : float):
        super().__init__(name, species)
        self.wingspan = wingspan
    def make_sound(self):
        return "Tweet! Tweet!"
    def move(self):
        return "Flying with wings"
    def fly(self):
        return self.name , "  is flying gracefully"
    def sing(self):
        return self.name , " is singing a beautiful song"

# Create different animals
dog = Dog("Buddy", "Golden Retriever", "Golden Retriever")
cat = Cat("Whiskers", "Domestic Cat", "Orange")
bird = Bird("Tweety", "Canary", 0.15)

# Display basic information
print(f"Dog: {dog.name} ({dog.species})")
print(f"Breed: {dog.breed}")
print(f"Sound: {dog.make_sound()}")
print(f"Movement: {dog.move()}")
dog.bark()
dog.fetch()

print(f"\nCat: {cat.name} ({cat.species})")
print(f"Color: {cat.coat_color}")
print(f"Sound: {cat.make_sound()}")
print(f"Movement: {cat.move()}")
cat.purr()
cat.climb()

print(f"\nBird: {bird.name} ({bird.species})")
print(f"Wingspan: {bird.wingspan}m")
print(f"Sound: {bird.make_sound()}")
print(f"Movement: {bird.move()}")
bird.fly()
bird.sing()

# Demonstrate polymorphism
animals = [dog, cat, bird]
print("\nAll animals making sounds:")
for animal in animals:
    print(f"{animal.name}: {animal.make_sound()}")

print("\nAll animals moving:")
for animal in animals:
    print(f"{animal.name}: {animal.move()}")