from room import Room
from character import Character, Friend, Enemy
from item import Item




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
village_leader = Friend('Village Leader','The leader, who awaits your arrival')


attacker_1 = Enemy('An Attacker','A wild man with a knife')

attacker_2 = Enemy('An attacker','A criminal that wants all you have')


old_man = Friend('An old man','An old man at the hut ready for your arrival')


guard_1 = Enemy('Guard 1','A soldier guarding the entrance and hallway')

soldier_strong = Enemy('The Massive Soldier', 'A strong soldier standing in the hallway')

soldier_1 = Enemy('Armory soldier 1','A soldier guarding the armory')

cook = Friend('The cook','A familiar woman in the kitchen')

king = Enemy('THE GREAT EVIL KING','The King who hides the recipe')

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
Hello there young warrior. I have chosen you to complete a mission, a daring a difficult one,
but one I think you will succeed in, for all of our futures.

   Our village needs you to take back the Great Curry Recipe that has been rightfully ours, from The Great Evil King.
    I have a spy in the King's castle, who tells me that the recipe is stored in the dungeon.

    On the path you will follow there will be a hut, where a close friend of mine will take care of you for a night.
     Remember that on the path there are wild men and criminals. If you havent already take the wooden sword. Good luck, and be careful """)

old_man.set_conversation("""
Oh hello my friend! You must be the fine boy the village leader was talking about. I hope your journey so far has been safe.
If you haven't taken it already, take this bread and water.
Good luck on your journey boy!""")

guard_1.set_conversation("""
WHO ARE YOU?
ANOTHER BOY WHO WANTS THE RECIPE?""")





#creating items
wooden_sword = Item('Wooden Sword', 'A simple blade to get the job done')
town_hall.set_item(wooden_sword)
bread = Item('Bread','Food for thought, and health')
water = Item('Water','Its just water')





#creating weaknesses
attacker_1.weakness = wooden_sword.name




#where the game runs
current_room = home
possibleDirections = ['north','south','east','west']
bag = []
dead = False

while dead == False:
    print('\n')
    current_room.describe()
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.describe()
    command = input('> ')
    if command.lower() in possibleDirections:
        current_room = current_room.move(command.lower())
    elif command.lower() == 'talk':
        #talking to the inhabitant, if there is one
        if inhabitant is not None:
            inhabitant.talk()
    elif command.lower() == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print(f"What will you fight with? You have:")
            if len(bag) > 0:
                for i in range(len(bag)):
                    print(bag[i])
            fight_with = input()
            if fight_with in bag:
                print(f'You have that')  
            else:
                print("you don't have a "+fight_with)
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                if Enemy.enemies_to_defeat == 0:
                    print("Congratulations, you have survived another adventure")
                    dead = True
                print("Bravo,hero you won the fight!")
                current_room.set_character(None)
            else:
                print("Scurry home, you lost the fight.")
                dead = True
        else:
            print("There is no one here to fight with")
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
            bag.append(item.get_name())
            current_room.set_item(None)
