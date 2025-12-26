# Add your class definition here (steps 1-3)
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"Woof! My name is {self.name} and I'm a {self.breed}.")
# Creating the instance of the Dog class (step 4)
my_dog = Dog("Buddy", "Golden Retriever")
# Directing the dog to bark (step 5)
my_dog.bark()