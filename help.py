from timespacer import time_text, time_text_spacer

def help():
    time_text_spacer('There are some important things you need to learn',2)
    time_text('First of all,',1.5)
    time_text('To move around places', 1)
    time_text_spacer('You will need to enter the direction you want to go in',3)
    time_text_spacer('look at the following example - ',2)

    time_text_spacer("""
WELCOME TO:
home
Your home with a big sign that says Jarad's home
The Town Hall is west. Enter [west] to go there
What's your command? > """, 3)
    time_text_spacer("In this example you must enter [west] to move to the next place. look below and see how to enter", 3)
    time_text_spacer("""
WELCOME TO:
home
Your home with a big sign that says Jarad's home
The Town Hall is west. Enter [west] to go there
What's your command? > west""", 3)

    time_text("Next, to pick up items", 2)
    time_text_spacer("simply enter [take] in the command line, the same place as where you put the direction. Do it as shown below", 5)
    time_text_spacer("""
WELCOME TO:
Town Hall  
A place in the centre of the village, lively with people
The home is east. Enter [east] to go there
The Road 1 is west. Enter [west] to go there
Village Leader is here!
He's the leader of the village, running things and giving people tasks
the [Wooden Sword] is here - It's a weak little blade, but it gets the job done!
What's your command? > take""", 3)
    time_text_spacer("This also applies for comannds such as",1)
    time_text('[talk] - a command entered to talk to the person in the room',1)
    time_text('[eat] - a command entered to eat food you have picked up',1)
    time_text('[inventory] - a command entered to check what you have in your bag',1)
    time_text('[health] - a command entered to check your health')
    time_text_spacer("Anything in the square brackets will be a command",2)


    time_text("When you will fight, you will get the option to do a strong attack or weak attack",4)
    time_text("Remember this - A strong attack gives double the attack power,",3)
    time_text(' but reduces the durability by 3 times as much as a weak attack',3)
    time_text_spacer('But has a 1 in 3 chance of doing a critical hit', 2)
    
    time_text_spacer('Remember at any time you can look at this again by entering [help] in the command line', 3)