class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]

    def __init__(self,name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type:{pet_type}. Must be on of {Pet.PET_TYPES}")
        # pass
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
    

        Pet.all.append(self)
    # pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        # pass
    
    def add_pet(self, pet):
        if not isinstance(pet,Pet):
            raise TypeError("Only pet instances can be added")
        pet.owner=self

    def get_sorted_pets(self):
        """Return this owner's pets sorted by their name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
    # pass