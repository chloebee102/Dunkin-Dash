
# coding: utf-8

# In[14]:

#defining all enemies for game
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    #defining enemy characteristics
    def is_alive(self):
        return self.hp > 0
    #to check our enemies are alive, lol

class Baby(Enemy):
    def __init__(self):
        super().__init__(name="Baby in a stroller", hp=10, damage=1)
    
class Pidgeon(Enemy):
    def __init__(self):
        super().__init__(name="Pidgeon", hp=20, damage=5)

class Starbucks(Enemy):
    def __init__(self):
        super().__init__(name="Starbucks Employee", hp=30, damage=10)

class Clubgoer(Enemy):
    def __init__(self):
        super().__init__(name="Drunk Clubgoer", hp=5, damage=2)

class GriddlerEmployee(Enemy):
    def __init__(self):
        super().__init__(name="Griddler's Employee", hp=20, damage=10)

class CityPlace(Enemy):
    def __init__(self):
        super().__init__(name="CityPlace Guard", hp=5, damage=1)

class Pelton(Enemy):
    def __init__(self):
        super().__init__(name="Lee Pelton", hp=50, damage=15)

class TourGuide(Enemy):
    def __init__(self):
        super().__init__(name="Emerson Tour Guide", hp=25, damage=5)

class Securitas(Enemy):
    def __init__(self):
        super().__init__(name="Securitas Guard", hp=5, damage=1)

class Sodexo(Enemy):
    def __init__(self):
        super().__init__(name="Sodexo Employee", hp=1, damage=30)

class Dunkin(Enemy):
    def __init__(self):
        super().__init__(name="Dunkin' Employee", hp=100, damage=30)

class Stairs(Enemy):
    def __init__(self):
        super().__init__(name="Stairs", hp=5, damage=5)

