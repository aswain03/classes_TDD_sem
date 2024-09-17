class Create_player:
    def __init__(self, name="Tav"):
        self.name = name
        self.stats = {}
        self.backpack = []
        self.level = 1
        self.capacity = 10

    def add_stats(self, name, value):
        self.stats[name] = value
        return f"{value} points added to {name}"

    def add_to_backpack(self, item):
        if len(self.backpack) < self.capacity:
            self.backpack.append(item)
            return f"{item} added to backpack"
        return "Backpack is full"

    def show_backpack(self):
        print(self.backpack)
        return self.backpack

    def increase_backpack_capacity(self, value):
        self.capacity += value
        return f"Backpack capacity increased by {value}"

    def level_up(self, name):
        self.level += 1
        self.stats[name] += 5
        return f"You leveled up! {name} increased by 5 points"

        """
        
        Learning Objectives:
        - Practice testing classes and methods
        - Create a class with attributes and methods
        - Applying good TDD practices
        
        Let's create a class that represents creating a player in a game.
        The class is going to need these attributes:
        - a name property (str)
        - a stats property (dict)
        - an inventory property (list)
        - a capacity property (int)
        - a level property (int)
    
        The class is going to need these methods:
        - add_stats(name, value) - adds a stat to the stats property
        - add_to_backpack(item) - adds an item to the inventory property
        - increase_backpack_capacity(value) - increases the capacity property by the value
        - level_up(name) - increases the level property by 1 and increases the value of the named property by 5
        """
