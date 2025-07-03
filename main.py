from room import Room
from character import Character, Friend, Enemy
from item import Item, Weapon, Food
from banner import banner_generator, banner_generator_v2
from timespacer import time_text, time_text_spacer
import time
from help import help


#creating the different rooms
home = Room('home')
home.set_description('Your home')

town_hall = Room('Town Hall')
town_hall.set_description('A place in the centre of the village, lively with people')

road_1 = Room('Road 1')
road_1.set_description('The rough road between the village and the hut')

hut = Room('A Hut')
hut.set_description('A small wooden hut dimly lit by a candle')

road_2 = Room('Road 2')
road_2.set_description('The paved road between the hut and the castle')

entrance = Room('The Entrance')
entrance.set_description('The grand entrance to the castle, with diamond, gold and silver')

hallway = Room('The Hallway')
hallway.set_description('A beautiful hallway, walls made of marble and lined with diamonds and emeralds, a sight to see')

armory = Room('The Armory')
armory.set_description('A room made to store weapons, but its almost empty?')

kitchen = Room('The Kitchen')
kitchen.set_description('A kitchen with a marble table, a window with a gold frame')

great_hall = Room('The Great Hall')
great_hall.set_description('A very large hall with shiny marble, gold, flowing lava from the walls, glowing gold, shiny silver, and platinum')

dungeon = Room('The Dungeon')
dungeon.set_description('An old dusty cave, with prisons and a box half open')

old_tunnel = Room('An Old Tunnel')
old_tunnel.set_description('Some secret passage with light at the end')
# a room where dead characters are stored
storage = Room('Storage')





#linking the rooms
home.link_room(town_hall, 'west')
town_hall.link_room(home, 'east')

town_hall.link_room(road_1, 'west')
road_1.link_room(town_hall, 'east')

road_1.link_room(hut, 'west')
hut.link_room(road_1, 'east')

hut.link_room(road_2, 'west')
road_2.link_room(hut, 'east')

road_2.link_room(entrance, 'west')
entrance.link_room(road_2, 'east')

entrance.link_room(hallway, 'northwest')
hallway.link_room(entrance, 'southeast')

hallway.link_room(armory, 'south')
armory.link_room(hallway, 'north')

hallway.link_room(kitchen, 'southwest')
kitchen.link_room(hallway, 'northeast')

hallway.link_room(great_hall, "west")
great_hall.link_room(hallway, 'east')

great_hall.link_room(dungeon, 'south')
dungeon.link_room(great_hall, 'north')

dungeon.link_room(old_tunnel, 'east')
old_tunnel.link_room(dungeon, 'west')

old_tunnel.link_room(road_2, 'northeast')
road_2.link_room(old_tunnel, 'southwest')




#creating characters
village_leader = Friend('Village Leader',"He's the leader of the village, running things and giving people tasks")


attacker_1 = Enemy('An Attacker',"He's a wild man with a sharp knife, maybe some random person", 20, 5)

attacker_2 = Enemy('An attacker',"He's A criminal that wants all you have", 30, 5)


old_man = Friend('An old man','An old man at the hut ready for your arrival')

guard_1 = Enemy('Guard','A soldier guarding the entrance and hallway', 40, 10)

soldier_strong = Enemy('The Massive Soldier', 'A super soldier standing in the hallway',50 , 20)

soldier_1 = Enemy('Armory soldier',"He is a big soldier guarding the armory", 40, 10)

cook = Friend('The cook',"She's the spy the village leader talked about")

king = Enemy('THE GREAT EVIL KING','HE"S THE EVIL KING! The one who stole the recipe!', 300, 20)

soldier_2 = Enemy('Dungeon guard',"He's a super soldier like the one before",50, 20)

apparition = Enemy('Apparition', 'Some weird apparition in the tunnel that seems like it wantd to hurt you', 5, 1)




#linking the characters to rooms
town_hall.set_character(village_leader)

road_1.set_character(attacker_1)
road_2.set_character(attacker_2)

hut.set_character(old_man)

entrance.set_character(guard_1)
hallway.set_character(soldier_strong)
armory.set_character(soldier_1)
kitchen.set_character(cook)
great_hall.set_character(king)
dungeon.set_character(soldier_2)
old_tunnel.set_character(apparition)




#setting speeches for the characters
village_leader.set_conversation("""
Hello there young warrior. I have chosen you to complete a mission, a daring and difficult one,
but one I think you will succeed in, for all of our futures.

   Our village needs you to take back the Great Curry Recipe that has been rightfully ours, from The Great Evil King.
    I have a spy in the King's castle, who tells me that the recipe is stored in the dungeon.

    On the path you will follow there will be a hut, where a close friend of mine will take care of you for a night.
     Remember that on the path there are wild men and criminals. If you havent already take the wooden sword. Good luck, and be careful """,15)

old_man.set_conversation("""
Oh hello my friend! You must be the fine boy the village leader was talking about. I hope your journey so far has been safe.
If you haven't taken it already, take this better sword. That wooden sword wont help you fight the king's men
Good luck on your journey boy!""",15)

cook.set_conversation("""
Hello boy. Im the spy. If you havent already take the Enchanted Sword from the armory and eat the Zoogar Berry""", 10)
#
 
