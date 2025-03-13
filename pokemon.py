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

           "lapras":
           {"type":{"type1":"water", "type2":"ice"}},

           "vaporeon":
           {"type":{"type1":"water", "type2":"none"}},
           
           "jolteon":
           {"type":{"type1":"electric", "type2":"none"}},

           "flareon":
           {"type":{"type1":"fire", "type2":"none"}},

           "porygon":
           {"type":{"type1":"normal", "type2":"none"}},

           "omastar":
           {"type":{"type1":"water", "type2":"rock"}},

           "kabutops":
           {"type":{"type1":"water", "type2":"rock"}},


           "aerodactyl":
           {"type":{"type1":"rock", "type2":"flying"}},

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
           {"type":{"type1":"psychic", "type2":"none"}},
           
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
nature_drop_atk = 1
nature_drop_def = 1
nature_drop_spa = 1
nature_drop_spd = 1
nature_drop_spe = 1


print(active)


if active == pokemon_keys[0]:
    active_hp = 80
    active_atk = 82
    active_def = 83
    active_spa = 100
    active_spd = 100
    active_spe =80
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
    active_nature = "modest"

if active == pokemon_keys[1]:
    active_hp = 78
    active_atk = 84
    active_def = 78
    active_spa = 109
    active_spd = 85
    active_spe = 100
    active_type1 = "fire"
    active_type2 = "flying"
    active_move1 = "blast burn"
    active_move2 = "heat wave"
    active_move3 = "air slash"
    active_move4 = "scorching sands "
    active_hp_evs = 4
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 252
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "modest"

if active == pokemon_keys[2]:
    active_hp = 79
    active_atk = 83
    active_def = 100
    active_spa = 85
    active_spd = 105
    active_spe =78
    active_type1 = "water"
    active_type2 = "none"
    active_move1 = "water pledge"
    active_move2 = "shell smash"
    active_move3 = "flash cannon"
    active_move4 = "water spout"
    active_hp_evs = 4
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 252
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "modest"

if active == pokemon_keys[3]:
    active_hp = 60
    active_atk = 45
    active_def = 50
    active_spa = 90
    active_spd = 80
    active_spe = 70
    active_type1 = "bug"
    active_type2 = "flying"
    active_move1 = "substitute"
    active_move2 = "bug buzz"
    active_move3 = "quiver dance"
    active_move4 = "sleep powder"
    active_hp_evs = 252
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "timid"

if active == pokemon_keys[4]:
    active_hp = 65
    active_atk = 90
    active_def = 40
    active_spa = 45
    active_spd = 80
    active_spe = 75
    active_type1 = "bug"
    active_type2 = "poison"
    active_move1 = "Knock off"
    active_move2 = "poison jab"
    active_move3 = "drill run"
    active_move4 = "u-turn"
    active_hp_evs = 0
    active_atk_evs = 252
    active_def_evs = 0
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "jolly"

if active == pokemon_keys[5]:
    active_hp = 83
    active_atk = 80
    active_def = 75
    active_spa = 70
    active_spd = 70
    active_spe = 101
    active_type1 = "normal"
    active_type2 = "flying"
    active_move1 = "u-turn"
    active_move2 = "roost"
    active_move3 = "brave bird"
    active_move4 = "return"
    active_hp_evs = 0
    active_atk_evs = 252
    active_def_evs = 0
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "jolly"

if active == pokemon_keys[6]:
    active_hp = 55
    active_atk = 81
    active_def = 60
    active_spa = 50
    active_spd = 70
    active_spe = 97
    active_type1 = "normal"
    active_type2 = "none"
    active_move1 = "facade"
    active_move2 = "sucker punch"
    active_move3 = "u-turn"
    active_move4 = "crunch"
    active_hp_evs = 0
    active_atk_evs = 252
    active_def_evs = 0
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "jolly"

if active == pokemon_keys[7]:
    active_hp = 90
    active_atk = 92
    active_def = 87
    active_spa = 75
    active_spd = 85
    active_spe = 76
    active_type1 = "poison"
    active_type2 = "ground"
    active_move1 = "stealth rock"
    active_move2 = "earth power"
    active_move3 = "sludge wave"
    active_move4 = "toxic"
    active_hp_evs = 0
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 252
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "timid"

if active == pokemon_keys[8]:
    active_hp = 81
    active_atk = 102
    active_def = 77
    active_spa = 85
    active_spd = 75
    active_spe = 85
    active_type1 = "poison"
    active_type2 = "ground"
    active_move1 = "sludge wave"
    active_move2 = "earth power"
    active_move3 = "ice beam"
    active_move4 = "substitute"
    active_hp_evs = 0
    active_atk_evs = 0
    active_def_evs = 4
    active_spa_evs = 252
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "timid"

