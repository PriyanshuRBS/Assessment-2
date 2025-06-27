from room import Room
from character import Character, Friend, Enemy
from item import Item, Weapon, Food
from banner import banner_generator, banner_generator_v2
from timespacer import time_text, time_text_spacer
import time


#creating the different rooms
home = Room('home')
home.set_description('Your home')

town_hall = Room('Town Hall')
town_hall.set_description('The administrative building, the place to report.')

road_1 = Room('Road 1')
road_1.set_description('The rough road between the village and the hut')

hut = Room('A Hut')
hut.set_description('A place to rest through the night?')

road_2 = Room('Road 2')
road_2.set_description('The paved road between the hut and the castle')

entrance = Room('The Entrance')
entrance.set_description('The grand entrance to the castle')

hallway = Room('The Hallway')
hallway.set_description('A hallway between rooms')

armory = Room('The Armory')
armory.set_description('A storage place of weapons')

kitchen = Room('The Kitchen')
kitchen.set_description('A place for food, and something more?')

great_hall = Room('The Great Hall')
great_hall.set_description('Where the king waits')

dungeon = Room('The Dungeon')
dungeon.set_description('The recipe lies here')

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
village_leader = Friend('Village Leader','The leader of the village, with a brief on yout mission')


attacker_1 = Enemy('An Attacker',"He's a wild man with a sharp knife", 20, 5)

attacker_2 = Enemy('An attacker',"He's A criminal that wants all you have", 30, 5)


old_man = Friend('An old man','An old man at the hut ready for your arrival')

guard_1 = Enemy('Guard 1','A soldier guarding the entrance and hallway', 40, 10)

soldier_strong = Enemy('The Massive Soldier', 'A strong soldier standing in the hallway',50 , 20)

soldier_1 = Enemy('Armory soldier 1','A soldier guarding the armory', 40, 10)

cook = Friend('The cook','A familiar woman in the kitchen')

king = Enemy('THE GREAT EVIL KING','The King who hides the recipe', 300, 20)

soldier_2 = ('Dungeon guard 1','A soldier guarding the dungeon')




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





#

#creating items
wooden_sword = Weapon('Wooden Sword', 'A simple blade to get the job done', 30, 10)
town_hall.set_item(wooden_sword)
iron_sword = Weapon('Iron Sword','A sharp sleek iron sword', 60, 20)
hut.set_item(iron_sword)
enchanted_sword = Weapon('Enchanted Sword', 'A heavenly blade with immense power', 100, 30)
zoogar_berry = Food('Zoogar Berry', 'A quick special food to heal up',100)
kitchen.set_item(zoogar_berry)
curry_recipe = Item('Curry Recipe', "The village's Curry recipe")
dungeon.set_item(curry_recipe)
fist = Weapon('Your fist', 'your fist', 10000000, 10)

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
time_text_spacer("THE ADVENTURE GAME",2)
time_text('Before starting,',1)
time_text_spacer('There are some important things you need to learn',2)
time_text('First of all,',1.5)
time_text('To move around roooms', 1)
time_text_spacer('You will need to enter the direction you want to go in',3)
time_text_spacer('look at the following example - ',2)

time_text_spacer("""
Welcome to:
home
Your home
Town Hall is west
> """, 4)
time_text_spacer("In this example you must enter [west] to move to the next place. look below and see how to enter", 5)
time_text_spacer("""
Welcome to:
home
Your home
Town Hall is west
>  west""", 4)

time_text("Next, to pick up items", 2)
time_text_spacer("simply enter [take] in the command line, the same place as where you put the direction. Do it as shown below", 5)
time_text_spacer("""
Welcome to:
The home is east
The Road 1 is west
Village Leader is here!
The leader of the village, with a brief on yout mission
the [Wooden Sword] is here - A simple blade to get the job done
> take""", 3)
time_text_spacer("This also applies for comannds such as [fight], [pat], [eat] and [talk]",5)
print('')
time_text_spacer("Now let's choose your skill", 3)
time_text_spacer("Do you want ", 2)
time_text_spacer("Fast healing - You have 150 HP and heal faster (healing happens as you move through rooms)",4)
time_text_spacer("Increased Strength - You have 95 HP but do more damage to the enemies",4)
time_text("Enter [Fast Healing] or [Increased Strength]",3)
skill = input(">")
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

    command = input('> ')
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
        elif current_room.move(command.lower()) == great_hall and armory not in last_rooms and kitchen not in last_rooms:
            print("Visit the other rooms first before going ")
        else:
            last_rooms.append(current_room)
            current_room = current_room.move(command.lower())
            hastalked = False
            if health < 100 and health > 100-heal_rate:
                health += health_max - health
            elif health < 100 and health < 100-heal_rate:
                health += heal_rate
            
    elif command.lower() == 'talk':
        #talking to the inhabitant, if there is one

        if inhabitant is not None:
            inhabitant.talk()
            hastalked = True
            print(hastalked)
                      
    elif command.lower() == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            if inhabitant.conversation is not None:
                if hastalked == False:
                    print(f'You must talk to {inhabitant.name} first')
            else:
                print("What will you fight with? You have:")
                #print("Debug::: len(bag)" + len(bag))
                for a in range(len(bag)):                       # show what’s in the bag
                    print(bag[a-1].name)
                    time.sleep(0.5)

                choice = input("> ").strip()
                # grab the *object* whose .name matches what the player typed
                for b in range(len(bag)):
                    if choice == bag[b-1].name:
                        print('You have that')
                        choice = bag[b-1]
                        time.sleep(0.2)
                        break
                if isinstance(choice, Weapon):
                    print('')
                else:
                    print('Seems you may not have selected a valid option, you just get your fists to fight')
                    choice = fist
                                  
        # ---------- FIGHT ----------
        # fight returns the *updated* health & dead flag
                health, dead, bag = inhabitant.fight(choice, health, dead, current_room, bag, strength)
        else:
            print("There is no one here to fight with")
            time.sleep(1)

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
