
# coding: utf-8

# In[1]:

#defining all items and weapons needed for game
#import pdb
class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        #allows us to define specifics about the item
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    #this is mainly for me, so I can get helpful information about my items

class Dollar(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Dollar",
                         description="A green bill worth {} that can be exchanged for goods and services.".format(str(self.amt)),
                         value=self.amt)

#need other items other than currency
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Your fists",
                      description= "Not very powerful, but they're what your mama gave ya.",
                      value=0,
                      damage=3)

class Purse(Weapon):
    def __init__(self):
        super().__init__(name="A Coach Purse",
                      description="A birthday gift from your Aunt. It's very expensive.",
                      value=100,
                      damage=10)

class Creamer(Weapon):
    def __init__(self):
        super().__init__(name="Lowfat Coffee Creamer",
                      description="A tiny container of coffee creamer. Good for making coffee taste less bad.",
                      value=1,
                      damage=5)

class Mace(Weapon):
    def __init__(self):
        super().__init__(name="Mace",
                      description="The can of mace your father gave you freshman year. Why is it still on your keychain?",
                      value=15,
                      damage=20)

class Coupon(Weapon):
    def __init__(self):
        super().__init__(name="Expired Coupon",
                      description="A crumpled, expired coupon from your purse. The edges are still sharp though.",
                      value=0,
                      damage=5)

class Textbook(Weapon):
    def __init__(self):
        super().__init__(name="Textbook",
                      description= "Your textbook for Research Writing. It's heavy and you've never opened it.",
                      value=50,
                      damage=15)

class Backpack(Weapon):
    def __init__(self):
        super().__init__(name="Blue Backpack",
                      description= "Lee Pelton's blue backpack. He carries this everywhere. He must be worried.",
                      value=100,
                      damage=50)

