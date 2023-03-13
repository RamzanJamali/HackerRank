# The bridges
class Bridges():
    def __init__(self, bridge_name):
        self.name = bridge_name
        self.description = None
        self.linked_areas = {}

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def linked_area(self, first_area, second_area):
        self.linked_areas[first_area] = second_area

    def describe(self):
        print(self.name)
        print(self.description)
        for area_a in self.linked_areas:
            area_b = self.linked_areas[area_a]
            print("The bridge connects " + area_a + " with " + area_b)
            print("\n")
