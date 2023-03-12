from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import Item
import random

#Create black magic
fire = spell("Fire", 25, 600, "black")
thunder = spell("Thunder", 25, 600, "black")
blizzard = spell("Blizzard", 25, 600, "black")
meteor = spell("Meteor", 40, 1200, "black")
quake = spell("Quake", 14, 140, "black")

#Create white magic
cure = spell("Cure", 25, 620, "white")
cura = spell("Cura", 32, 1500, "white")

#each spell has a name2
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 12, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100},
        {"name": "Meteor", "cost": 20, "dmg": 200}]

#Create Some Item (section 4.41 )
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 999) #heals the max HP
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#adding a variable to simplify instantiate the players
player_spells = [fire, thunder, blizzard, meteor, cure, cura]

enemy_spells = [fire, meteor, cure]

#adding quantity in 4.42
player_items = [{"item" : potion, "quantity" : 15},  {"item": hipotion, "quantity": 5},
                {"item" : superpotion, "quantity": 5},  { "item" : elixer, "quantity" : 5},
                {"item" : hielixer, "quantity": 2}, {"item" : grenade, "quantity": 5}]

#instatiated the person class
#player magic
player1 = Person("Valos:", 3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_spells, player_items)

enemy1 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])
enemy2 = Person("Magus", 11200, 701, 525, 25, enemy_spells, []) #putting this
enemy3 = Person("Imp  ", 1250, 130, 560, 325, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]


#print(player.generate_damage())
#print(player.generate_damage())
#print(player.generate_damage())

#print(player.generate_spell_damage(0))
#print(player.generate_spell_damage(1))

#setting the battle
running = True
i = 0

#make sure that bcolors.ENDC is added so it ends the formatting
print(bcolors.FAIL + bcolors.BOLD + "An ENEMY ATTACKS!" + bcolors.ENDC)
#print("This is a normal attack") #there is no ref bold formatting because of ENDC

while running:
    print("===================================================")

    #one loop that the prints out the stats
    print("\n\n")
    print("NAME                        HP                                   MP                     ")

    for player in players:
        player.get_stats()
        print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        player.choose_action()
        choice = input("    Choose action:")
        #in programming we count at 0 not 1 reason we reduce the choice to 0
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked" + enemies[enemy].name.replace(" ", "") + " for", dmg, "points of damage.") #Enemy HP:", enemy.get_hp())

            #removing enemy with 0 hp from the enemy list
            if enemies[enemy].get_hp == 0:
                print(enemies[enemy].name + " has died.")
                del enemies[enemy]

        #adding magic
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            #Updated with below code
            #magic_dmg = player.generate_spell_damage(magic_choice)
            #reduce the magic point bey cost of that spell
            #spell = player.get_spell_name(magic_choice)
            #cost = player.get_spell_mp_cost(magic_choice) 
            
            #this should allow us to go back to the main menu
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg =spell.generate_damage()
            
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue #this goes back to the beginning
            
            player.reduce_mp(spell.cost)

            if spell.type == "white" :
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)

            elif spell.type == "black":    
                #get the enemy to take the damage
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to" + enemies[enemy].name.replace(" ", "")  + bcolors.ENDC)

                #removing enemy with 0 hp from the enemy list
                if enemies[enemy].get_hp == 0:
                    print(enemies[enemy].name + " has died.")
                    del enemies[enemy]

        #adding items from section 4.41
        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            #this should allow us to go back to the main menu
            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            #checking if player has enough items to be used
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left . . ."  + bcolors.ENDC)
                continue #continue is used here to allow us to choose again

            #reducing the number of quantity items once it's being used
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
                
            elif  item.type == "elixer":

                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(dmg)
                print(bcolors.FAIL + "/n" + item.name + "deals", str(item.prop), "points of damage to " + enemies[enemy].name.replace(" ", "") + bcolors.ENDC)

                      #removing enemy with 0 hp from the enemy list
                if enemies[enemy].get_hp == 0:
                    print(enemies[enemy].name.replace(" ", "") + " has died.")
                    del enemies[enemy]

    # check if battle is over
    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp == 0:
            defeated_players += 1

    # check if Player won
    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    #check if Enemy won
    elif defeated_enemies == 2:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False


    #Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        
        if enemy_choice == 0:
            #Chose attack
            target = random.randrange(0, 3)
            enemy_dmg = enemy.generate_damage()

            players[target].take_damage(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for", enemy_dmg)

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            print("Enemy chose", spell, "damage is", magic_dmg)

            if spell.type == "white" :
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals", enemy.name + " for", str(magic_dmg) + bcolors.ENDC)

            elif spell.type == "black":    
                #get the enemy to take the damage
                target = random.randrange(0, 3)
                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + enemy.name.replace(" ", "") + "'s" + spell.name + " deals", str(magic_dmg), "points of damage to" + players[target].name.replace(" ", "")  + bcolors.ENDC)

                #removing enemy with 0 hp from the enemy list
                if players[target].get_hp == 0:
                    print(players[target].name.replace(" ", "") + " has died.")
                    del players[target]

#https://github.com/nickgermaine/python_text_battle