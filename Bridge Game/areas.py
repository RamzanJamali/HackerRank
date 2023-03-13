# The areas or rooms
class Areas():
    def __init__(self,area_name):
        self.name = area_name
        self.description = None
        self.bridges = {}
        self.near_areas = {}

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def near_area(self, area_to_link, direction):
        self.near_areas[direction] = area_to_link

    def set_bridge(self, to_area, bridge_number):
        self.bridges[bridge_number] = to_area

    def describe(self):
        print(self.name)
        print(self.description)
        for direction in self.near_areas:
            area = self.near_areas[direction]
            print("The " + area.name + " is in " + direction)
        for start in self.bridges:
            end = self.bridges[start]
            print("The " + start + " connects to " + end.name)

    