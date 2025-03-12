# pokemon dictionary, all info for pokemon which will be called later will be here
# dictionaries come in the format: x = {key:value, key2:value2}, you call dictionaries
# by going like x[key], and then it'll retrieve the value of the key
# keys can have identical values but values cannot have identical keys
# vvv you can also nest them like so vvv
import random
import math
pokemon = {"venusaur":
           
           {"type":{"type1":"grass", "type2":"poison"}},

           "charizard":
           {"type":{"type1":"flying", "type2":"fire"}},

           "blastoise":
           {"type":{"type1":"water", "type2":"none"}},

           "butterfree":
           {"type":{"type1":"bug", "type2":"flying"}},

           "beedrill":
           {"type":{"type1":"bug", "type2":"poison"}},

           "pigeot":
           {"type":{"type1":"normal", "type2":"flying"}},

           "raticate":
           {"type":{"type1":"normal", "type2":"none"}},

           "nidoqueen":
           {"type":{"type1":"ground", "type2":"poison"}}, 

           "nidoking":
           {"type":{"type1":"ground", "type2":"poison"}},  

           "clefable":
           {"type":{"type1":"fairy", "type2":"none"}},

           "ditto":
           {"type":{"type1":"normal", "type2":"none"}},

           "jolteon":
           {"type":{"type1":"electric", "type2":"none"}},

           "flareon":
           {"type":{"type1":"fire", "type2":"none"}},

           "porygon":
           {"type":{"type1":"normal", "type2":"none"}},

           "snorlax":
           {"type":{"type1":"normal", "type2":"none"}},

           "articuno":
           {"type":{"type1":"ice", "type2":"flying"}},

           "zapdos":
           {"type":{"type1":"electric", "type2":"flying"}},

           "moltres":
           {"type":{"type1":"fire", "type2":"flying"}},

           "dragonite":
           {"type":{"type1":"dragon", "type2":"flying"}},

           "mewtwo":
           {"type":{"type1":"psychic", "type2":"none"}}
           
           }
#this is the list team assign randomizer as well as all the base stats set to the active slot(stats that will change when active changes)
pokemon_keys = list(pokemon.keys())

t1mon1 = random.choice(pokemon_keys)

t1mon2 = random.choice(pokemon_keys)

t1mon3 = random.choice(pokemon_keys)

t1mon4 = random.choice(pokemon_keys)

t1mon5 = random.choice(pokemon_keys)

t1mon6 = random.choice(pokemon_keys)

active = str(t1mon1)
#base stats
active_hp = 0
active_atk = 0
active_def = 0
active_spa = 0
active_spd = 0
active_spe = 0
#type
active_type1 = "none"
active_type2 = "none"
#moves
active_move1 = "none"
active_move2 = "none"
active_move3 = "none"
active_move4 = "none"
#ev's
active_hp_evs = 0
active_atk_evs = 0
active_def_evs = 0
active_spa_evs = 0
active_spd_evs = 0
active_spe_evs = 0
#natures
natures = ["adamant", "modest", "timid", "jolly", "bold", "calm", "brave", "serious"]
active_nature = natures[7]
nature_boost_atk = 1
nature_boost_def = 1
nature_boost_spa = 1
nature_boost_spd = 1
nature_boost_spe = 1

print(active)
pokemon_keys = list(pokemon.keys())
active = pokemon_keys[1]
if active == pokemon_keys[1]:
    active_hp = 80
    active_atk = 82
    active_def = 83
    active_spa = 100
    active_spde = 100
    active_sped =80
    active_type1 = "grass"
    active_type2 = "poison"
    active_move1 = "sludge bomb"
    active_move2 = "leaf storm"
    active_move3 = "poison powder"
    active_move4 = "protect"
    active_hp_evs = 4
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 252
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = natures[1]


if active_nature == natures[0] or natures[6]:
    nature_boost_atk = 1.10
elif active_nature == natures[4]:
    nature_boost_def = 1.10
elif active_nature == natures[1]:
    nature_boost_spa = 1.10
elif active_nature == natures[5]:
    nature_boost_spd = 1.10
elif active_nature == natures[2] or natures[3]:
    nature_boost_spe = 1.10




#Hp calculator
if active_hp_evs != 0:
    print("hp is, ", (math.floor(((2*active_hp+31+(active_hp_evs/4))*50)/100)+50+10))
else:
    print("parker likes dudes")
if active_atk_evs != 0:
    print("atk is,", ((((2*active_atk+31+(active_atk_evs/4)*50)/100)+5)*nature_boost_atk))
else:
    print("parker likes dudes")

if active_spa_evs != 0:
    print("spak is,", math.floor((((2*active_spa+31+(active_spa_evs/4))*50)/100)+5)*nature_boost_spa))
else:
    print("parker likes dudes")
#print the list of the keys
print(pokemon_keys)
#print certain key
print(pokemon_keys[5])
#print certain key value
print(pokemon[pokemon_keys[5]])