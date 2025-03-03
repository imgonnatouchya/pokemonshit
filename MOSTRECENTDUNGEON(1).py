import random
import math
import time

#this while loop is here in case the player wants to keep playing, user is given the option to break it when they lose
continuequestion = "keep going"
while continuequestion != "n":
    # vvvv score (determines difficulty) vvvv
    score = 0
    hiddenscore = 1
    # vvvv stats vvvv
    character = "mystery person"
    hp = 100
    maxhp = 100
    end = 0.00
    atk = 1
    statlist = ["hp", "end", "atk"]
    # vvvv items vvvv
    currentweapon = {"name":"hands", "dmg":10}
    currentshield = {"name":"arms", "end":0.03}
    inventory = {1:"", 2:"", 3:""}
    # vvvv important variables vvvv
    winchoice = ""
    lastevent = "event"
    healcounter = 0
    # -------------------------------------------------------------------------
    enemylist = ["slime", "skeleton", "zombie", "cave bat", "cave dweller"]
    enemylist2 = ["dungeon marauder", "dungeon archer", "wolf", "big slime", "evil dungeon delver"]

    #these functions will be called when defining the stats of the items in positive events.
    def statrollsword():
        '''
        odds for swords

        args: 
            none

        returns: 
            random number
        '''
        return min(random.randint(40,300), random.randint(1,300), random.randint(1,300))
    def statrollshield():
        '''
        odds for shields

        args: 
            none

        returns: 
            random number
        '''
        return min(random.randint(1000,7000)/100, random.randint(1000,7000)/100, random.randint(1000,7000)/100)

    #adjectives, for when gaining an item which will be applied to it
    adjlist = [
        "glittering", 
        "worn", 
        "battle-scarred", 
        "damp", 
        "brand-new", 
        "steel", 
        "silver", 
        "mysterious-looking", 
        "comically large", 
        "comically small", 
        "silly", 
        "paladin's", 
        "the dragon of dorima's"
        ]

    #different character options, all have their own stats and items
    storydict = {
    "outsider":{
        "character":"outsider",
        "story":"you come from a far off land out north of the world. you were raised by a village of nordic people, taught and trained to be strong, powerful, and self-sufficient. you've come here to purge what evil dwells in the caverns.",
        "atk":1.75,
        "end":0.15,
        "weapon":{"name":"heavy handaxe", "dmg":50},
        "shield":{"name":"arms", "end":0.01},
        "inventory":{1:"small attack potion", 2:"", 3:""}
        },
            
    "knight":{
        "character":"knight",
        "story":"you're a rank-and-file member of the queen's guard. you came here to find riches and hopefully be relieved of your duties one day, to live out the rest of your days with family and friends.",
        "atk":1.50,
        "end":0.30,
        "weapon":{"name":"arming sword", "dmg":35},
        "shield":{"name":"round shield", "end":0.15},
        "inventory":{1:"medium hp potion", 2:"", 3:""}
        },

    "mercenary":{
        "character":"mercenary",
        "story":"you want to be rich, no sugarcoating it. you're small and quick, and know the exact weak spots of every single creature. such knowledge required you to prioritize study over body, though.",
        "atk":2,
        "end":0.05,
        "weapon":{"name":"small dagger", "dmg":25},
        "shield":{"name":"arm braces", "end":0.10},
        "inventory":{1:"medium attack potion", 2:"", 3:""}
        }
    }
    items = {
        "atk":{
            "small attack potion":0.50,
            "medium attack potion":1,
            "large attack potion":2,
        },
        
        "end":{
            "small endurance potion":0.15,
            "medium endurance potion":0.30,
            "large endurance potion":0.50,
        },
        
        "hp":{
            "small hp potion":0.25,
            "medium hp potion":0.6,
            "large hp potion":0.9
        }
        
    }
    #events
    positiveevntlist = {
    1:{"text":"\n----------------------------------------\nYippee! (positive event)\nA little goblin holding a tattered bag over it's shoulder skitters past, \nand a sword falls out of the bag. Pick it up? (y/n)", "effect":"dmg", "change":1},
    2:{"text":"\n----------------------------------------\nYippee! (positive event)\nAs you continue, someone carrying a heavy load passes by, \nand asks you to please take something. Help them out and take a shield? (y/n)", "effect":"end", "change":0.01}, 
    3:{"text":"\n----------------------------------------\nYippee! (positive event)\nEntering a shrine, you happen across a statue sculpted after... \nyou? It is holding a sword. Take it? (y/n)", "effect":"dmg", "change":1}, 
    4:{"text":"\n----------------------------------------\nYippee! (positive event)\nYou happen across a pedestal holding a shield. Take it? (y/n)", "effect":"end", "change":0.01},
    5:{"text":"\n----------------------------------------\nYippee! (positive event)\nA small sack lays at your feet. You open it and it contains a sword. Take it? (y/n)", "effect":"dmg", "change":1}
    }
    negativeevntlist = {
    1:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nYou trip. Idiot.", "effect":"end", "change":-0.03}, 
    2:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nYou hear disembodied murmuring all around you, whispering discouraging words.", "effect":"atk", "change":-0.20},
    3:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nYou spot a tall, silhouetted, skinny creature. It stares, so you stare back. \nIt disappears for the blink of an eye, reappears, then sprints away. \nYour arm is now bent backwards.", "effect":"atk", "change":-0.60}, 
    4:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nA stinging headache hits you, and the pain makes it hard to think!", "effect":"end", "change":-0.15},
    5:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nCramp!! That hurts....", "effect":"end", "change":-0.08},
    6:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nThe ceiling trembles, and a rock falls flat on the top of your head.", "effect":"end", "change":-0.08},
    7:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nYou pull a book from a shelf you find, and its contents detail forbidden knowledge.", "effect":"atk", "change":-0.30},
    8:{"text":"\n----------------------------------------\nWomp womp.. (negative event)\nA skeleton with no arms comes sprinting out a corner full speed, right into your swinging arm, and falls apart.", "effect":"atk", "change":-0.20}
    }

    '''vvv all of these are used for rolls. vvv'''
    #determines event stuff
    def evnt2roll():
        '''
        series of things that will happen upon getting an event from a roll, will result in a positive or negative event,
        if positive, give random item, if negative, reduce random stat by random rumber.

        args: 
            none

        returns: 
            random shield, or sword, if positive
            a number to lower either atk or end by, if negative
        '''
        global lastevent
        global end
        global atk
        global currentshield
        global currentweapon
        global hp
        event2 = random.randint(1,50)
        if event2 >= 20:
            #chooses from positive event list randomly
            eventchosen = positiveevntlist[random.randint(1,5)]
            
            #will check if event changes attack or endurance (is sword or shield,) then give input option
            if "dmg" in eventchosen["effect"]:
                eventchosen["change"] = statrollsword()
                choose = input(eventchosen["text"] + "\nIts damage:  " + str(eventchosen["change"]) + "\n Your current " + currentweapon["name"] + "'s damage: " + str(currentweapon["dmg"]) + "\n----------------------------------------\n>")
            elif eventchosen["effect"] == "end":
                eventchosen["change"] = round(0.01*statrollshield(), 2)
                choose = input(eventchosen["text"] + "\nIts endurance:  " + str((eventchosen["change"]%1)*100) + "%\n Your current " + currentshield["name"] + "'s endurance: " + str(currentshield["end"]*100) + "%\n----------------------------------------\n>")
            #if invalid response
            while choose != "y" and choose != "n":
                print("\npick an OPTION!!!\n")
                if eventchosen["effect"] == "dmg":
                    choose = input(eventchosen["text"] + "\nIts damage:  " + str(eventchosen["change"]) + "\n Your current " + currentweapon["name"] + "'s damage: " + str(currentweapon["dmg"]) + "\n----------------------------------------\n>")
                elif eventchosen["effect"] == "end":
                    choose = input(eventchosen["text"] + "\nIts endurance:  " + str(((eventchosen["change"])%1)*100) + "%\n Your current " + currentshield["name"] + "'s endurance: " + str(currentshield["end"]*100) + "%\n----------------------------------------\n>")
            #checks input, then if item gained is sword or shield
            if choose == "y" and eventchosen["effect"] == "dmg":
                currentweapon["name"] = random.choice(adjlist) + " sword"
                print("You got a", currentweapon["name"])
                currentweapon["dmg"] = eventchosen["change"]
                time.sleep(1.5)
            elif choose == "y" and eventchosen["effect"] == "end":
                currentshield["name"] = random.choice(adjlist) + " shield"
                print("You got a", currentshield["name"])
                currentshield["end"] = eventchosen["change"]
                time.sleep(1.5)
            elif choose == "n":
                print("\nYou didn't take the item.\n")
                time.sleep(1.5)
                pass

        else:
            #chooses from negative event list randomly
            eventchosen = negativeevntlist[random.randint(1,8)]
            if eventchosen["effect"] == "atk":
                eventchosen["change"] = round((eventchosen["change"] * score)/20, 2)
                print(eventchosen["text"], "\n" + eventchosen["effect"], eventchosen["change"] )
                atk = round(atk+eventchosen["change"], 2)
                if atk < 1:
                    atk = 1
                print("new atk: " + str(atk) + "\n----------------------------------------\n")
                time.sleep(4)
            elif eventchosen["effect"] == "end":
                eventchosen["change"] = round((eventchosen["change"] * score)/15, 2)
                print(eventchosen["text"], "\n" + eventchosen["effect"] + " " + str(eventchosen["change"]*100) + "%")
                end = round(end+eventchosen["change"], 2)
                if end < 0.01:
                    end = 0.01
                print("new end: " + str(round((end*100), 2)) + "%\n----------------------------------------\n")
                time.sleep(4)


    def enemyroll():
        '''
        when an enemy encounter is rolled for, this function will be used. fights happen inside of here, with 2 main beligerents, the player and enemy.
        enemy stats are random every time function is called, player stats are brought into this function to be used in a fight.

        args: 
            none

        returns: 
            "win"
            "lost"
            "ran"

        '''
        global lastevent
        global atk
        global end
        global hp
        global currentweapon
        global currentshield
        endpotused = False
        atkpotused = False
        miss = False
        parry = False
        totalendbuff = 0
        totalatkbuff = 0
        #enemy strength scaling, scaling affected by set odds and the hidden score
        if hiddenscore > 25:
            print("\n==========================\nYou come across a " + random.choice(enemylist2) + "!\n==========================")
            enemyatk = round(float(random.randrange(151,201))/100 * (hiddenscore/40), 2)
            enemyend = round(float(random.randrange(31,60))/100 * (hiddenscore/40), 2)
            enemywep = round(random.randint(40,50) * enemyatk, 2)
            enemyhp = math.ceil(random.randint(100,120) * (hiddenscore/25))
        else:
            print("\n==========================\nYou come across a " + random.choice(enemylist) + "!\n==========================")
            enemyatk = round(float(random.randrange(100,151))/100 * (hiddenscore/20), 2)
            enemyend = round(float(random.randrange(5,31))/75 * (hiddenscore/50), 2)
            enemywep = round(random.randint(40,50) * enemyatk, 2)
            enemyhp = math.ceil(random.randint(100,120) * (hiddenscore/15))
        #in case values are too low or too high, causing the game to be unplayable, this'll set them to a "fairer" value
        if enemyend > 1:
            enemyend = 0.90
        if enemyatk < 1:
            enemyatk = 1
        print("dmg: " + str(round((enemywep*enemyatk), 2)) + "\nend: " + str(round((enemyend%1), 1)*100) + "%")
        while True:
            print("-------------\nenemy hp: " + str(enemyhp))
            print("your hp: " + str(hp) + "/" + str(maxhp))
            time.sleep(2)
            #prompts to fight or run
            battlechoice = input(">Fight, >Run, or use an >Item? You can also check your >Stats beforehand. >").lower()
            if battlechoice == "stats":
                print("\n----------------\nscore: " + str(score) + "\n----------------\nhp: " + str(hp) + "\nmax hp: " + str(maxhp) + "\n----------------\natk: " + str(atk) + "\nend: " + str((end%1)*100) + "%\n----------------\ncurrent weapon: " + currentweapon["name"] + "\ncurrent weapon dmg: " + str(currentweapon["dmg"]) + "\ncurrent shield: " + currentshield["name"] + "\ncurrent shield end: " + str((currentshield["end"]%1)*100)  + "%\n----------------\nSLOT 1: " + inventory[1] + "\nSLOT 2: " + inventory[2] + "\nSLOT 3: " + inventory[3] + "\n----------------\n")
                battlechoice = input("Fight, Run, or use an Item? >")
            while battlechoice != "fight" and battlechoice != "run" and battlechoice != "item":
                battlechoice = input("(Pick one of the following options given.)\n>Fight, >Run, or use an >Item? >").lower()
            if battlechoice == "item":
                print("\nSLOT 1: " + inventory[1] + "\nSLOT 2: " + inventory[2] + "\nSLOT 3: " + inventory[3])
                itemchoice = int(input("\n\nType the slot the item you want to use is in (1,2,3)... >"))
                if inventory[itemchoice] == "":
                    print("NOTHING buffed. Empty slot chosen.")
                else:
                    catcount = 0
                    while catcount <= 2:
                        if catcount == 0:
                            for potion in items["atk"]:
                                if potion == inventory[itemchoice]:
                                    if characterchoice == "outsider":
                                        atk += 2(items.get("atk").get(potion))
                                        totalatkbuff += 2(items.get("atk").get(potion))
                                    else:
                                        atk += items.get("atk").get(potion)
                                        totalatkbuff += items.get("atk").get(potion)
                                    atkpotused = True
                                    inventory[itemchoice] = ""
                                    print("^^^^ ATTACK BUFFED ^^^^\nNEW ATK: " + str(atk) + "\n")
                        elif catcount == 1:
                            for potion in items["end"]:
                                if potion == inventory[itemchoice]:
                                    if end + (items.get("end").get(potion)) > 0.99:
                                        totalendbuff += end+items.get("end").get(potion)-0.99
                                        end = 0.99
                                        endpotused = True
                                        inventory[itemchoice] = ""
                                        print("^^^^ ENDURANCE BUFFED TO MAX! ^^^^\n")
                                    else:
                                        totalendbuff += items.get("end").get(potion)
                                        end += items.get("end").get(potion)
                                        endpotused = True
                                        inventory[itemchoice] = ""
                                        print("^^^^ ENDURANCE BUFFED ^^^^\nNEW END: " + str(end*100) + "%\n")
                        elif catcount == 2:
                            for potion in items["hp"]:
                                if potion == inventory[itemchoice]:
                                    hp *= (maxhp * (items.get("hp").get(potion)))
                                    if hp > maxhp:
                                        hp = maxhp
                                    inventory[itemchoice] = ""
                                    print("^^^^ HEALTH RESTORED ^^^^\nNEW HP: " + str(hp) + "/" + str(maxhp) + "\n")
                        catcount += 1
                battlechoice = input(">Fight or >Run? >").lower()
                while battlechoice != "fight" and battlechoice != "run":
                    battlechoice = input("(Pick one of the following options given.)\n>Fight, or >Run? >").lower()
            #if run is picked
            if battlechoice == "run":
                print("\n>>>>>>>>>>>\nYou try to run, and...")
                time.sleep(1)
                if character == "mercenary":
                    if random.randint(1,100) >= 35:
                        print("You ran away swiftly.\n>>>>>>>>>>>\n")
                        return "ran"
                    else:
                        print("Failed.\n>>>>>>>>>>>\n")
                else:
                    if random.randint(1,100) >= 60:
                        print("You ran away.\n>>>>>>>>>>>\n")
                        return "ran"
                    else:
                        print("Failed.\n>>>>>>>>>>>\n")
                time.sleep(0.75)
            #if fight is picked
            elif battlechoice == "fight":
                criticalcheck = random.randint(1, 100)
                if criticalcheck >= 90:
                    critfactor = 2
                    crit = True
                else:
                    critfactor = 1
                    crit = False
                #calculates user attack damage
                currentattackdmg = round(currentweapon["dmg"]*atk, 2)
                finalatk = round(((currentattackdmg*(1-enemyend))*(random.randrange(8, 13)/10))*critfactor, 2)
                enemyhp = round(enemyhp - finalatk, 2)
                #if user wins:
                if enemyhp <= 0:
                    print("-------------")
                    if crit == True:
                        print("\n***CRITICAL HIT!***")
                        time.sleep(0.3)
                        print("\n\n          * *\n")
                        time.sleep(0.25)
                        print("\n          *-*\n         *   *\n          *-*\n")
                        time.sleep(0.25)
                        print("\\         *-*         /\n --------*   *--------\n/         *-*         \\")
                        time.sleep(0.25)
                        print("\n\\                     /\n\n/                     \\")
                        time.sleep(0.25)
                        print("\n\n\n")
                        print(">YOU ATTACK WITH *" + str(finalatk) + "* POWER!<\nEnemy hp left: " + str(round(enemyhp, 2)))
                    else:
                        print("\n>YOU ATTACK WITH " + str(finalatk) + " POWER!<\nEnemy hp left: " + str(round(enemyhp, 2)))
                    time.sleep(1)
                    print("\n-------------\nVICTORY!")
                    time.sleep(1.5)
                    lastevent = "fight"
                    if endpotused == True:
                        print(totalendbuff)
                        end -= totalendbuff
                    if atkpotused == True:
                        atk -= totalatkbuff
                    return "won"
                #otherwise:
                else:
                    print("-------------")
                    if crit == True:
                        print("\n***CRITICAL HIT!***")
                        time.sleep(0.3)
                        print("\n\n          * *\n")
                        time.sleep(0.25)
                        print("\n          *-*\n         *   *\n          *-*\n")
                        time.sleep(0.25)
                        print("\\         *-*         /\n --------*   *--------\n/         *-*         \\")
                        time.sleep(0.25)
                        print("\n\\                     /\n\n/                     \\")
                        time.sleep(0.25)
                        print("\n\n\n")
                        print("\n>YOU ATTACK WITH *" + str(finalatk) + "* POWER!<\nEnemy hp left: " + str(round(enemyhp, 2)))
                    else:
                        print("\n-------------\n>YOU ATTACK WITH " + str(finalatk) + " POWER!<\nEnemy hp left: " + str(round(enemyhp, 2)))
                    time.sleep(1.5)
                    
            #enemy attacks
            enemycurrentattackdmg = enemywep*enemyatk
            combinedend = end+currentshield["end"]
            #checks if combined endurance is over 1 (essentially making you invincible then)
            if combinedend > 0.99:
                combinedend = 0.99
            #calculates enemy attack damage
            finalenemyatk = round((enemycurrentattackdmg*(1-combinedend))*(random.randint(8, 12)/10), 2)
            if characterchoice != "knight" and characterchoice != "mercenary" and characterchoice != "outsider":
                if (random.randint(1,100) <= 15):
                    miss = True
                    finalenemyatk = 0
            if characterchoice == "knight" and enemywep > currentweapon["dmg"]:
                if random.randint(1,100) <= 30:
                    parry = True
                    finalenemyatk = 0
            else:
                parry = False
            hp = round(hp-finalenemyatk, 2)
            #if user is a loser:
            if hp <= 0:
                print(">YOU'RE HIT WITH " + str(finalenemyatk) + " POWER!<\nYour hp left: " + str(hp))
                time.sleep(1.5)
                print("Game over.")
                return "lost"
            #otherwise:
            else:
                if miss == True:
                    print(">>>ENEMY ATTACK EVADED>>>\n-------------\n")
                elif parry == True:
                    print("/*\\PARRY/*\\\n-------------\n")
                else:
                    print(">YOU'RE HIT WITH " + str(finalenemyatk) + " POWER!<\nYour hp left: " + str(hp) + "\n-------------\n")
                time.sleep(1.5)



    '''           FROM HERE ON OUT,
                        GAME
                       BEGINS
                        !!!!        
    '''

    if continuequestion == "n":
        break
    #explains game
    print("""\nHere's the run-down:\n
vvv STATS vvv
HP: If this number gets to 0, game over!
ATK: Attack, augments weapon damage
END: Endurance, helps negate enemy damage\n\n
vvv WEAPON/SHIELD vvv
WEAPON: What HURTS your enemy! Augmented by your ATK stat
SHIELD: Its endurance is added to your endurance stat directly (endurance caps at 99%)\n\n
vvv ITEMS vvv
You might find them after a battle, and you get to use 1 per turn before attacking (or running)\n\n
vvv GOAL vvv
Reach the BOTTOM of the DUNGEON!!
==================================================================================================       
Enemies will get stronger the further you go. Every 3 battles you win your HP is fully restored.
Good luck!\n""")
    
    #check if user understands, if not check if user understands, if not...
    understood = input("Understood? (y/n) >")
    while understood != "y":
        understood = input("UNDERSTOOD?? (y/n) >")
    print("\n-------------------Choose a character!-------------------\n")
    time.sleep(1)
    print("Knight: " + storydict['knight']['story'], "\n----------------\n",
    "ATK", storydict['knight']['atk'], "\n",
    "END", storydict['knight']['end']*100, "%\n---------------\n",
    "Weapon:", storydict['knight']['weapon']['name'], "\n",
    "Weapon damage:", storydict['knight']['weapon']['dmg'], "\n---------------\n",
    "Shield:", storydict['knight']['shield']['name'], "\n",
    "Shield endurance:", storydict['knight']['shield']['end']*100, "%\n",
    "Starts with a medium HP potion\n\n"
    "CLASS PERK: When an enemy has more attack than your weapon, 30% chance to PARRY an attack\n\n")
    time.sleep(1.5)
    print(
    "Outsider: " + storydict['outsider']['story'], "\n----------------\n",
    "ATK", storydict['outsider']['atk'], "\n",
    "END", storydict['outsider']['end']*100, "%\n---------------\n",
    "Weapon:", storydict['outsider']['weapon']['name'], "\n",
    "Weapon damage:", storydict['outsider']['weapon']['dmg'], "\n---------------\n",
    "Shield:", storydict['outsider']['shield']['name'], "\n",
    "Shield endurance:", storydict['outsider']['shield']['end']*100, "%\n", 
    "Starts with a small attack potion\n\n"
    "CLASS PERK: Any ATK increases after battle are doubled, and ATK potions have a higher impact\n\n")
    time.sleep(1.5)
    print(
    "Mercenary: " + storydict['mercenary']['story'], "\n----------------\n",
    "ATK", storydict['mercenary']['atk'], "\n",
    "END", storydict['mercenary']['end']*100, "%\n---------------\n",
    "Weapon:", storydict['mercenary']['weapon']['name'], "\n",
    "Weapon damage:", storydict['mercenary']['weapon']['dmg'], "\n---------------\n",
    "Shield:", storydict['mercenary']['shield']['name'], "\n",
    "Shield endurance:", storydict['mercenary']['shield']['end']*100, "%\n"
    "Starts with a medium attack potion\n\n"
    "CLASS PERK: Higher chance to run away\n\n")
    time.sleep(1.5)
    #pick character
    characterchoice = input(">Knight, >Outsider, or >Mercenary? \n(psst, try >None)\n>").lower()

    if characterchoice == "mercenary":
        character = "mercenary"
        atk = storydict['mercenary']['atk']
        end = storydict['mercenary']['end']
        currentweapon["name"] = storydict['mercenary']['weapon']['name']
        currentweapon["dmg"] = storydict['mercenary']['weapon']['dmg']
        currentshield["name"] = storydict['mercenary']['shield']['name']
        currentshield["end"] = storydict['mercenary']['shield']['end']
        inventory = storydict["mercenary"]["inventory"]
    elif characterchoice == "outsider":
        character = "outsider"
        atk = storydict['outsider']['atk']
        end = storydict['outsider']['end']
        currentweapon["name"] = storydict['outsider']['weapon']['name']
        currentweapon["dmg"] = storydict['outsider']['weapon']['dmg']
        currentshield["name"] = storydict['outsider']['shield']['name']
        currentshield["end"] = storydict['outsider']['shield']['end']
        inventory = storydict["outsider"]["inventory"]
    elif characterchoice == "knight":
        character = "knight"
        atk = storydict['knight']['atk']
        end = storydict['knight']['end']
        currentweapon["name"] = storydict['knight']['weapon']['name']
        currentweapon["dmg"] = storydict['knight']['weapon']['dmg']
        currentshield["name"] = storydict['knight']['shield']['name']
        currentshield["end"] = storydict['knight']['shield']['end']
        inventory = storydict["knight"]["inventory"]
    else:
        print("\nUNKNOWN\'S GIFT!\nAll enemy attacks now have a 15% chance to miss, AND you run away from fights successfully more often!\nThis is the INTENDED way to play!")
        time.sleep(2)

    while True:
        #victory check
        if score>60 and winchoice != "continue":
            print("YOU WIN! To achieve this you must've gotten extremely lucky, so congratulations.")
            winchoice = input("\ntype anything to end, or \"continue\" to keep going until you die... >")
            if winchoice == "continue":
                pass
            else:
                break
        roll = input("\nType anything to continue, or \"stats\" to view your current stats... >")
        if roll == "stats":
            print("\n----------------\nscore: " + str(score) + "\n----------------\nhp: " + str(hp) + "\nmax hp: " + str(maxhp) + "\n----------------\natk: " + str(atk) + "\nend: " + str((end%1)*100) + "%\n----------------\ncurrent weapon: " + currentweapon["name"] + "\ncurrent weapon dmg: " + str(currentweapon["dmg"]) + "\ncurrent shield: " + currentshield["name"] + "\ncurrent shield end: " + str((currentshield["end"]%1)*100)  + "%\n----------------\nSLOT 1: " + inventory[1] + "\nSLOT 2: " + inventory[2] + "\nSLOT 3: " + inventory[3] + "\n----------------\n")
            input("\nType anything to continue... >")
        #random num generator that will decide enemy/event
        eventoddroll = random.randint(1, 100)
        #if enemy:
        if eventoddroll > 50:
            enemyresult = enemyroll()
            #will trigger if enemy counter is lost, and ask if player wants to continue or not.
            if enemyresult == "lost":
                print("\n:( :( :( :( :( :( :( :(\nfinal score: " + str(score) + "\n:( :( :( :( :( :( :( :(\n")
                continuequestion = input("try again? (y/n) >")
                while continuequestion != "y" and continuequestion != "n":
                    continuequestion = input("do you want to TRY AGAIN?? (y/n) >")
                break
            elif enemyresult == "ran":
                #add to hidden score if player ran away, so enemies still get harder
                hiddenscore += 1
                lastevent = "fight"
            elif enemyresult == "won":
                healcounter += 1
                score += 5
                hiddenscore += 5
                statimprove = random.choice(statlist)
                #improve random stat
                if statimprove == "atk":
                    if characterchoice == "outsider":
                        atk += (round(min(round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2)), 2))*2
                    else:
                        atk += round(min(round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2)), 2)
                    atk = round(atk, 2)
                    print("\n**************************\natk improved. new atk:", str(round(atk, 2)), "\n**************************\n-------------\n")
                elif statimprove == "end":
                    end += round(min(round(random.uniform(0.02, 0.15), 2), round(random.uniform(0.02, 0.15), 2)), 2)
                    end = round(end, 2)
                    print("\n**************************\nend improved. new end:", str((round(end, 2))*100), "%\n**************************\n-------------\n")
                elif statimprove == "hp":
                    hpgain = min(random.randint(20,60), random.randint(20,60))
                    maxhp = maxhp + hpgain
                    hp = hp + hpgain
                    print("\n**************************\nhp improved. new max hp:", str(maxhp), "\n**************************\n-------------\n")
                time.sleep(1)
                #might find random item here
                if random.randint(1,100) > 65:
                    invnum = 1
                    while invnum <= 3:
                        if inventory.get(invnum) == "":
                            strtemp = random.choice(["end", "atk", "hp"])
                            if strtemp == "atk":
                                inventory[invnum] = random.choice(list(items["atk"]))
                            elif strtemp == "end":
                                inventory[invnum] = random.choice(list(items["end"]))
                            else:
                                inventory[invnum] = random.choice(list(items["hp"]))
                            print("+++  YOU FOUND A", inventory.get(invnum).upper(), "! +++")
                            time.sleep(1)
                            break
                        else:
                            invnum += 1
                #heal user to full hp every 3 fights won
                if healcounter%3 == 0:
                    print("HP RESTORED TO MAX!")
                    hp = maxhp
        #if event:
        else:
            #this will check if the last roll resulted in an event. if it did, run enemy encounter. if it didn't, run event.
            #this prevents getting 2 events in a row
            if lastevent != "event":
                evnt2roll()
                lastevent = "event"
            else:
                enemyresult = enemyroll()
                if enemyresult == "lost":
                    print("\n:( :( :( :( :( :( :( :(\nfinal score: " + str(score) + "\n:( :( :( :( :( :( :( :(\n")
                    continuequestion = input("try again? (y/n) >")
                    while continuequestion != "y" and continuequestion != "n":
                        continuequestion = input("do you want to TRY AGAIN?? (y/n) >")
                    break
                elif enemyresult == "ran":
                    hiddenscore += 5
                    lastevent = "fight"
                elif enemyresult == "won":
                    healcounter += 1
                    score += 5
                    hiddenscore += 5
                    statimprove = random.choice(statlist)
                    if statimprove == "atk":
                        atk += round(min(round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2), round(random.uniform(0.05, 0.90), 2)), 2)
                        atk = round(atk, 2)
                        print("\n**************************\natk improved. new atk:", str(round(atk, 2)), "\n**************************\n-------------\n")
                    elif statimprove == "end":
                        end += round(min(round(random.uniform(0.02, 0.15), 2), round(random.uniform(0.02, 0.15), 2)), 2)
                        end = round(end, 2)
                        print("\n**************************\nend improved. new end:", str((round(end, 2))*100), "%\n**************************\n-------------\n")
                    elif statimprove == "hp":
                        hpgain = min(random.randint(20,60), random.randint(20,60))
                        maxhp = maxhp + hpgain
                        hp = hp + hpgain
                        print("\n**************************\nhp improved. new max hp:", str(maxhp), "\n**************************\n-------------\n")
                    if healcounter%3 == 0:
                        print("HP RESTORED TO MAX!")
                        hp = maxhp