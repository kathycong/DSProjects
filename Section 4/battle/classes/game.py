import random
from .magic import spell
import pprint #importing pretty print

#setting colors and other formatting
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #ends the formatting code
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#need to initialise this class with a few parameters
#this class contains statistics
class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic #dictionary of magic spells 
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

#need utilities method to handle the battle
#methods are usually small
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh) #using randomrange we are making it dynamic

#Below code are no longer needed after the magic class was created
 #   def generate_spell_damage(self, i):
 #       mgl = self.magic[i]["dmg"] - 5
 #       mgh = self.magic[i]["dmg"] + 10
 #       return random.randrange(mgl,  mgh) '''

    #method where the enemy take the damage
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0 :
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    #create utilities to get properteies
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

#Below code are no longer needed after the magic class was created
 #   def get_spell_name(self, i):
 #       return self.magic[i]["name"]

  #  def get_spell_mp_cost(self, i):
   #     return self.magic[i]["cost"] '''

#we need more methods where it can choose either attack or magic
    def choose_action(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1 

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, " (x5)")
            i += 1










