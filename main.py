from room import Room
from character import Character, Friend, Enemy
from item import Item, Weapon, Food
import time

#testing


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
Hello there young warrior. I have chosen you to complete a mission, a daring a difficult one,
but one I think you will succeed in, for all of our futures.

   Our village needs you to take back the Great Curry Recipe that has been rightfully ours, from The Great Evil King.
    I have a spy in the King's castle, who tells me that the recipe is stored in the dungeon.

    On the path you will follow there will be a hut, where a close friend of mine will take care of you for a night.
     Remember that on the path there are wild men and criminals. If you havent already take the wooden sword. Good luck, and be careful """,15)

old_man.set_conversation("""
Oh hello my friend! You must be the fine boy the village leader was talking about. I hope your journey so far has been safe.
If you haven't taken it already, take this bread and water, and a better sword. That wooden sword wont help you fight the king's men
Good luck on your journey boy!""",15)







#creating items
wooden_sword = Weapon('Wooden Sword', 'A simple blade to get the job done', 30, 10)
town_hall.set_item(wooden_sword)
iron_sword = Weapon('Iron Sword','A sharp sleek iron sword', 60, 20)
hut.set_item(iron_sword)
enchanted_sword = Weapon('Enchanted Sword', 'A heavenly blade with immense power', 100, 30)
zoogar_berry = Food('Zoogar Berry', 'A quick special food to heal up',100)
kitchen.set_item(zoogar_berry)






#creating weaknesses
attacker_1.weakness = wooden_sword.name




#where the game runs
current_room = home
possibleDirections = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest']
health = 100
bag = []
dead = False
hastalked = False
eaten_food = None
food_found = False

while dead == False:
    print('\n')
    current_room.describe()
    time.sleep(0.1)
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
            if health > 100 and health > 95:
                health += 100 - health
            elif health > 100 and health < 95:
                health += 5
            
    elif command.lower() == 'talk':
        #talking to the inhabitant, if there is one

        if inhabitant is not None:
            inhabitant.talk()
            hastalked = True
            print(hastalked)
            

            
    elif command.lower() == "fight":
        if inhabitant and isinstance(inhabitant, Enemy):

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
                    

        # ---------- FIGHT ----------
        # fight returns the *updated* health & dead flag
            health, dead, bag = inhabitant.fight(choice, health, dead, current_room, bag)

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
                    health = 200
                food_found = True
            if food_found == True:
                break
        if food_found == False:
            print('There is no food to eat')
            
    else:
        print("""OOPS! 
              Semms you have entered an invalid command, try agian.""")
        time.sleep(0.3)
