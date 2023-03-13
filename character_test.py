from character import Enemy, Friend, Character

"""
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Hey boy!")

dave.set_weakness("cheese")
dave.add_item("fork")
dave_has = dave.show_inventory()
print(dave_has)
dave.steal("fork")
dave_has = dave.show_inventory()
print(dave_has)
"""
oogway = Friend("oogway", " an old tortoise")
oogway.set_conversation("I see a Dragon Warrior in you.")
oogway.add_item("sword")
oogway_has = oogway.show_inventory()
print(oogway_has)
oogway.gift("apple")
oogway_has = oogway.show_inventory()
print(oogway_has)
oogway.borrow("sword")
oogway_has = oogway.show_inventory()
print(oogway_has)
