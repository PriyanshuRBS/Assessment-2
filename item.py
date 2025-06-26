class Item():
    
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description

    def describe(self):
        print(f"the ["+self.name+"] is here - "+self.description)

class Weapon(Item):

    def __init__(self, name, description, durability, damage):
        super().__init__(name, description)
        self.durability = durability
        self.damage = damage

    def durability_check(self):
        if self.durability >= 0:
            return True
        else:
            return False
        
class Food(Item):

    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing

        
