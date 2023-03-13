from room import Room
from item import Item
from character import Enemy, Character, Friend
from rpginfo import RPGInfo

backpack = []

kitchen = Room("kitchen")
kitchen.description = "A dank and dirty room, buzzing with flies"

ballroom = Room("ballroom")
ballroom.description = "A vast room with a shiny wooden floor; huge candlesticks guard the entrance"

dining_hall = Room("dining_hall")
dining_hall.description = "A large room with ornate golden decorations on each wall"

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen,"north")
ballroom.link_room(dining_hall,"east")
dining_hall.link_room(ballroom,"west")

silver = Item("silver")
silver.set_description('A shinig piece of metal')
silver.set_size("2 kg")
ballroom.set_item(silver)
cheese = Item("cheese")
cheese.set_description('Some sweet cheese from Italy.')
cheese.set_size("1 kg")
kitchen.set_item(cheese)

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

drake = Enemy("Drake", "The giant dracula")
drake.set_conversation("Halloween is near!")
drake.set_weakness("silver")
kitchen.set_character(drake)

oogway = Friend("oogway", "An old turtoise")
oogway.set_conversation("I see a Dragon Warrior in you.")
ballroom.set_character(oogway)

#print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
Enemies = Enemy.number_of_enemies
current_room = ballroom

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if Enemies == 0:
        print("Congratulations! You win")
        break

    command = input("> ").lower()
    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("Nobody is in the room!")
    elif command == "fight":
        if inhabitant is not None:
            print("What will you fight with? \t")
            fight_with = input()
            k = 0
            items = []
            for j in backpack:
                items.append(backpack[k].name)
                k = k + 1
            if fight_with in items:
                state = inhabitant.fight(fight_with)
                if state is not True:
                    print("Game over")
                    break
                else:
                    current_room.remove_character()
                    Enemies = Enemies - 1
            else:
                print("You don't have " + fight_with + " in your backpack")
        else:
            print("Nobody is in the room!")
    elif command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "gift":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                gift_item = input("What do you want to gift? ")
                inhabitant.gift(gift_item)
            else:
                print(inhabitant.name + " does not accept gifts.")
        else:
            print("Nobody is in the room!")
    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Friend):
                inhabitant.hug()
            else:
                print("[" + inhabitant.name + " says]: I wouldn't do that if I were you.")
        else:
            print("Nobody is in the room!")
    elif command == "take":
        if current_room._item is not None:
            take_item = input("which item? ")
            current_room.take(take_item, backpack)
        else:
            print("Nothing in the room")
    else:
        print("command not found")


RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()
