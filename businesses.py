
class Rescue():


    def __init__(self):
        self.inventory = []
        self.capacity = 0

    def set_capacity(self, new_cap):
        self.capacity = new_cap

    def add_dog(self, new_dog):
        if self.capacity < 20:
            self.inventory.append(new_dog)
            self.capacity += 1
    def search_dog(dog):
        