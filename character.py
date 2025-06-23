class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        
        
    # Describe this character
    
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        
        
    # Set what this character will say when talked to
    
    def set_conversation(self, conversation):
        self.conversation = conversation
        
        
    # Talk to this character
    
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    
                    
    # Fight with this character
    
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description, health, hit_damage):
        super().__init__(char_name, char_description)
        self.weakness = None 
        self.enemies_to_defeat = Enemy.enemies_to_defeat + 1
        self.health = health
        self.hit_damage = hit_damage


    def steal(self):
        print('You steal from'+self.name)

    def fight(self, combat_item, player_health, dead_or_not):
        while self.health > 0 or player_health > 0:
            if combat_item is not None:
                choice = input("Strong or weak?")
                if choice.lower == 'strong':
                    combat_item.durability -= 15
                    self.health -= combat_item.damage
                    print(f"You did {combat_item.damage} damage!")
                    print(f"{self.name} fights back!")
                elif choice.lower == 'weak':
                    combat_item.durability -= 5
                    self.health -= combat_item.damage / 2
                    print(f"You did {combat_item.damage/2} damage!")
                    print(f"{self.name} fights back!")
            print(f"{self.name} hits you! -{self.hit_damage} health")
            player_health -= self.hit_damage
        if self.health <= 0:
            print(f"{self.name} is dead, you win!")
        elif player_health <= 0:
            print(f"Scurry home, you lost the fight to {self.name}")
            dead_or_not = True
            

            
        

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")
    # What other methods could your Friend class have?
    


