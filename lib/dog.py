class Dog:
    approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

    def __init__(self, name: str = "", breed: str = ""):
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, value):
        if value in self.approved_breeds:
            self._breed = value
        else:
            print("Breed must be in the list of approved breeds.")

# Example usage:
dog1 = Dog("Buddy", "Beagle")
print(dog1.name)   # Buddy
print(dog1.breed)  # Beagle

dog2 = Dog("Max", "Labrador")  # Breed must be in the list of approved breeds.
