class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.characters = None
        self.item = None

    #get the desrciption of the room
    def describe(self):
        print(f"{self.name} \n {self.description}")

    #set the description of the room
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    #get the name of the room
    def get_name(self):
        return self.name

    #set the name of the Room
    def set_name(self, new_name):
        self.name = new_name

    def set_character(self, character):
        self.characters = character

    def get_character(self):
        return self.characters

    def get_item(self):
        return self.item
    
    def set_item(self, item_name):
        self.item = item_name

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The "+ room.get_name()+ " is " + direction + '. Enter ['+ direction + '] to go there')
    
    
    #link the rooms in an order
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self





