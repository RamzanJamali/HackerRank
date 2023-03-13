class Item():

    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.weight = None

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.name)
        print(self.description)

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size