#creating items
wooden_sword = Weapon('Wooden Sword', "It's a weak little blade, but it gets the job done!", 30, 10)
town_hall.set_item(wooden_sword)
iron_sword = Weapon('Iron Sword',"A sleek shiny blade that does its job very well", 60, 20)
hut.set_item(iron_sword)
enchanted_sword = Weapon('Enchanted Sword', 'The heavenly blade, blessed by divine power, with extreme power', 100, 40)
armory.set_item(enchanted_sword)
zoogar_berry = Food('Zoogar Berry', "It's a magical berry that gives you alot of health",100)
kitchen.set_item(zoogar_berry)
curry_recipe = Item('Curry Recipe', "The Curry Recipe, a peice of paper plated with gold, with glowing words")
dungeon.set_item(curry_recipe)
fist = Weapon('Your fist', 'your fist', 10000000, 2)

#where the game runs

current_room = home
possibleDirections = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
health_max = 100
health = 100
heal_rate = 5
bag = []
dead = False
hastalked = False
eaten_food = None
food_found = False
stength = 5

time_text_spacer("Hello!",1.5)
time_text_spacer("welcome to...", 1.5)
banner_generator_v2('THE') 
time.sleep(1)        
banner_generator('CURRY')  
time.sleep(1)
banner_generator_v2('GAME')
time.sleep(2)
time_text('Before starting,',1)

help()

time_text_spacer("Now let's descide your skills", 2)
time_text('Fast healing - More health, more healing, less damage', 3)
time_text('Increased Strength - Less health, less healing, double damage', 3)

skill = input(" What's Your Command? >")
if skill.lower() == 'fast healing':
    health = 150
    health_max = 150
    heal_rate = 10
    strength = 10
elif skill.lower() == 'increased strength':
    health = 95
    health_max = 95
    heal_rate = 5
    strength = 15
else:
    time_text('You have no skill since you did not give a valid input!',4)
    health = 100
    health_max = 100
    heal_rate = 5
    strength = 5
time_text_spacer(f"You have {health}HP, {heal_rate}HP healing rate and {strength} strength", 4)
time_text("Entering the game.", 0.5)
time_text("Entering the game..", 0.5)
time_text_spacer("Entering the game...", 0.5)
time_text_spacer('You begin in your room...', 2)


while dead == False:
    print('\n')
    time_text("welcome to: ", 0.2)
    current_room.describe()
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    last_rooms = []
    time.sleep(0.1)

    if inhabitant is not None:
        inhabitant.describe()
        time.sleep(0.1)

    if item is not None:
        item.describe()
        time.sleep(0.1)

    command = input("What's your command? >")
    time.sleep(0.1)

    if command.lower() in possibleDirections:
        if inhabitant and isinstance(inhabitant, Enemy):
            print("")
            print("You cannot move until the enemy is defeated")
            time.sleep(1)
        elif  isinstance(inhabitant, Friend) and inhabitant.conversation != None and hastalked == False:
            print("")
            print(f"You must talk to {inhabitant.name} first!")
            time.sleep(1)
        elif current_room.move(command.lower()) == old_tunnel and dungeon not in last_rooms:
            print("You cannot go there")
        elif current_room.move(command.lower()) == great_hall:
            if kitchen in last_rooms and armory in last_rooms:
                great_hall_key = True
        else:
            if current_room == hallway:
                if great_hall_key == True:
                    last_rooms.append(current_room)
                    current_room = current_room.move(command.lower())
                    hastalked = False
                    if health < 100 and health > 100-heal_rate:
                        health += health_max - health
                    elif health < 100 and health < 100-heal_rate:
                        health += heal_rate
                else:
                    time_text("Go to the hallway first", 2)
            else:
                if current_room == hallway:
                    if great_hall_key == True:
                        last_rooms.append(current_room)
                        current_room = current_room.move(command.lower())
                        hastalked = False
            
    elif command.lower() == 'talk':
        #talking to the inhabitant, if there is one
        hastalked = True
        if inhabitant is not None:
            inhabitant.talk()
            
                      
    elif command.lower() == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            if inhabitant.conversation is not None:
                if hastalked == False:
                    print(f'You must talk to {inhabitant.name} first')
            else:

                                  
        # ---------- FIGHT ----------
        # fight returns the *updated* health & dead flag
                health, dead, bag = inhabitant.fight(health, dead, current_room, bag, strength, fist)
        else:
            time_text('There is no one here to fight with', 2)

    elif command.lower() == 'pat':
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.pat()
        else:
            print("There is no one here to pat :(")
    elif command.lower() == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            time.sleep(1)
            bag.append(item)
            current_room.set_item(None)


    elif command.lower() == "eat":
        for c in range(len(bag)):
            if isinstance(bag[c-1], Food):
                eaten_food = bag[c-1]
                print(f'You eat {eaten_food.name}')
                health += eaten_food.healing
                if health > 100:
                    health = 100
                elif eaten_food.name == 'Zoogar Berry':
                    health_max += 50
                    health = health_max
                food_found = True
            if food_found == True:
                break
        if food_found == False:
            print('There is no food to eat')
            
    elif command == help:
        help()
    else:
        print("""OOPS! 
              Semms you have entered an invalid command, try agian.""")
        time.sleep(0.3)

    if curry_recipe in bag:
        old_man.set_conversation("""You have found the curry recipe! Our village will be proud.
                                    You must have also found the Zoogar Berry I assume, the spy, my daughter, kept it safe for you. """)
        village_leader.set_conversation("""You Have Succeeded!
                                            The recipe i think should stay with you, since you are the one who saved it
                                                And i announce you my heir.
                                        Now go home,you have had a tiring journey.""")

    if current_room == home and dungeon in last_rooms:
        time.sleep(2)
        banner_generator_v2('The')
        banner_generator_v2('End')
        break
