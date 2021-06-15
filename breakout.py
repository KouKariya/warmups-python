# Warmup project to refresh python skills and knowledge written in Python 3.9
# By Jesse Gallarzo
# coding=utf-8

#TODO add a random variable for buffs

#Game Variables
killer_health = 10
killer_attack = 2
survivor_health = 7
survivor_attack = 1
escaped = False

#Game State
while(escaped is False and killer_health > 1 or escaped is False and survivor_health > 1):
    action = input("You're being attacked! What do you do? FIGHT? or RUN? ")

    if action == "RUN":
        escaped = True
        print("You got away safely!")

    elif action == "FIGHT":
        killer_health = killer_health - survivor_health
        survivor_health = survivor_health - killer_attack
        print("The killer takes " + str(survivor_attack) + " damage!")
        print("You take " + str(killer_attack) + " damage!")

    if survivor_health <= 0:
        print("The killer got to you. Game over...")
    elif killer_health <= 0:
        print("You managed to fend off the attacker and survived!")
        print("Game over!")
