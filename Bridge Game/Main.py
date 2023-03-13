#The Bridge Game
from areas import Areas
from bridges import Bridges

# Defining some areas
area_1 = Areas("area_1")
area_1.description = "Centre area of the game"

area_2 = Areas("area_2")
area_2.description = "Downtown or south side area"

# Defining first Bridge
bridge_1_2_1 = Bridges("bridge_1_2_1")
bridge_1_2_1.description = "This bridge connects area_1 with area_2"
bridge_1_2_1.linked_area(area_1.name, area_2.name)

# Defining second Bridge
bridge_1_2_2 = Bridges("bridge_1_2_2")
bridge_1_2_2.description = "This bridge connects area_1 with area_2"
bridge_1_2_2.linked_area(area_1.name, area_2.name)

# Linking areas
area_1.near_area(area_2, "south")
area_2.near_area(area_1, "north")
area_1.set_bridge(area_2, bridge_1_2_1.name)
area_1.set_bridge(area_2, bridge_1_2_2.name)

# Testing
area_1.describe()
print("\n")
area_2.describe()
# bridge_1_2_1.describe()