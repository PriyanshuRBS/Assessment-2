from room import Room
from character import Character, Friend, Enemy
from item import Item, Weapon, Food
from banner import banner_generator, banner_generator_v2
from timespacer import time_text, time_text_spacer
import time
from help import help


#creating the different rooms
home = Room('home')
home.set_description("Your home with a big sign that says Jarad's home")

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


#creating items
sandwich = Food('Sandwich', 'a snack from your mother to take with you on your trip',30)

wooden_sword = Weapon('Wooden Sword', "It's a weak little blade, but it gets the job done!", 30, 10)

iron_sword = Weapon('Iron Sword',"A sleek shiny blade that does its job very well", 60, 20)

enchanted_sword = Weapon('Enchanted Sword', 'The heavenly blade, blessed by divine power, with extreme power', 100, 40)

zoogar_berry = Food('Zoogar Berry', "It's a magical berry that gives you alot of health",100)

curry_recipe = Item('Curry Recipe', "The Curry Recipe, a peice of paper plated with gold, with glowing words")

fist = Weapon('Your fist', 'your fist', 10000000, 2)


#creating characters
mother = Friend('Mother', "Your mother, you should talk to her")

village_leader = Friend('Village Leader',"He's the leader of the village, running things and giving people tasks. You should talk to him")

attacker_1 = Enemy('Attacker',"He's a wild man with a sharp knife, maybe some random person", 20, 5)

attacker_2 = Enemy('Attacker',"He's A criminal that wants all you have", 30, 5)

old_man = Friend('An old man','An old man at the hut ready for your arrival')

guard_1 = Enemy('Guard','A soldier guarding the entrance and hallway', 40, 10)

soldier_strong = Enemy('The Massive Soldier', 'A Massive Soldier with big muscles standing in the hallway',50 , 20)

soldier_1 = Enemy('Armory soldier',"He is a big soldier guarding the armory", 40, 10)

cook = Friend('The cook',"She's the spy the village leader talked about")

king = Enemy('THE GREAT EVIL KING','HE"S THE EVIL KING! The one who stole the recipe!', 300, 30)

soldier_2 = Enemy('Dungeon guard',"He's a super soldier like the one before",50, 20)

apparition = Enemy('Apparition', 'Some weird apparition in the tunnel that seems like it wantd to hurt you', 5, 1)


#setting speeches for the characters
mother.set_conversation("""
Hey son! today is your big day! head to the town hall as fast you can!, and take this sandwich with you!""")

village_leader.set_conversation("""
Hello Jarad. Ive known you since you were born and i know that this mission is perfect for you. I have chosen you to complete a mission, a daring and difficult one,
but one I think you will succeed in, for all of our futures.

   Our village needs you to take back the Great Curry Recipe that has been rightfully ours, from The Great Evil King.
    I have a spy in the King's castle, who tells me that the recipe is stored in the dungeon.

    On the path you will follow there will be a hut, where a close friend of mine will take care of you for a night.
     Remember that on the path there are wild men and criminals. If you havent already take the wooden sword. Good luck, and be careful """)

old_man.set_conversation("""
Oh hello Jarad! Ive been waiting for you! I heard theres 2 attackers on the loose! they lurk these roads, but dont come near houses, so its safe here.
    I have this Iron Sword for you. because that Wooden Sword wont get you too far, not far enough to survive that castle, your unc-Enemy's castle. 
        Now get going, you haven't much time.""")

cook.set_conversation("""
Hello Jarad. Im the spy you were informed about. In the Great Hall is the King, and in the dungeon is the recipe. 
    If you havent already take the Enchanted Sword from the armory, take it, 
        And if you havent already eaten the Zoogar Berry, eat it. It will give you enough health to survive the battle.""")
king.set_conversation("""
I've met many boys who have tried to take back the recipe, and none have made it out alive. You will be no different Jarad.
    you wonder how i know your name? Well, Jarad, to put it simply, I was your uncle. It will be sad to kill you, but you, like the other boys, come in the way of my wealth.
        You can't defeat me, so just give up and let's make this quick""" )


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