if active == pokemon_keys[9]:
    active_hp = 95
    active_atk = 70
    active_def = 73
    active_spa = 95
    active_spd = 90
    active_spe = 60
    active_type1 = "fairy"
    active_type2 = "none"
    active_move1 = "monnblast"
    active_move2 = "recover"
    active_move3 = "protect"
    active_move4 = "flamethrower"
    active_hp_evs = 252
    active_atk_evs = 0
    active_def_evs = 236
    active_spa_evs = 4
    active_spd_evs = 4
    active_spe_evs = 12
    active_nature = "bold"

if active == pokemon_keys[10]:
    active_hp = 130
    active_atk = 85
    active_def = 80
    active_spa = 85
    active_spd = 95
    active_spe = 60
    active_type1 = "water"
    active_type2 = "ice"
    active_move1 = "scald"
    active_move2 = "freeze dry"
    active_move3 = "protect"
    active_move4 = "perish song"
    active_hp_evs = 252
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 4
    active_spd_evs = 252
    active_spe_evs = 0
    active_nature = "calm"

if active == pokemon_keys[11]:
    active_hp = 130
    active_atk = 65
    active_def = 60
    active_spa = 110
    active_spd = 95
    active_spe = 65
    active_type1 = "water"
    active_type2 = "none"
    active_move1 = "scald"
    active_move2 = "haze"
    active_move3 = "wish"
    active_move4 = "protect"
    active_hp_evs = 252
    active_atk_evs = 0
    active_def_evs = 252
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 0
    active_nature = "bold"

if active == pokemon_keys[12]:
    active_hp = 65
    active_atk = 65
    active_def = 60
    active_spa = 110
    active_spd = 95
    active_spe = 130
    active_type1 = "electric"
    active_type2 = "none"
    active_move1 = "calm mind"
    active_move2 = "thunderbolt"
    active_move3 = "volt switch"
    active_move4 = "alluring voice"
    active_hp_evs = 0
    active_atk_evs = 0
    active_def_evs = 4
    active_spa_evs = 252
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "timid"

if active == pokemon_keys[13]:
    active_hp = 65
    active_atk = 130
    active_def = 60
    active_spa = 95
    active_spd = 110
    active_spe = 65
    active_type1 = "fire"
    active_type2 = "none"
    active_move1 = "flar blitz"
    active_move2 = "facade"
    active_move3 = "protect"
    active_move4 = "copycat"
    active_hp_evs = 252
    active_atk_evs = 252
    active_def_evs = 4
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 0
    active_nature = "adamant"

if active == pokemon_keys[14]:
    active_hp = 65
    active_atk = 60
    active_def = 105
    active_spa = 85
    active_spd = 112.5
    active_spe = 40
    active_type1 = "normal"
    active_type2 = "none"
    active_move1 = "double edge"
    active_move2 = "ice beam"
    active_move3 = "recover"
    active_move4 = "agility"
    active_hp_evs = 252
    active_atk_evs = 128
    active_def_evs = 124
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 0
    active_nature = "brave"

if active == pokemon_keys[15]:
    active_hp = 70
    active_atk = 60
    active_def = 125
    active_spa = 115
    active_spd = 70
    active_spe = 55
    active_type1 = "water"
    active_type2 = "rock"
    active_move1 = "shell smash"
    active_move2 = "hydro pump"
    active_move3 = "endure"
    active_move4 = "power gem"
    active_hp_evs = 0
    active_atk_evs = 0
    active_def_evs = 4
    active_spa_evs = 252
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "timid"

if active == pokemon_keys[16]:
    active_hp = 60
    active_atk = 115
    active_def = 105
    active_spa = 65
    active_spd = 70
    active_spe = 80
    active_type1 = "water"
    active_type2 = "rock"
    active_move1 = "rapid spin"
    active_move2 = "knock off"
    active_move3 = "stone edge"
    active_move4 = "liquidation"
    active_hp_evs = 0
    active_atk_evs = 252
    active_def_evs = 4
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "adamant"

if active == pokemon_keys[17]:
    active_hp = 80
    active_atk = 105
    active_def = 65
    active_spa = 60
    active_spd = 75
    active_spe = 130
    active_type1 = "rock"
    active_type2 = "flying"
    active_move1 = "roost"
    active_move2 = "stealth rock"
    active_move3 = "stone edge"
    active_move4 = "earthquake"
    active_hp_evs = 0
    active_atk_evs = 252
    active_def_evs = 4
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 252
    active_nature = "adamant"

if active == pokemon_keys[18]:
    active_hp = 160
    active_atk = 110
    active_def = 65
    active_spa = 65
    active_spd = 110
    active_spe = 30
    active_type1 = "normal"
    active_type2 = "none"
    active_move1 = "yawn"
    active_move2 = "protect"
    active_move3 = "earthquake"
    active_move4 = "body slam"
    active_hp_evs = 140
    active_atk_evs = 116
    active_def_evs = 252
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 0
    active_nature = "adamant"

