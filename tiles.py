
# coding: utf-8

# In[56]:

#needed to define the plane in which the player moves

import items, enemies, actions, world
#import pdb

class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self): #display info when entering the tile
        raise NotImplementedError()
        
    def modify_player(self, the_player):
        raise NotImplementedError()
        
    def adjacent_moves(self):
        #default actions a player can do
        moves = []
        #pdb.set_trace()
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveRight())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveLeft())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveUp())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveDown())
        return moves
     
    def available_actions(self):
        #Sets up available actions based on room
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
     
        return moves

class BoylstonSt(MapTile):
    def intro_text(self):
        return """
        You find yourself stranded on the sidewalk of Boylston St.
        You can make out the alleyway and Walker Building further down the street.
        """
    
    def modify_player(self, the_player):
        pass

#defining a room that provides items
class ItemRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, the_player):
        the_player.inventory.append(self.item)

    def modify_player(self, the_player):
        self.add_loot(the_player)


#defining a room that holds enemies
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    #prevent enemies from respawning
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))
            
    def available_actions(self): #make non-default actions available
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class CopyCenter(ItemRoom):
    def __init__(self, x , y):
        super().__init__(x, y, items.Dollar(1))
        
    def intro_text(self):
        return """
        As you walk by the Print and Copy Center, you notice something sticking out of the nearby mailbox.
        It's a dollar! You put it in your wallet.
        """

