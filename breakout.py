# Warmup project to refresh python skills and knowledge written in Python 3.9
# By Jesse Gallarzo
# coding=utf-8

#Character Variables
killer_health = 7
killer_attack = 3
#killer_speed = 3

survivor_health = 7
survivor_attack = 2.5
#survivor_speed = 4
#survivor_luck

#Game Variables
escaped = False

#TODO create function that deal with dispensing damage to characters and turn order
def battle():
    print("This is a test")
    #Function that deals with order of attacks and calcuating damage

#Game State
print ("You're being attacked!")
while(escaped is False and killer_health >= 1 or escaped is False and survivor_health >= 1):

    #Playable actions for the Player
    action = input("What do you do? FIGHT? or RUN? ")

    #Escape from attack
    if action == "RUN":
        escaped = True
        print("You got away safely!")

    #Fight the monster
    elif action == "FIGHT":
        killer_health = killer_health - survivor_attack
        survivor_health = survivor_health - killer_attack
        print("The killer takes " + str(survivor_attack) + " damage!")
        print("Killer Healt: " + str(killer_health))
        print("You take " + str(killer_attack) + " damage!")
        print("Survivor's health: " + str(survivor_health))

    #Resolve game state.
    if survivor_health <= 0:
    #TODO fix how turns resolve here for characters
        #escaped = True
        print("The killer got to you. Game over...")
    elif killer_health <= 0:
        escaped = True
        print("You managed to fend off the attacker and survived!")
        print("Game over!")

    #If none of the game states reslove, gather new 'action' input and restart
