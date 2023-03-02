from classes.game import Person, bcolors
from classes.magic import spell

#Create black magic
fire = spell("Fire", 10, 100, "black")
thunder = spell("Thunder", 10, 100, "black")
blizzard = spell("Blizzard", 10, 100, "black")
meteor = spell("Meteor", 20, 200, "black")
quake = spell("Quake", 14, 140, "black")

#Create white magic
cure = spell("Cure", 12, 120, "white")
cura = spell("Cura", 18, 200, "white")

#each spell has a name
magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 12, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]

#instatiated the person class
#player magic
player = Person(460, 65, 60, 34, [fire, thunder, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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
    player.choose_action()
    choice = input("Choose action:")
    #in programming we count at 0 not 1 reason we reduce the choice to 0
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.") #Enemy HP:", enemy.get_hp())

    #adding magic
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        #Updated with below code
        #magic_dmg = player.generate_spell_damage(magic_choice)
        #reduce the magic point bey cost of that spell
        #spell = player.get_spell_name(magic_choice)
        #cost = player.get_spell_mp_cost(magic_choice) 

        spell = player.magic[magic_choice]
        magic_dmg =spell.generate_damage()
        
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue #this goes back to the beginning

        player.reduce_mp(spell.cost)
        #get the enemy to take the damage
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage"  + bcolors.ENDC)

    #now we want the enemy to attack us
    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg) #, "Player HP", player.get_hp())

    print("===================================================")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)


    #printing the magic points
    print("You MP : ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")
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
