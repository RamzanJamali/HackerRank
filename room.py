class Room():

    number_of_rooms = 0

    def __init__(self,room_name):
        self._name = room_name
        self._description = None
        self._linked_rooms = {}
        self.character = None
        self._item = []
        Room.number_of_rooms = Room.number_of_rooms + 1

    @property
    def description(self):
        return self._description


    @description.setter
    def description(self, room_description):
        self._description = room_description

    def set_item(self, new_item):
        self._item.append(new_item)

    def get_items(self):
        return self._item

    def describe(self):
        print(self._name)
        print(self._description)
        for item in self._item:
            print(str(item.name) + "\t" + str(item.description) + "\t \t" + (item.size))

    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, new_room):
        self._name = new_room

    def link_room(self, room_to_link, direction):
        self._linked_rooms[direction] = room_to_link

    def get_character(self):
        return self.character

    def set_character(self, new_character):
        self.character = new_character

    def remove_character(self):
        self.character = None

    def get_details(self):
        self.describe()
        for direction in self._linked_rooms:
            room = self._linked_rooms[direction]
            print("The " + room.name + " is " + direction)

    def move(self, direction):
        if direction in self._linked_rooms:
            return self._linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def take(self, take_item, backpack):
        i = 0
        for take_it in self._item:
            if take_item == self._item[i].name:
                take_item = self._item[i]
                backpack.append(take_item)
                self._item.remove(take_item)
                print("Item is now in backpack")
                break
            i = i + 1
            print("Item not in list")


    def item_list(self):
        k = 0
        items = []
        for j in self._item:
            items.append(self._item[k].name)
            k = k + 1

        return items







