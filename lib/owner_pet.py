class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.owner = owner
        Pet.add_to_all(self)
        if (Pet.is_pet(pet_type)):
            self.pet_type = pet_type
        else:
            raise Exception

    @classmethod
    def is_pet(cls, pet_type):
        if (pet_type in cls.PET_TYPES):
            return True
        else:
            return False 

    @classmethod
    def add_to_all(cls, pet):
        cls.all.append(pet)

class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if (isinstance(pet, Pet)):
            pet.owner = self
        else:
            raise Exception

    def get_sorted_pets(self):
        pets = self.pets()
        return sorted(pets, key=lambda pet: pet.name)