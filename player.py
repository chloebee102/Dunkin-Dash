
# coding: utf-8

# In[16]:

import random
import items, world
#import pdb

class Player():
    def __init__(self):
        #pdb.set_trace()
        self.inventory = [items.Fists()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
 
    def is_alive(self):
        return self.hp > 0
 
    def do_action(self, action, **kwargs): #player needs to be able to take an action
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    #setting up movement actions
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_up(self):
        self.move(dx=0, dy=-1)
 
    def move_down(self):
        self.move(dx=0, dy=1)
 
    def move_right(self):
        self.move(dx=1, dy=0)
 
    def move_left(self):
        self.move(dx=-1, dy=0)

    #defining the attack for the player
    def attack(self, enemy):
        best_weapon = None 
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon): #cycles through weapons to find the best one
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
     #setting up print message for attacks
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
            #allows player to flee, sending them to a random tile
            available_moves = tile.adjacent_moves()
            r = random.randint(0, len(available_moves) - 1)
            self.do_action(available_moves[r])

