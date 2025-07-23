from os import system, name
#a system that clears the screen after every input so it is easier to read
def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")