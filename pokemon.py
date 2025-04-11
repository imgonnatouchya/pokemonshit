# pokemon dictionary, all info for pokemon which will be called later will be here
# dictionaries come in the format: x = {key:value, key2:value2}, you call dictionaries
# by going like x[key], and then it'll retrieve the value of the key
# keys can have identical values but values cannot have identical keys
# vvv you can also nest them like so vvv
#Landon Mann
import random
import math
pokemon = {"venusaur":
           {"type":{"type1":"grass", "type2":"poison"},
           "hp":80,
           "atk":82,
           "def":83,
           "spa":100,
           "spd":100,
           "spe":80,
           "m1":"sludge bomb",
           "m2":"leaf storm",
           "m3":"poison powder",
           "m4":"protect",
           "hp_ev":4,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":252,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"modest"},

           "charizard":
           {"type":{"type1":"flying", "type2":"fire"},
           "hp":78,
           "atk":84,
           "def":78,
           "spa":109,
           "spd":85,
           "spe":100,
           "m1":"blast burn",
           "m2":"heat wave",
           "m3":"air slash",
           "m4":"scorching sands",
           "hp_ev":4,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":252,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"modest"},

           "blastoise":
           {"type":{"type1":"water", "type2":"none"},
           "hp":79,
           "atk":83,
           "def":100,
           "spa":85,
           "spd":105,
           "spe":78,
           "m1":"water pledge",
           "m2":"shell smash",
           "m3":"flash cannon",
           "m4":"water spout",
           "hp_ev":4,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":252,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"modest"},

           "butterfree":
           {"type":{"type1":"bug", "type2":"flying"},
           "hp":60,
           "atk":45,
           "def":50,
           "spa":90,
           "spd":80,
           "spe":70,
           "m1":"substitute",
           "m2":"bug buzz",
           "m3":"quiver dance",
           "m4":"sleep powder",
           "hp_ev":252,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"timid"},

           "beedrill":
           {"type":{"type1":"bug", "type2":"poison"},
           "hp":65,
           "atk":90,
           "def":40,
           "spa":45,
           "spd":80,
           "spe":75,
           "m1":"knock off",
           "m2":"poison jab",
           "m3":"drill run",
           "m4":"u-turn",
           "hp_ev":0,
           "atk_ev":252,
           "def_ev":0,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"jolly"},

           "pigeot":
           {"type":{"type1":"normal", "type2":"flying"},
           "hp":83,
           "atk":80,
           "def":75,
           "spa":70,
           "spd":70,
           "spe":101,
           "m1":"u-turn",
           "m2":"roost",
           "m3":"brave bird",
           "m4":"return",
           "hp_ev":0,
           "atk_ev":252,
           "def_ev":0,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"jolly"},

           "raticate":
           {"type":{"type1":"normal", "type2":"none"},
           "hp":55,
           "atk":81,
           "def":60,
           "spa":50,
           "spd":70,
           "spe":97,
           "m1":"facade",
           "m2":"sucker punch",
           "m3":"u-turn",
           "m4":"crunch",
           "hp_ev":0,
           "atk_ev":252,
           "def_ev":0,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"jolly"},

           "nidoqueen":
           {"type":{"type1":"ground", "type2":"poison"},
           "hp":90,
           "atk":92,
           "def":87,
           "spa":75,
           "spd":85,
           "spe":76,
           "m1":"stealth rock",
           "m2":"earth power",
           "m3":"sludge wave",
           "m4":"toxic",
           "hp_ev":0,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":252,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"timid"}, 

           "nidoking":
           {"type":{"type1":"ground", "type2":"poison"},
           "hp":91,
           "atk":102,
           "def":77,
           "spa":85,
           "spd":75,
           "spe":85,
           "m1":"sludge wave",
           "m2":"earth power",
           "m3":"ice beam",
           "m4":"substitute",
           "hp_ev":0,
           "atk_ev":0,
           "def_ev":4,
           "spa_ev":252,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"timid"},  

           "clefable":
           {"type":{"type1":"fairy", "type2":"none"},
           "hp":95,
           "atk":70,
           "def":73,
           "spa":95,
           "spd":90,
           "spe":69,
           "m1":"monnblast",
           "m2":"recover",
           "m3":"protect",
           "m4":"flamethrower",
           "hp_ev":252,
           "atk_ev":0,
           "def_ev":236,
           "spa_ev":4,
           "spd_ev":4,
           "spe_ev":12,
           "nature":"bold"},

           "lapras":
           {"type":{"type1":"water", "type2":"ice"},
           "hp":130,
           "atk":85,
           "def":80,
           "spa":85,
           "spd":95,
           "spe":60,
           "m1":"scald",
           "m2":"freeze dry",
           "m3":"protect",
           "m4":"perish song",
           "hp_ev":252,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":4,
           "spd_ev":252,
           "spe_ev":0,
           "nature":"calm"},

           "vaporeon":
           {"type":{"type1":"water", "type2":"none"},
           "hp":130,
           "atk":65,
           "def":60,
           "spa":110,
           "spd":95,
           "spe":65,
           "m1":"scald",
           "m2":"haze",
           "m3":"wish",
           "m4":"protect",
           "hp_ev":252,
           "atk_ev":0,
           "def_ev":252,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":0,
           "nature":"bold"},
           
           "jolteon":
           {"type":{"type1":"electric", "type2":"none"}},

           "flareon":
           {"type":{"type1":"fire", "type2":"none"},
           "hp":65,
           "atk":130,
           "def":60,
           "spa":95,
           "spd":110,
           "spe":65,
           "m1":"flar blitz",
           "m2":"facade",
           "m3":"protect",
           "m4":"copycat",
           "hp_ev":252,
           "atk_ev":252,
           "def_ev":4,
           "spa_ev":0,
           "spd_ev":0,
           "spe_ev":0,
           "nature":"adamant"},

           "porygon":
           {"type":{"type1":"normal", "type2":"none"}},

           "omastar":
           {"type":{"type1":"water", "type2":"rock"},
           "hp":70,
           "atk":60,
           "def":125,
           "spa":115,
           "spd":70,
           "spe":55,
           "m1":"shell smash",
           "m2":"hydro pump",
           "m3":"endure",
           "m4":"power gem",
           "hp_ev":0,
           "atk_ev":0,
           "def_ev":4,
           "spa_ev":252,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"timid"},

           "kabutops":
           {"type":{"type1":"water", "type2":"rock"}},


           "aerodactyl":
           {"type":{"type1":"rock", "type2":"flying"},
           "hp":80,
           "atk":105,
           "def":65,
           "spa":60,
           "spd":75,
           "spe":130,
           "m1":"roost",
           "m2":"stealth rock",
           "m3":"stone edge",
           "m4":"earthquake",
           "hp_ev":0,
           "atk_ev":252,
           "def_ev":4,
           "spa_ev":0,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"adamant"},

           "snorlax":
           {"type":{"type1":"normal", "type2":"none"}},

           "articuno":
           {"type":{"type1":"ice", "type2":"flying"},
           "hp":90,
           "atk":85,
           "def":100,
           "spa":95,
           "spd":125,
           "spe":85,
           "m1":"freeze dry",
           "m2":"roost",
           "m3":"roost",
           "m4":"haze",
           "hp_ev":248,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":208,
           "spd_ev":0,
           "spe_ev":52,
           "nature":"modest"},

           "zapdos":
           {"type":{"type1":"electric", "type2":"flying"},
           "hp":90,
           "atk":90,
           "def":85,
           "spa":125,
           "spd":90,
           "spe":100,
           "m1":"hurricane",
           "m2":"volt switch",
           "m3":"thunder wave",
           "m4":"roost",
           "hp_ev":248,
           "atk_ev":0,
           "def_ev":4,
           "spa_ev":244,
           "spd_ev":0,
           "spe_ev":16,
           "nature":"timid"},

           "moltres":
           {"type":{"type1":"fire", "type2":"flying"}, 
           "hp":90,
           "atk":100,
           "def":90,
           "spa":125,
           "spd":85,
           "spe":90,
           "m1":"flamethrower",
           "m2":"will-o-wisp",
           "m3":"air slash",
           "m4":"roost",
           "hp_ev":248,
           "atk_ev":0,
           "def_ev":248,
           "spa_ev":0,
           "spd_ev":0,
           "spe_ev":12,
           "nature":"bold"},

           "dragonite":
           {"type":{"type1":"dragon", "type2":"flying"},
           "hp":91,
           "atk":134,
           "def":95,
           "spa":100,
           "spd":100,
           "spe":80,
           "m1":"outrage",
           "m2":"stomping tantrum",
           "m3":"aerial ace",
           "m4":"extreme speed",
           "hp_ev":244,
           "atk_ev":252,
           "def_ev":4,
           "spa_ev":0,
           "spd_ev":4,
           "spe_ev":4,
           "nature":"adamant"},

           "mewtwo":
           {"type":{"type1":"psychic", "type2":"none"}},
           
           }
#this is the list team assign randomizer as well as all the base stats set to the active slot(stats that will change when active changes)
pokemon_keys = list(pokemon.keys())
#assign team 1
t1mon1 = random.choice(pokemon_keys)
t1mon2 = random.choice(pokemon_keys)
t1mon3 = random.choice(pokemon_keys)
t1mon4 = random.choice(pokemon_keys)
t1mon5 = random.choice(pokemon_keys)
t1mon6 = random.choice(pokemon_keys)
#assign team 2
t2mon1 = random.choice(pokemon_keys)
t2mon2 = random.choice(pokemon_keys)
t2mon3 = random.choice(pokemon_keys)
t2mon4 = random.choice(pokemon_keys)
t2mon5 = random.choice(pokemon_keys)
t2mon6 = random.choice(pokemon_keys)

active = str(t1mon1)
active2 = str(t2mon1)

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

#------STATS FOR TEAM 2------
#base stats
active2_hp = 0
active2_atk = 0
active2_def = 0
active2_spa = 0
active2_spd = 0
active2_spe = 0
#type
active2_type1 = "none"
active2_type2 = "none"
#moves
active2_move1 = "none"
active2_move2 = "none"
active2_move3 = "none"
active2_move4 = "none"
#ev's
active2_hp_evs = 0
active2_atk_evs = 0
active2_def_evs = 0
active2_spa_evs = 0
active2_spd_evs = 0
active2_spe_evs = 0

active2_nature = natures[7]
nature_boost_atk2 = 1
nature_boost_def2 = 1
nature_boost_spa2 = 1
nature_boost_spd2 = 1
nature_boost_spe2 = 1
nature_drop_atk2 = 1
nature_drop_def2 = 1
nature_drop_spa2 = 1
nature_drop_spd2 = 1
nature_drop_spe2 = 1



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
    active_move1 = "flare blitz"
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
    active_move1 = "tri attack"
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
    active_atk_evs = 0
    active_def_evs = 0
    active_spa_evs = 208
    active_spd_evs = 0
    active_spe_evs = 52
    active_nature = "modest"

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




#team 2
if active2 == pokemon_keys[0]:
    active2_hp = 80
    active2_atk = 82
    active2_def = 83
    active2_spa = 100
    active2_spd = 100
    active2_spe =80
    active2_type1 = "grass"
    active2_type2 = "poison"
    active2_move1 = "sludge bomb"
    active2_move2 = "leaf storm"
    active2_move3 = "poison powder"
    active2_move4 = "protect"
    active2_hp_evs = 4
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 252
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "modest"

if active2 == pokemon_keys[1]:
    active2_hp = 78
    active2_atk = 84
    active2_def = 78
    active2_spa = 109
    active2_spd = 85
    active2_spe = 100
    active2_type1 = "fire"
    active2_type2 = "flying"
    active2_move1 = "blast burn"
    active2_move2 = "heat wave"
    active2_move3 = "air slash"
    active2_move4 = "scorching sands "
    active2_hp_evs = 4
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 252
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "modest"

if active2 == pokemon_keys[2]:
    active2_hp = 79
    active2_atk = 83
    active2_def = 100
    active2_spa = 85
    active2_spd = 105
    active2_spe =78
    active2_type1 = "water"
    active2_type2 = "none"
    active2_move1 = "water pledge"
    active2_move2 = "shell smash"
    active2_move3 = "flash cannon"
    active2_move4 = "water spout"
    active2_hp_evs = 4
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 252
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "modest"

if active2 == pokemon_keys[3]:
    active2_hp = 60
    active2_atk = 45
    active2_def = 50
    active2_spa = 90
    active2_spd = 80
    active2_spe = 70
    active2_type1 = "bug"
    active2_type2 = "flying"
    active2_move1 = "substitute"
    active2_move2 = "bug buzz"
    active2_move3 = "quiver dance"
    active2_move4 = "sleep powder"
    active2_hp_evs = 252
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "timid"

if active2 == pokemon_keys[4]:
    active2_hp = 65
    active2_atk = 90
    active2_def = 40
    active2_spa = 45
    active2_spd = 80
    active2_spe = 75
    active2_type1 = "bug"
    active2_type2 = "poison"
    active2_move1 = "Knock off"
    active2_move2 = "poison jab"
    active2_move3 = "drill run"
    active2_move4 = "u-turn"
    active2_hp_evs = 0
    active2_atk_evs = 252
    active2_def_evs = 0
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "jolly"

if active2 == pokemon_keys[5]:
    active2_hp = 83
    active2_atk = 80
    active2_def = 75
    active2_spa = 70
    active2_spd = 70
    active2_spe = 101
    active2_type1 = "normal"
    active2_type2 = "flying"
    active2_move1 = "u-turn"
    active2_move2 = "roost"
    active2_move3 = "brave bird"
    active2_move4 = "return"
    active2_hp_evs = 0
    active2_atk_evs = 252
    active2_def_evs = 0
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "jolly"

if active2 == pokemon_keys[6]:
    active2_hp = 55
    active2_atk = 81
    active2_def = 60
    active2_spa = 50
    active2_spd = 70
    active2_spe = 97
    active2_type1 = "normal"
    active2_type2 = "none"
    active2_move1 = "facade"
    active2_move2 = "sucker punch"
    active2_move3 = "u-turn"
    active2_move4 = "crunch"
    active2_hp_evs = 0
    active2_atk_evs = 252
    active2_def_evs = 0
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "jolly"

if active2 == pokemon_keys[7]:
    active2_hp = 90
    active2_atk = 92
    active2_def = 87
    active2_spa = 75
    active2_spd = 85
    active2_spe = 76
    active2_type1 = "poison"
    active2_type2 = "ground"
    active2_move1 = "stealth rock"
    active2_move2 = "earth power"
    active2_move3 = "sludge wave"
    active2_move4 = "toxic"
    active2_hp_evs = 0
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 252
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "timid"

if active2 == pokemon_keys[8]:
    active2_hp = 81
    active2_atk = 102
    active2_def = 77
    active2_spa = 85
    active2_spd = 75
    active2_spe = 85
    active2_type1 = "poison"
    active2_type2 = "ground"
    active2_move1 = "sludge wave"
    active2_move2 = "earth power"
    active2_move3 = "ice beam"
    active2_move4 = "substitute"
    active2_hp_evs = 0
    active2_atk_evs = 0
    active2_def_evs = 4
    active2_spa_evs = 252
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "timid"

if active2 == pokemon_keys[9]:
    active2_hp = 95
    active2_atk = 70
    active2_def = 73
    active2_spa = 95
    active2_spd = 90
    active2_spe = 60
    active2_type1 = "fairy"
    active2_type2 = "none"
    active2_move1 = "monnblast"
    active2_move2 = "recover"
    active2_move3 = "protect"
    active2_move4 = "flamethrower"
    active2_hp_evs = 252
    active2_atk_evs = 0
    active2_def_evs = 236
    active2_spa_evs = 4
    active2_spd_evs = 4
    active2_spe_evs = 12
    active2_nature = "bold"

if active2 == pokemon_keys[10]:
    active2_hp = 130
    active2_atk = 85
    active2_def = 80
    active2_spa = 85
    active2_spd = 95
    active2_spe = 60
    active2_type1 = "water"
    active2_type2 = "ice"
    active2_move1 = "scald"
    active2_move2 = "freeze dry"
    active2_move3 = "protect"
    active2_move4 = "perish song"
    active2_hp_evs = 252
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 4
    active2_spd_evs = 252
    active2_spe_evs = 0
    active2_nature = "calm"
if active2 == pokemon_keys[11]:
    active2_hp = 130
    active2_atk = 65
    active2_def = 60
    active2_spa = 110
    active2_spd = 95
    active2_spe = 65
    active2_type1 = "water"
    active2_type2 = "none"
    active2_move1 = "scald"
    active2_move2 = "haze"
    active2_move3 = "wish"
    active2_move4 = "protect"
    active2_hp_evs = 252
    active2_atk_evs = 0
    active2_def_evs = 252
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 0
    active2_nature = "bold"

if active2 == pokemon_keys[12]:
    active2_hp = 65
    active2_atk = 65
    active2_def = 60
    active2_spa = 110
    active2_spd = 95
    active2_spe = 130
    active2_type1 = "electric"
    active2_type2 = "none"
    active2_move1 = "calm mind"
    active2_move2 = "thunderbolt"
    active2_move3 = "volt switch"
    active2_move4 = "alluring voice"
    active2_hp_evs = 0
    active2_atk_evs = 0
    active2_def_evs = 4
    active2_spa_evs = 252
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "timid"

if active2 == pokemon_keys[13]:
    active2_hp = 65
    active2_atk = 130
    active2_def = 60
    active2_spa = 95
    active2_spd = 110
    active2_spe = 65
    active2_type1 = "fire"
    active2_type2 = "none"
    active2_move1 = "flare blitz"
    active2_move2 = "facade"
    active2_move3 = "protect"
    active2_move4 = "copycat"
    active2_hp_evs = 252
    active2_atk_evs = 252
    active2_def_evs = 4
    active2_spa_evs = 0
    active2_spd_evs = 0
    active2_spe_evs = 0
    active2_nature = "adamant"

if active2 == pokemon_keys[14]:
    active2_hp = 65
    active2_atk = 60
    active2_def = 105
    active2_spa = 85
    active2_spd = 112.5
    active2_spe = 40
    active2_type1 = "normal"
    active2_type2 = "none"
    active2_move1 = "double edge"
    active2_move2 = "ice beam"
    active2_move3 = "recover"
    active2_move4 = "agility"
    active2_hp_evs = 252
    active2_atk_evs = 128
    active2_def_evs = 124
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 0
    active2_nature = "brave"

if active2 == pokemon_keys[15]:
    active2_hp = 70
    active2_atk = 60
    active2_def = 125
    active2_spa = 115
    active2_spd = 70
    active2_spe = 55
    active2_type1 = "water"
    active2_type2 = "rock"
    active2_move1 = "shell smash"
    active2_move2 = "hydro pump"
    active2_move3 = "endure"
    active2_move4 = "power gem"
    active2_hp_evs = 0
    active2_atk_evs = 0
    active2_def_evs = 4
    active2_spa_evs = 252
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "timid"

if active2 == pokemon_keys[16]:
    active2_hp = 60
    active2_atk = 115
    active2_def = 105
    active2_spa = 65
    active2_spd = 70
    active2_spe = 80
    active2_type1 = "water"
    active2_type2 = "rock"
    active2_move1 = "rapid spin"
    active2_move2 = "knock off"
    active2_move3 = "stone edge"
    active2_move4 = "liquidation"
    active2_hp_evs = 0
    active2_atk_evs = 252
    active2_def_evs = 4
    active2_spa_evs = 0
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "adamant"

if active2 == pokemon_keys[17]:
    active2_hp = 80
    active2_atk = 105
    active2_def = 65
    active2_spa = 60
    active2_spd = 75
    active2_spe = 130
    active2_type1 = "rock"
    active2_type2 = "flying"
    active2_move1 = "roost"
    active2_move2 = "stealth rock"
    active2_move3 = "stone edge"
    active2_move4 = "earthquake"
    active2_hp_evs = 0
    active2_atk_evs = 252
    active2_def_evs = 4
    active2_spa_evs = 0
    active2_spd_evs = 0
    active2_spe_evs = 252
    active2_nature = "adamant"

if active2 == pokemon_keys[18]:
    active2_hp = 160
    active2_atk = 110
    active2_def = 65
    active2_spa = 65
    active2_spd = 110
    active2_spe = 30
    active2_type1 = "normal"
    active2_type2 = "none"
    active2_move1 = "yawn"
    active2_move2 = "protect"
    active2_move3 = "earthquake"
    active2_move4 = "body slam"
    active2_hp_evs = 140
    active2_atk_evs = 116
    active2_def_evs = 252
    active2_spa_evs = 0
    active2_spd_evs = 0
    active2_spe_evs = 0
    active2_nature = "adamant"

if active2 == pokemon_keys[19]:
    active2_hp = 90
    active2_atk = 85
    active2_def = 100
    active2_spa = 95
    active2_spd = 125
    active2_spe = 85
    active2_type1 = "ice"
    active2_type2 = "flying"
    active2_move1 = "freeze dry"
    active2_move2 = "roost"
    active2_move3 = "substitute"
    active2_move4 = "haze"
    active2_hp_evs = 248
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 208
    active2_spd_evs = 0
    active2_spe_evs = 52
    active2_nature = "modest"

if active2 == pokemon_keys[20]:
    active2_hp = 90
    active2_atk = 90
    active2_def = 85
    active2_spa = 125
    active2_spd = 90
    active2_spe = 100
    active2_type1 = "electric"
    active2_type2 = "flying"
    active2_move1 = "hurricane"
    active2_move2 = "volt switch"
    active2_move3 = "thunder wave"
    active2_move4 = "roost"
    active2_hp_evs = 248
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 244
    active2_spd_evs = 0
    active2_spe_evs = 16
    active2_nature = "timid"

if active2 == pokemon_keys[21]:
    active2_hp = 90
    active2_atk = 100
    active2_def = 90
    active2_spa = 125
    active2_spd = 85
    active2_spe = 90
    active2_type1 = "fire"
    active2_type2 = "flying"
    active2_move1 = "flamethrower"
    active2_move2 = "will-o-wisp"
    active2_move3 = "air slash"
    active2_move4 = "roost"
    active2_hp_evs = 248
    active2_atk_evs = 0
    active2_def_evs = 248
    active2_spa_evs = 0
    active2_spd_evs = 0
    active2_spe_evs = 12
    active2_nature = "bold"

if active2 == pokemon_keys[22]:
    active2_hp = 91
    active2_atk = 134
    active2_def = 95
    active2_spa = 100
    active2_spd = 100
    active2_spe = 80
    active2_type1 = "dragon"
    active2_type2 = "flying"
    active2_move1 = "outrage "
    active2_move2 = "extreme speed"
    active2_move3 = "stomping tantrum"
    active2_move4 = "aerial ace"
    active2_hp_evs = 244
    active2_atk_evs = 252
    active2_def_evs = 4
    active2_spa_evs = 0
    active2_spd_evs = 4
    active2_spe_evs = 4
    active2_nature = "adamant"

if active2 == pokemon_keys[23]:
    active2_hp = 106
    active2_atk = 110
    active2_def = 90
    active2_spa = 154
    active2_spd = 90
    active2_spe = 130
    active2_type1 = "psychic"
    active2_type2 = "none"
    active2_move1 = "nasty plot"
    active2_move2 = "psystrike"
    active2_move3 = "thunderbolt"
    active2_move4 = "ice beam"
    active2_hp_evs = 0
    active2_atk_evs = 0
    active2_def_evs = 0
    active2_spa_evs = 252
    active2_spd_evs = 4
    active2_spe_evs = 252
    active2_nature = "timid"



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


if active2_nature == "adamant":
    nature_boost_atk2 = 1.10
    nature_drop_spa2 = 0.90
if active2_nature == "brave":
    nature_boost_atk2 = 1.10
    nature_drop_spe2 = 0.90
if active2_nature == "bold":
    nature_boost_def2 = 1.10
    nature_drop_atk2 = 0.90
if active2_nature == "modest":
    nature_boost_spa2 = 1.10
    nature_drop_atk2 = 0.90
if active2_nature == "calm":
    nature_boost_spd2 = 1.10
    nature_drop_atk22 = 0.90
if active2_nature == "jolly":
    nature_boost_spe2 = 1.10
    nature_drop_spa2 = 0.90
if active2_nature == "timid":
    nature_boost_spe2 = 1.10
    nature_drop_atk2 = 0.90

#Hp calculator
if active_hp_evs != 256:
    active_hp_stat = (math.floor(((2*active_hp+31+(active_hp_evs/4))*50)/100)+50+10)
else:
    print("parker likes dudes")

#stat calculators
if active_atk_evs != 256:
    active_atk_stats = math.floor(math.floor((math.floor(((2*active_atk+31+math.floor(active_atk_evs/4))*50)/100)+5)*nature_boost_atk)*nature_drop_atk) 
else:
    print("parker likes dudes")

if active_spa_evs != 256:
    active_spa_stats = math.floor((math.floor(((2*active_spa+31+math.floor(active_spa_evs/4))*50)/100)+5)*nature_boost_spa)
else:
    print("parker likes dudes")

if active_def_evs != 256:
    active_def_stats = math.floor((math.floor(((2*active_def+31+math.floor(active_def_evs/4))*50)/100)+5)*nature_boost_def) 
else:
    print("parker likes dudes")

if active_spd_evs != 256:
    active_spd_stats = math.floor((math.floor(((2*active_spd+31+math.floor(active_spd_evs/4))*50)/100)+5)*nature_boost_spd) 
else:
    print("parker likes dudes")

if active_spe_evs != 256:
    active_spe_stats = math.floor((math.floor(((2*active_spe+31+math.floor(active_spe_evs/4))*50)/100)+5)*nature_boost_spe) 
else:
    print("parker likes dudes")



#team 2 stats
if active2_hp_evs != 256:
    active2_hp_stats = (math.floor(((2*active2_hp+31+(active2_hp_evs/4))*50)/100)+50+10)
else:
    print("parker likes dudes")

#stat calculators
if active2_atk_evs != 256:
    active2_atk_stats = math.floor(math.floor((math.floor(((2*active2_atk+31+math.floor(active2_atk_evs/4))*50)/100)+5)*nature_boost_atk2)*nature_drop_atk2) 
else:
    print("parker likes dudes")

if active2_spa_evs != 256:
    active2_spa_stats = math.floor((math.floor(((2*active2_spa+31+math.floor(active2_spa_evs/4))*50)/100)+5)*nature_boost_spa2) 
else:
    print("parker likes dudes")

if active2_def_evs != 256:
    active2_def_stats = math.floor((math.floor(((2*active2_def+31+math.floor(active2_def_evs/4))*50)/100)+5)*nature_boost_def2) 
else:
    print("parker likes dudes")

if active2_spd_evs != 256:
    active2_spd_stats = math.floor((math.floor(((2*active2_spd+31+math.floor(active2_spd_evs/4))*50)/100)+5)*nature_boost_spd2) 
else:
    print("parker likes dudes")

if active2_spe_evs != 256:
    active2_spe_stats = math.floor((math.floor(((2*active2_spe+31+math.floor(active2_spe_evs/4))*50)/100)+5)*nature_boost_spe2) 
else:
    print("parker likes dudes")


t1_points= 0
t2_points=0
#actual fight 
print("Battle Start")
print("Player 1 sent out,", active, ",", active_type1, ",", active_type2)
print("Player 2 sent out,", active2, ",", active2_type1, ",", active2_type2)

#Here we need to make a code that will loop to have infinite turns until someone types concede,
#or one side takes out all 6 pokemon. An input should be repeated, either fight, switch, or
#concede. If either fight or switch are chosen it will either display your switches or your active
#moves. After one input is done it should then ask another for player 2 which same rules apply.
#Every time something is KO'd add 1 point to either t1_points or t2_points dpending on which team
#got the KO. If all inputs are entered (and none are the cause the game to end) then the calculation
#will play out, change values and then repeat the code.


while t1_points != 6 and t2_points != 6:
    turn_p1 = input("Fight or switch: ")
    if turn_p1 == "switch":
        print("bsakjhbf")
        switch_p1 = input("Swap to,", t1mon2, t1mon3, t1mon4, t1mon5, t1mon6 , " or back")
        while switch_p1 == "back" or "Back":
                turn_p1 = input("Fight or switch")
                if turn_p1 == "switch" or "Switch":
                    switch_p1 = input("Swap to,", t1mon2, t1mon3, t1mon4, t1mon5, t1mon6 , " or back")
        
        if switch_p1 == t1mon2:
            move_p1 = "switch2"
        elif switch_p1 == t1mon3:
            move_p1 = "switch3"
        elif switch_p1 == t1mon4:
            move_p1 = "switch4"
        elif switch_p1 == t1mon5:
            move_p1 = "switch5"
        elif switch_p1 == t1mon6:
            move_p1 = "switch6"
        else:
            print("nope")
    elif turn_p1 == "fight" or "Fight":
        attack_p1 = input("Pick,", active_move1, active_move2, active_move3, active_move4, " or back")
        while attack_p1 == "back" or "Back":
            turn_p1 = input("Fight or switch")
            if turn_p1 == "fight" or "Fight":
                attack_p1 = input("Pick,", active_move1, active_move2, active_move3, active_move4, " or back")
        if attack_p1 == active_move1:
            move_p1 = "attack1"
        elif attack_p1 == active_move2:
            move_p1 = "attack2"
        elif attack_p1 == active_move3:
            move_p1 = "attack3"
        elif attack_p1 == active_move4:
            move_p1 = "attack4"
        else:
            print("nuh uh")
    else:
        print("nuh uh")
    print(move_p1)





#need damage numbers, types, effectiveness, and two equations for physical and special 
stab = 1.0
effective = 1
#90 is a placeholder for now 
power = 90
role = random.uniform(0.85, 1.0)
print(round(role, 2))
calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*power*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
print(calculation)
print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2, "w/ a 90 base power move")