if active == pokemon_keys[19]:
    active_hp = 90
    active_atk = 85
    active_def = 100
    active_spa = 95
    active_spd = 125
    active_spe = 85
    active_type1 = "ice"
    active_type2 = "flying"
    active_move1 = "freeze dry"
    active_move2 = "roost"
    active_move3 = "substitute"
    active_move4 = "haze"
    active_hp_evs = 248
    active_atk_evs = 208
    active_def_evs = 0
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 52
    active_nature = "calm"

if active == pokemon_keys[20]:
    active_hp = 90
    active_atk = 90
    active_def = 85
    active_spa = 125
    active_spd = 90
    active_spe = 100
    active_type1 = "electric"
    active_type2 = "flying"
    active_move1 = "hurricane"
    active_move2 = "volt switch"
    active_move3 = "thunder wave"
    active_move4 = "roost"
    active_hp_evs = 248
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 244
    active_spd_evs = 0
    active_spe_evs = 16
    active_nature = "timid"

if active == pokemon_keys[21]:
    active_hp = 90
    active_atk = 100
    active_def = 90
    active_spa = 125
    active_spd = 85
    active_spe = 90
    active_type1 = "fire"
    active_type2 = "flying"
    active_move1 = "flamethrower"
    active_move2 = "will-o-wisp"
    active_move3 = "air slash"
    active_move4 = "roost"
    active_hp_evs = 248
    active_atk_evs = 0
    active_def_evs = 248
    active_spa_evs = 0
    active_spd_evs = 0
    active_spe_evs = 12
    active_nature = "bold"

if active == pokemon_keys[22]:
    active_hp = 91
    active_atk = 134
    active_def = 95
    active_spa = 100
    active_spd = 100
    active_spe = 80
    active_type1 = "dragon"
    active_type2 = "flying"
    active_move1 = "outrage "
    active_move2 = "extreme speed"
    active_move3 = "stomping tantrum"
    active_move4 = "aerial ace"
    active_hp_evs = 244
    active_atk_evs = 252
    active_def_evs = 4
    active_spa_evs = 0
    active_spd_evs = 4
    active_spe_evs = 4
    active_nature = "adamant"

if active == pokemon_keys[23]:
    active_hp = 106
    active_atk = 110
    active_def = 90
    active_spa = 154
    active_spd = 90
    active_spe = 130
    active_type1 = "psychic"
    active_type2 = "none"
    active_move1 = "nasty plot"
    active_move2 = "psystrike"
    active_move3 = "thunderbolt"
    active_move4 = "ice beam"
    active_hp_evs = 0
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 252
    active_spd_evs = 4
    active_spe_evs = 252
    active_nature = "timid"




if active_nature == "adamant":
    nature_boost_atk = 1.10
    nature_drop_spa = 0.90

if active_nature == "brave":
    nature_boost_atk = 1.10
    nature_drop_spe = 0.90

if active_nature == "bold":
    nature_boost_def = 1.10
    nature_drop_atk = 0.90

if active_nature == "modest":
    nature_boost_spa = 1.10
    nature_drop_atk = 0.90

if active_nature == "calm":
    nature_boost_spd = 1.10
    nature_drop_atk = 0.90

if active_nature == "jolly":
    nature_boost_spe = 1.10
    nature_drop_spa = 0.90

if active_nature == "timid":
    nature_boost_spe = 1.10
    nature_drop_atk = 0.90



#Hp calculator
if active_hp_evs != 256:
    print("hp is, ", (math.floor(((2*active_hp+31+(active_hp_evs/4))*50)/100)+50+10))
else:
    print("parker likes dudes")

#stat calculators
if active_atk_evs != 256:
    print("atk is,", math.floor(math.floor((math.floor(((2*active_atk+31+math.floor(active_atk_evs/4))*50)/100)+5)*nature_boost_atk)*nature_drop_atk) )
else:
    print("parker likes dudes")

if active_spa_evs != 256:
    print("spak is,", math.floor((math.floor(((2*active_spa+31+math.floor(active_spa_evs/4))*50)/100)+5)*nature_boost_spa) )
else:
    print("parker likes dudes")

if active_def_evs != 256:
    print("def is,", math.floor((math.floor(((2*active_def+31+math.floor(active_def_evs/4))*50)/100)+5)*nature_boost_def) )
else:
    print("parker likes dudes")

if active_spd_evs != 256:
    print("spdef is,", math.floor((math.floor(((2*active_spd+31+math.floor(active_spd_evs/4))*50)/100)+5)*nature_boost_spd) )
else:
    print("parker likes dudes")

if active_spe_evs != 256:
    print("speed is,", math.floor((math.floor(((2*active_spe+31+math.floor(active_spe_evs/4))*50)/100)+5)*nature_boost_spe) )
else:
    print("parker likes dudes")

print(active)
print(active_type1)
print(active_type2)
print(active_move1)
print(active_move2)
print(active_move3)
print(active_move4)


#print the list of the keys
print(pokemon_keys)
#print certain key
print(pokemon_keys[5])
#print certain key value
print(pokemon[pokemon_keys[5]])