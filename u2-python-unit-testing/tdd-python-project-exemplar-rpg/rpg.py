#import data from other game files (and random)
from hero import Hero
from skeletons import Skeleton
from items import item_master_list
from random import choice

#class to organize central game logic
class Game:
    def __init__(self):
        '''Establish initial game state'''
        self.hero = None
        self.skeleton = None
        self.lost = False
        self.item_list = item_master_list

    def start_game(self):
        '''Reset game state attributes'''
        print("Welcome to Python Quest!")
        print("Your goal is to rescue the python from an army of skeletons.")
        player_name = input("Enter your hero's name: ")
        self.hero = Hero(player_name)
        self.lost = False
        self.item_list = item_master_list
        self.new_item()
        self.hero.show_details()
        self.run_game()

    def new_item(self):
        '''Draw random item from list and add to hero inventory'''
        new_item = choice(self.item_list)
        self.hero.get_item(new_item)

    def run_game(self):
        '''Loop encounters until the hero is level 10 or the game is lost'''
        while (self.hero.level<10) and (not self.lost):
            self.new_encounter()
        print("You find the python and rescue it.  Good job!")
        self.end_game()

    def new_encounter(self):
        '''Generate a new skeleton based on hero level and prompt player choice'''
        self.skeleton = Skeleton(self.hero.level)
        self.choice()

    def choice(self):
        '''Initiate Fight or Flee function based on player choice'''
        player_choice = input("Do you FIGHT or FLEE? ")
        if(player_choice.lower() == "fight"):
            self.fight()
        elif(player_choice.lower() == "flee"):
            self.flee()
        else:
            self.choice()

    def fight(self):
        '''
        Resolve player attack then skeleton attack.
        Advance if player wins.
        End game if player Loses.
        Call recursively until fight resolved.
        '''
        pl_atk = self.hero.strike()
        sk_death = self.skeleton.check_death(pl_atk)
        if not sk_death:
            self.skeleton.show_details()
            sk_atk = self.skeleton.strike()
            pl_death = self.hero.check_death(sk_atk)
            if pl_death:
                self.lost = True
                input("...")
                self.end_game()
            else:
                input("...")
                self.fight()
        else:
            input("...")
            self.advance()

    def flee(self):
        '''
        Resolve player flee attempt.
        End encounter if flee succeeds.
        Skeleton attack if flee fails.
        End game if player dies.
        Otherwise, escalate to fight.
        '''
        if self.hero.speed > self.skeleton.speed:
            print(self.hero.name + " escaped!")
        else:
            print(self.hero.name+ " wasn't fast enought!")
            sk_atk = self.skeleton.strike()
            pl_death = self.hero.check_death(sk_atk)
            if pl_death:
                print("The hero has fallen!")
                self.lost = True
                input("...")
                self.end_game()
            else:
                input("...")
                self.fight()

    def advance(self):
        '''
        Increment player level
        Give the player a new item.
        Display new player stats.
        '''
        self.hero.level += 1
        self.new_item()
        self.hero.show_details()
        input("...")

    def end_game(self):
        '''Reset game if player chooses to.'''
        reset_check = input("Play again? ")
        if (reset_check.lower() == "y" ) or (reset_check.lower() == "yes" ):
            self.start_game()
        elif (reset_check.lower() == "n" ) or (reset_check.lower() == "no" ):
            pass
        else:
            self.end_game()

new_game = Game()
new_game.start_game()