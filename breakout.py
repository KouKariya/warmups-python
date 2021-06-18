# Warmup project to refresh python skills and knowledge written in Python 3.9
# By Jesse Gallarzo
# coding=utf-8

#Character Variables
# / HP/ ATT/ SPD/
killer_stats = [7,3,3]
killer_health = 7
killer_attack = 3
killer_speed = 3

# / HP/ ATT/ SPD/ LCK/
survivor_stats = [7,2.5,4,1]
survivor_health = 7
survivor_attack = 2.5
survivor_speed = 4
#survivor_luck = 1

#Game Variables
escaped = False

#TODO create function that deal with dispensing damage to characters and turn order
def battle(sur_hp,kil_hp,sur_attack,kil_attack,sur_speed,kil_speed):
    #Define global methods to change killer's and survivor's health
    if (sur_speed > kil_speed):
        killer_stats[0] = kil_hp - sur_attack
        print("The killer takes " + str(sur_attack) + " damage!")
        survivor_stats[0] = sur_hp - kil_attack
        print("You take " + str(sur_attack) + " damage!")

    elif (kil_speed > sur_speed):
        survivor_stats[0] = sur_hp - kil_attack
        print("You take " + str(sur_attack) + " damage!")
        killer_stats[0] = kil_hp - sur_attack
        print("The killer takes " + str(sur_attack) + " damage!")

#Game State
print ("You're being attacked!")
while(escaped is False and killer_health >= 1 or escaped is False and survivor_health >= 1):

    #Playable actions for the Player
    action = input("What do you do? FIGHT? or RUN? ")

    print("Killer Health: " + str(killer_health))
    print("Survivor's health: " + str(survivor_health))

    #Escape from attack
    if action == "RUN":
        escaped = True
        print("You got away safely!")

    #Fight the monster
    elif action == "FIGHT":
        battle(survivor_stats[0], killer_stats[0], survivor_stats[1], killer_stats[1], survivor_stats[2],killer_stats[2])
        #killer_health = killer_health - survivor_attack
        #survivor_health = survivor_health - killer_attack
        #print("The killer takes " + str(survivor_attack) + " damage!")
        #print("Killer Health: " + str(killer_health))
        #print("You take " + str(killer_attack) + " damage!")
        #print("Survivor's health: " + str(survivor_health))

    #Resolve game state.
    if survivor_health <= 0:
    #TODO fix how turns resolve here for characters
        #escaped = True
        print("The killer got to you. Game over...")
    elif killer_health <= 0:
        escaped = True
        print("You managed to fend off the attacker and survived!")
        print("Game over!")

    #If none of the game states resolve, gather new 'action' input and restart
