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

    def fight(self, combat_item, player_health: int, dead_flag: bool):

        while self.health > 0 and player_health > 0:
            # ---------- PLAYER TURN ----------
            if combat_item: # if the player has a weapon
                print(' ')
                choice = input("Strong or weak? ").strip().lower()

                if choice.lower() == "strong":
                    combat_item.durability -= 15
                    dmg = combat_item.damage
                elif choice.lower() == "weak":
                    combat_item.durability -= 5
                    dmg = combat_item.damage // 2   # integer division → whole dmg so we dont need to deal with decimals
                else:
                    print("You hesitate!")
                    dmg = 0

                self.health = max(0, self.health - dmg)
                print(f"You did {dmg} damage. {self.name} now has "
                      f"{self.health} HP.")

            # Enemy defeated?
            if self.health == 0:
                print(f"{self.name} is dead – you win!")
                return player_health, dead_flag

            # ---------- ENEMY TURN ----------
            print(f"{self.name} hits you! -{self.hit_damage} HP")
            player_health = max(0, player_health - self.hit_damage)

            if player_health == 0:
                print(f"You lost the fight to {self.name}.")
                dead_flag = True
                return player_health, dead_flag

        # Shouldn’t get here, but just in case:
        return player_health, dead_flag
            

            
        

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def pat(self):
        print(self.name + " pats you back!")
    # What other methods could your Friend class have?
    