hallway.link_room(great_hall, 'west')
great_hall.link_room(hallway, 'east')

great_hall.link_room(dungeon, 'south')
dungeon.link_room(great_hall, 'north')

dungeon.link_room(old_tunnel, 'east')
old_tunnel.link_room(dungeon, 'west')

old_tunnel.link_room(road_2, 'northeast')
road_2.link_room(old_tunnel, 'southwest')


#linking the characters to rooms
home.set_character(mother)

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


#linking the items to rooms
home.set_item(sandwich)

town_hall.set_item(wooden_sword)

hut.set_item(iron_sword)

armory.set_item(enchanted_sword)

kitchen.set_item(zoogar_berry)

dungeon.set_item(curry_recipe)


#where the game runs
health = 0
health_max = 0
time_text_spacer("Hello!",1.5)
time_text_spacer("welcome to...", 1.5)
banner_generator_v2('Stealth & Spice') 
time.sleep(1.5)
time_text_spacer("         An Adventure For Heritage",2)
time_text_spacer(' ', 0.5)
time.sleep(2)
instructions_question = input("Would you like to go through how to play the game? (type [y] for yes and [n] for no) > ")
if instructions_question == 'y':
    help()
elif instructions_question =='n':
    time_text_spacer('Alright, but remember you can eneter [help] in the command line to see the instructions', 2)
else:
    time_text_spacer('Sounds close enough to yes', 1)
    help()

time_text_spacer("Now let's descide your skills", 2)
time_text('[1] -> Fast healing - More health, more healing, less damage', 2)
time_text('[2] -> Increased Strength - Less health, less healing, double damage', 1)

#asking for skill
skill = input(" What's Your Command? > ")
if skill.lower() == '1':
    health = 150
    health_max = 150
    heal_rate = 10
    strength = 10
    
elif skill.lower() == '2':
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
time_text_spacer(f"You have {health}HP, {heal_rate}HP healing rate and {strength} strength", 2)
time_text_spacer('Your name is Jarad', 1)
time_text("Entering the game...", 1.5)

time_text_spacer('You begin in your room...', 2)


#the loop where the game runs
current_room = home
possible_directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
heal_rate = 5
bag = []
dead = False
hastalked = False
eaten_food = None
food_found = False
stength = 5
kitchen_key = False
armory_key = False
completion_key = False
last_rooms = []

