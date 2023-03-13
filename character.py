class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.inventory = []

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description)
        print( self.inventory)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def add_item(self, new_item):
        self.inventory.append(new_item)

    def show_inventory(self):
        return self.inventory



class Enemy(Character):

    number_of_enemies = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.number_of_enemies = Enemy.number_of_enemies + 1

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def steal(self, item):
        if item in self.inventory:
            self.inventory = self.inventory.remove(item)
            return self.inventory
        else:
            print(self.name + " does not have " + item)

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print("[" + self.name + " says]: Thanks, I needed that hug")


    def gift(self, new_item):
        print("[" + self.name + " says]: Thank you for gifting me " + new_item)
        self.inventory.append(new_item)

    def borrow(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return self.inventory
        else:
            print(self.name + " does not have " + item)