class ColonialTheater(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of Emerson's Campus. Still closed to the public, neat.
        """
    
    def modify_player(self, the_player):
        pass

class Colo(ItemRoom):
    def __init__(self, x ,y):
        super().__init__(x, y, items.Dollar(1))
    
    def intro_text(self):
        return """
        As you pass by Colonial, you decide to pop into the mailroom.
        You have one package to pickup.
        Inside, from your grandma, is a single dollar bill.
        Well at least it's not socks."""

class Sidewalk(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of Boylston St."""
    
    def modify_player(self, the_player):
        pass

class BostonCommon(MapTile):
    def intro_text(self):
        return """
        You walk all the way to the Boston Commons. 
        There's no Dunkin' near here.
        You turn around."""
    
    def modify_player(self, the_player):
        pass

class BarnesandNoble(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dollar(1))
        
    def intro_text(self):
        return """
        You pass by the Barnes and Noble. Inside, overpriced apparel rots.
        You decide to go in. Once inside, you purchase a lanyard.
        The store is so grateful for a customer, they pay you.
        You pocket one dollar.
        """

class TextbookStore(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Textbook())
        
    def intro_text(self):
        return """
        You walk into the Tufte Textbook Store. It's quiet, as usual.
        The clerk at the desk hands you something.
        It's a textbook. You put it away for now.
        """

class PianoRow(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Coupon())
    
    def intro_text(self):
        return """
        You walk into Piano Row. The securitas guard's eyes are glazed over.
        Over on the table are a stack of flyers and coupons.
        You take a coupon, maybe it works at Dunkin'.
        """

class ECPD(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Mace())
        
        
    def intro_text(self):
        return """
        You walk up the ramp into the ECPD Office. There is a faint sound of crickets.
        As you pass by the window, a can of Mace sit unattended.
        You pocket the Mace.
        """

class Dunkin(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Creamer())
        
    def intro_text(self):
        return """
        Finally, you walk into the Dunkin' Donuts. The line is massive.
        So very, very massive.
        As you wait in line, a coffee creamer rolls along the floor.
        You pick up and pocket the coffee creamer.
        """

class Lockers(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Backpack())
    
    def intro_text(self):
        return """
        As you walk up the stairs of the Campus Center, you end up in the hallway near the Max.
        To the left of this hallway is a row of Grad Student lockers.
        Sitting forlornly near one is a blue backpack. You pick it up.
        """

class Sidewalk2(ItemRoom):
    def __init__(self, x, y):
        print("Sidewalk2 init")
        super().__init__(x, y, items.Purse())
        
    def intro_text(self):
        return """
        As you walk along the sidewalk, you notice a bag at your feet.
        It's your purse! Whoops, how did that get here?"""

class WalkerB(MapTile):
    def intro_text(self):
        return """
        As you leave the alley and enter the basement of Walker, the securitas guard stares.
        You rummage through your pockets for your ID. It's not there.
        You dejectedly turn around and leave Walker.
        """
    
    def modify_player(self, the_player):
        pass

class Alley(MapTile):
    def intro_text(self):
        return """
        The sidewalk ends and turns to brick. You look to your left and see the alleyway.
        Down at the end of the alleyway, lies City Place.
        """
    
    def modify_player(self, the_player):
        pass

class Alley2(MapTile):
    def intro_text(self):
        return """
        Another uneven, brick pathway in the alleyway.
        """
    
    def modify_player(self, the_player):
        pass

class CampusCenter(MapTile):
    def intro_text(self):
        return """
        You pass through the hallway of Piano Row and head up the flight of stairs to the Campus Center.
        Watch out for the spilled mozzarella sticks on the stairs!
        """
    
    def modify_player(self, the_player):
        pass

class Tufte(MapTile):
    def intro_text(self):
        return """
        You swing open the large doors to the Tufte Building.
        You walk inside.
        """
    
    def modify_player(self, the_player):
        pass

class Doorway(MapTile):
    def intro_text(self):
        return """
        You go to open the doorway to City Place. You have to use both hands.
        The doors are heavy and you are weak.
        """
    
    def modify_player(self, the_player):
        pass

class Foodcourt(MapTile):
    def intro_text(self):
        return """
        Another greasy part of the City Place foodcourt.
        """
    
    def modify_player(self, the_player):
        pass

class Doorway2(MapTile):
    def intro_text(self):
        return """
        You go to leave City Place. You can't.
        The Dunkin' is literally right there.
        Try again, kid.
        """
    
    def modify_player(self, the_player):
        pass

class DiningCenter(MapTile):
    def intro_text(self):
        return """
        You go to enter the Dining Center. A sodexo employee stops you.
        You don't live on campus.
        You're out of meal swipes.
        You shall not pass.
        """
    
    def modify_player(self, the_player):
        pass
#
#class Sidewalk2(ItemRoom):
#    def __init__(self, x, y, item):
#        super().__init__(x, y, items.Purse())
#        
#    def intro_text(self):
#        return """
#        As you walk along the sidewalk, you notice a bag at your feet.
#        It's your purse! Whoops, how did that get here?
#        """

class VisitorCenter(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.TourGuide())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An Emerson Tour Guide blocks your path. They brace themselves with their weapon of overexaggerated facts.
            """
        else:
            return """
            The last remaining Tour Guide cowers behind the counter.
            """

class WhiskeySaigon(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Clubgoer())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            From the doors of Whiskey Saigon busts out an obnoxious, drunk club goer looking for a fight. 
            """
        else:
            return """
            The club goer has now resorted to smoking heavily outside the club. You're not sure if this is much better than before.
            """

class Walker(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Securitas())
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Before you can step into the Walker elevators, a lethargic Securitas guard says "ID please."
            """
        else:
            return """
            The Securitas agent is now fast asleep.
            """

class Griddlers(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GriddlerEmployee())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Before you can hurry along the sidewalk, a Griddlers employee stops you. 
            They make eye contact.
            They have a flyer in their hand.
            Oh god no.
            """
        else:
            return """
            The corpse of a dead Griddler's employee rots along the sidewalk.
            """

class CenterStage(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Sodexo())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You decide to stop for mozzarella sticks. 
            But when the Sodexo Employee hands you the box, there's 2 less than usual.
            You can't allow this.
            """
        else:
            return """
            The Sodexo employee is nowhere to be found. Students are looting for mozzarella sticks.
            All is right with the world.
            """

class Tufte2(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Stairs())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            As you enter Tufte, you spot your longtime menace.
            Two fights of stairs.
            """
        else:
            return """
            The stairs will forever be here in Tufte.
            But at least you have now conquered them.
            """

class Alley3(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Pidgeon())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Suddenly, you stop in your tracks. 
            There in the alleyway, staring at you with its beady, little eyes...
            A Pidgeon!
            """
        else:
            return """
            The Pidgeon still sits in the alleyway. But no longer does he stare at you with contempt, but instead with respect.
            """

class Starbucks(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Starbucks())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You walk into the Starbucks. The scent of coffee bitch slaps you in the face.
            "Have you tried our new frappucino?" asks the tired barista.
            """
        else:
            return """
            The barista is still there and still tired, but no longer do they offer you the new frappucino.
            You have won.
            """

class FoodCourt2(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Baby())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A mother carlessly pushing her baby in a stroller walks by.
            As the stroller passes, the baby reaches out and smacks your leg.
            Not today, baby.
            """
        else:
            return """
            There are no strollers to be seen. This is your territory now.
            """

class Dunkin2(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Dunkin())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            Finally! At last! You've reached the end of the line.
            But there before you stands the ultimate and most powerful enemy of your journey.
            The Dunkin' Donuts barista.
            Prepare for battle! (And coffee)
            """
        else:
            return """
            The entire Dunkin' Donuts is on fire. You've defeated them once and for all.
            You may run on Dunkin', but Dunkin' got ran over by you.
            """

class SevenEleven(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Pelton())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You waltz into the 7/11.
            Who is there, but the one and only Prezzy P?
            He's eyeing the last Big Gulp cup.
            Oh no you don't, Lee. 
            """
        else:
            return """
            Lee Pelton is no longer here, but you still smell the faint scent of tuition money.
            """

class TwoB(ItemRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dollar(1))
        
    def intro_text(self):
        return """
        You walk into the lobby of 2B.
        A dollar bill flutters down from the ceiling.
        Woah, this place is literally made of money.
        You pocket the dollar.
        """

class Dunkin3(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... can it be?
        It is! 
        Your morning coffee!
 
 
        Victory is yours!
        """
 
    def modify_player(self, player):
        player.victory = True

