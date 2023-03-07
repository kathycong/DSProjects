from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import Item

#Create black magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 12, 124, "black")
blizzard = spell("Blizzard", 10, 100, "black")
meteor = spell("Meteor", 20, 200, "black")
quake = spell("Quake", 14, 140, "black")

#Create white magic
cure = spell("Cure", 12, 120, "white")
cura = spell("Cura", 18, 200, "white")

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
#adding quantity in 4.42
player_items = [{"item" : potion, "quantity" : 15},  {"item": hipotion, "quantity": 5},
                {"item" : superpotion, "quantity": 5},  { "item" : elixer, "quantity" : 5},
                {"item" : hielixer, "quantity": 2}, {"item" : grenade, "quantity": 5}]

#instatiated the person class
#player magic
player1 = Person("Valos:", 3260, 65, 60, 34, player_spells, player_items)
player2 = Person("Nick :", 4160, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot:", 3089, 65, 60, 34, player_spells, player_items)
enemy = Person("Magus:", 1200, 65, 45, 25, [], [])

players = [player1, player2, player3]


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

    for player in players:

        player.choose_action()
        choice = input("    Choose action:")
        #in programming we count at 0 not 1 reason we reduce the choice to 0
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for", dmg, "points of damage.") #Enemy HP:", enemy.get_hp())

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
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage"  + bcolors.ENDC)

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
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP/MP" + bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "/n" + item.name + "deals", str(item.prop), "points of damage" + bcolors.ENDC)


    #now we want the enemy to attack us
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg) #, "Player HP", player.get_hp())

    print("===================================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    
#need to determine if the battle is over when stats are 0
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp()  == 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False

#to defeat the enemy we need to get the player to do more things like heal or do more damage
#choosing the magic


   # print("You chose", player.get_spell_name(int(choice)))

   # running = False