while dead == False:
    if completion_key == True and current_room == dungeon:
        print("""
[Game says]:
    Go through the old tunnel and then go east until you reach home, the castle is collapsing""")
    elif completion_key == True and current_room == home:
                print("""
[Game says]:
    talk to your mother to finish the game""")



    print('\n')
    time_text("WELCOME TO: ", 0.2)
    current_room.describe()
    time.sleep(0.1)
    current_room.get_details()
    time.sleep(0.1)
    inhabitant = current_room.get_character()
    time.sleep(0.1)
    item = current_room.get_item()
    time.sleep(0.1)

    if inhabitant is not None:
        inhabitant.describe()
        time.sleep(0.1)
    
    if isinstance(inhabitant, Enemy):
        print(f'Enter [fight] to fight with {inhabitant.name}')

    if item is not None:
        item.describe()
        time.sleep(0.1)

    command = input("What's your command? > ")
    time_text('   ', 0.1)

    if command.lower() in possible_directions:
        next_room = current_room.move(command.lower())

        if inhabitant and isinstance(inhabitant, Enemy):
            print("")
            print("You cannot move until the enemy is defeated")
            time.sleep(1)
        elif isinstance(inhabitant, Friend) and inhabitant.conversation is not None and hastalked == False:
            time_text(f'You must talk to {inhabitant.name} first!', 1)
        elif next_room == old_tunnel and current_room != dungeon:
            time_text('You cannot go there yet, that place is for later',1)
        elif current_room == dungeon and next_room == great_hall:
            time_text('You cannot go back, the castle is collapsing',1)
        elif next_room == great_hall:
            if kitchen_key == False or armory_key == False:
                time_text('Visit the Kitchen and armory first before entering the great hall',1)
            else:
                last_rooms.append(current_room)
                current_room = next_room
                # Give keys after moving
                if current_room == kitchen:
                    kitchen_key = True
                if current_room == armory:
                    armory_key = True

                hastalked = False
                if health < health_max and health > health_max - heal_rate:
                    health = health_max
                elif health < health_max and health < health_max - heal_rate:
                    health += heal_rate
        else:
            last_rooms.append(current_room)
            current_room = next_room
            # Give keys after moving
            if current_room == kitchen:
                kitchen_key = True
            if current_room == armory:
                armory_key = True

            hastalked = False
            if health < health_max and health > health_max - heal_rate:
                health = health_max
            elif health < health_max and health < health_max - heal_rate:
                health += heal_rate



    elif command.lower() == 'talk':
        hastalked = True
        # Talking to the inhabitant, if there is one
        if inhabitant is not None:
            inhabitant.talk()


    elif command.lower() == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):
            if inhabitant.conversation is not None and not hastalked:
                print(f'You must talk to {inhabitant.name} first')
            else:
                # Fight returns the updated health & dead flag
                health, dead, bag = inhabitant.fight(health, dead, current_room, bag, strength, fist)
        else:
            time_text('There is no one here to fight with', 2)

    elif command.lower() == 'take':
        if item is not None:
            bag.append(item)
            print(f'You put {item.name} in your bag')
            current_room.item = None
            if item == curry_recipe:
                completion_key = True
                old_man.set_conversation("""
You have found the curry recipe! Our village will be proud.
    It must have been a difficult battle, fighting your uncle, 
        but i assume you ate the Zoogar Berry before battle, and gained the health to survive the strength of your uncle """)
                village_leader.set_conversation("""
You Have Succeeded Jarad! Your name will be celebrated for centuries in our village.
    Keep the recipe with yourself, for you are worthy of keeping it,
        And lastly, I announce you my heir.
            Now go home, you have had a tiring journey.""")
                mother.set_conversation("""Rest my boy, it is done""")

        else:
            print('There is no item to take')
        
    elif command.lower() == 'health':
        print(f"You currently have {health}HP")

    elif command.lower() == "eat":
        print('You have:')
        food_items = []
        for item in bag:
            if isinstance(item, Food):
                print(item.name)
                food_items.append(item)

        food_choice_name = input('Which food would you like to eat? ')

        # Try to find a matching food
        food_choice = None
        for item in food_items:
            if item.name.lower() == food_choice_name.lower():
                food_choice = item
                break

        if food_choice is None:
            time_text_spacer('That is not a food.', 1)

        elif food_choice == zoogar_berry:
            time_text_spacer('You eat the Zoogar Berry.', 1)
            if health_max < 100:
                health_max += zoogar_berry.healing
                time_text_spacer(f'You have {health_max} HP', 1)
            else:
                health_max = 195
            health = health_max
            bag.remove(food_choice)

        else:
            time_text_spacer(f'You eat the {food_choice.name}.', 1)
            if health < (health_max - food_choice.healing):
                health += food_choice.healing
            else:
                health = health_max
            bag.remove(food_choice)


            
    elif command.lower() == 'help':
        help()

    elif command.lower() == 'inventory':
        print("In your bag you have: ")
        for e in range(len(bag)):
            if isinstance(bag[e-1], Weapon):
                print(f"{bag[e-1].name} - {bag[e-1].durability} durability")
            else:
                print(bag[e-1].name)
        print('')
    else:
        print("""OOPS! 
              Semms you have entered an invalid command, try agian.""")
        time.sleep(0.3)

    if current_room == home and completion_key == True and hastalked == True:
        banner_generator_v2('The')
        banner_generator_v2('End')
        break