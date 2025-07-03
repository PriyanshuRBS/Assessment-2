from timespacer import time_text, time_text_spacer

def help():
    time_text_spacer('There are some important things you need to learn',2)
    time_text('First of all,',1.5)
    time_text('To move around places', 1)
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
What's your command? >  west""", 4)

    time_text("Next, to pick up items", 2)
    time_text_spacer("simply enter [take] in the command line, the same place as where you put the direction. Do it as shown below", 5)
    time_text_spacer("""
Welcome to:
                     
A place in the centre of the village, lively with people
The home is east
The Road 1 is west
Village Leader is here!
He's the leader of the village, running things and giving people tasks
the [Wooden Sword] is here - It's a weak little blade, but it gets the job done!
What's your command? > take""", 3)
    time_text_spacer("This also applies for comannds such as [fight], [pat], [eat] and [talk]",5)

    time_text("When you will fight, you will get the option to do a strong attack or weak attack",4)
    time_text("Remember this - A strong attack gives double the attack power,",4)
    time_text_spacer(' but reduces the durability by 3 times as much as a weak attack',3)
    