
# coding: utf-8

# In[14]:

print("Welcome to Dunkin' Dash! Get your morning coffee before it's too late!")
print("By Chloe Warfford")

__author__ = 'Chloe Warfford'
import world
#import pdb
from player import Player
 
#setting up gameplay
def play():
    #pdb.set_trace()
    world.load_tiles()
    player = Player()
    #load the starting room and introduction
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check state, just in case
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action) #show actions
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs) #hotkey executes the action
                    break  
        elif not player.is_alive():
            print("You died! And ghosts can't order coffee!")
            
            
if __name__ == "__main__":
    play()

