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
           {"type":{"type1":"electric", "type2":"none"},
           "hp":65,
           "atk":65,
           "def":60,
           "spa":110,
           "spd":95,
           "spe":130,
           "m1":"calm mind",
           "m2":"thundebolt",
           "m3":"volt switch",
           "m4":"alluring voice",
           "hp_ev":0,
           "atk_ev":0,
           "def_ev":4,
           "spa_ev":252,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"timid"},

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
           {"type":{"type1":"normal", "type2":"none"},
           "hp":65,
           "atk":0,
           "def":105,
           "spa":145,
           "spd":113,
           "spe":40,
           "m1":"tri attack",
           "m2":"ice beam",
           "m3":"recover",
           "m4":"agility",
           "hp_ev":252,
           "atk_ev":0,
           "def_ev":124,
           "spa_ev":145,
           "spd_ev":4,
           "spe_ev":0,
           "nature":"modest"},

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
           {"type":{"type1":"water", "type2":"rock"},
           "hp":60,
           "atk":115,
           "def":105,
           "spa":65,
           "spd":70,
           "spe":55,
           "m1":"rapid spin",
           "m2":"knock off",
           "m3":"stone edge",
           "m4":"liquidation",
           "hp_ev":0,
           "atk_ev":252,
           "def_ev":4,
           "spa_ev":0,
           "spd_ev":0,
           "spe_ev":252,
           "nature":"adamant"},


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
           {"type":{"type1":"normal", "type2":"none"},
           "hp":160,
           "atk":110,
           "def":65,
           "spa":65,
           "spd":110,
           "spe":30,
           "m1":"yawn",
           "m2":"protect",
           "m3":"earthquake",
           "m4":"body slam",
           "hp_ev":140,
           "atk_ev":116,
           "def_ev":252,
           "spa_ev":0,
           "spd_ev":0,
           "spe_ev":0,
           "nature":"adamant"},

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
           {"type":{"type1":"psychic", "type2":"none"}, 
           "hp":106,
           "atk":110,
           "def":90,
           "spa":154,
           "spd":90,
           "spe":130,
           "m1":"nasty plot",
           "m2":"psystrike",
           "m3":"thunderbolt",
           "m4":"ice beam",
           "hp_ev":0,
           "atk_ev":0,
           "def_ev":0,
           "spa_ev":252,
           "spd_ev":4,
           "spe_ev":252,
           "nature":"timid"},
        }

#all moves have move types to determine effcetivness (fire 2x dmg to grass, etc) a dmg type
#which determines what stat uses calculation (atk if physical that damages def, spp is special
# that dmages spd, and status which for now will be no damage no effect (just a dead move)
# as they act as an effect.)
moves = {"sludge bomb":
         {"power": 0, "dmg_type": "special", "move_type": "poison"},
         "leaf storm":
         {"power": 0, "dmg_type": "special", "move_type": "grass"},
         "poison powder":
         {"power": 0, "dmg_type": "status", "move_type": "poison"},
         "protect":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "blast burn":
         {"power": 0, "dmg_type": "special", "move_type": "fire"},
         "heat wave":
         {"power": 95, "dmg_type": "special", "move_type": "fire"},
         "air slash":
         {"power": 0, "dmg_type": "special", "move_type": "flying"},
         "scorching sands":
         {"power": 70, "dmg_type": "special", "move_type": "ground"},
         "water pledge":
         {"power": 80, "dmg_type": "special", "move_type": "water"},
         "shell smash":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "flash cannon":
         {"power": 0, "dmg_type": "special", "move_type": "steel"},
         "water spout":
         {"power": 150, "dmg_type": "special", "move_type": "water"},
         "substitute":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "quiver dance":
         {"power": 0, "dmg_type": "status", "move_type": "bug"},
         "sleep powder":
         {"power": 0, "dmg_type": "status", "move_type": "grass"},
         "bug buzz":
         {"power": 0, "dmg_type": "special", "move_type": "bug"},
         "knock off":
         {"power": 65, "dmg_type": "physical", "move_type": "dark"},
         "poison jab":
         {"power": 0, "dmg_type": "physical", "move_type": "poison"},
         "drill run":
         {"power": 80, "dmg_type": "physical", "move_type": "ground"},
         "u-turn":
         {"power": 70, "dmg_type": "physical", "move_type": "bug"},
         "roost":
         {"power": 0, "dmg_type": "status", "move_type": "flying"},
         "brave bird":
         {"power": 120, "dmg_type": "physical", "move_type": "flying"},
         "return":
         {"power": 102, "dmg_type": "physical", "move_type": "normal"},
         "facade":
         {"power": 0, "dmg_type": "physical", "move_type": "normal"},
         "sucker punch":
         {"power": 70, "dmg_type": "physical", "move_type": "dark"},
         "crunch":
         {"power": 80, "dmg_type": "physical", "move_type": "dark"},
         "stealth rock":
         {"power": 0, "dmg_type": "status", "move_type": "rock"},
         "earth power":
         {"power": 0, "dmg_type": "special", "move_type": "ground"},
         "sludge wave":
         {"power": 95, "dmg_type": "special", "move_type": "poison"},
         "toxic":
         {"power": 0, "dmg_type": "status", "move_type": "poison"},
         "ice beam":
         {"power": 0, "dmg_type": "special", "move_type": "ice"},
         "recover":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "moonblast":
         {"power": 0, "dmg_type": "special", "move_type": "fairy"},
         "flamethrower":
         {"power": 0, "dmg_type": "special", "move_type": "fire"},
         "scald":
         {"power": 0, "dmg_type": "special", "move_type": "water"},
         "freeze dry":
         {"power": 0, "dmg_type": "special", "move_type": "ice"},
         "perish song":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "haze":
         {"power": 0, "dmg_type": "status", "move_type": "ice"},
         "wish":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "calm mind":
         {"power": 0, "dmg_type": "status", "move_type": "psychic"},
         "thunderbolt":
         {"power": 0, "dmg_type": "special", "move_type": "electric"},
         "volt switch":
         {"power": 70, "dmg_type": "special", "move_type": "electric"},
         "alluring voice":
         {"power": 0, "dmg_type": "special", "move_type": "fairy"},
         "flare blitz":
         {"power": 120, "dmg_type": "physical", "move_type": "fire"},
         "copycat":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "double edge":
         {"power": 120, "dmg_type": "physical", "move_type": "normal"},
         "agility":
         {"power": 0, "dmg_type": "status", "move_type": "psychic"},
         "tri attack":
         {"power": 0, "dmg_type": "special", "move_type": "normal"},
         "hydro pump":
         {"power": 0, "dmg_type": "special", "move_type": "water"},
         "power gem":
         {"power": 90, "dmg_type": "special", "move_type": "rock"},
         "endure":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "rapid spin":
         {"power": 40, "dmg_type": "physical", "move_type": "normal"},
         "stone edge":
         {"power": 100, "dmg_type": "physical", "move_type": "rock"},
         "liquidation":
         {"power": 85, "dmg_type": "physical", "move_type": "water"},
         "earthquake":
         {"power": 100, "dmg_type": "physical", "move_type": "ground"},
         "yawn":
         {"power": 0, "dmg_type": "status", "move_type": "normal"},
         "body slam":
         {"power": 85, "dmg_type": "physical", "move_type": "normal"},
         "thunder wave":
         {"power": 0, "dmg_type": "status", "move_type": "electric"},
         "hurricane":
         {"power": 110, "dmg_type": "special", "move_type": "flying"},
         "will-o-wisp":
         {"power": 0, "dmg_type": "status", "move_type": "fire"},
         "outrage":
         {"power": 120, "dmg_type": "physical", "move_type": "dragon"},
         "extreme speed":
         {"power": 80, "dmg_type": "physical", "move_type": "normal"},
         "aerial ace":
         {"power": 60, "dmg_type": "physical", "move_type": "flying"},
         "nasty plot":
         {"power": 0, "dmg_type": "status", "move_type": "dark"},
         "psystrike":
         {"power": 120, "dmg_type": "special", "move_type": "psychic"},
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


#------STATS FOR TEAM 1------
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
    active_move1 = moves["sludge bomb"]
    active_move2 = moves["leaf storm"]
    active_move3 = moves["poison powder"]
    active_move4 = moves["protect"]
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
    active_move1 = moves["blast burn"]
    active_move2 = moves["heat wave"]
    active_move3 = moves["air slash"]
    active_move4 = moves["scorching sands"]
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
    active_move1 = moves["water pledge"]
    active_move2 = moves["shell smash"]
    active_move3 = moves["flash cannon"]
    active_move4 = moves["water spout"]
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
    active_move1 = moves["substitute"]
    active_move2 = moves["bug buzz"]
    active_move3 = moves["quiver dance"]
    active_move4 = moves["sleep powder"]
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
    active_move1 = moves["knock off"]
    active_move2 = moves["poison jab"]
    active_move3 = moves["drill run"]
    active_move4 = moves["u-turn"]
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
    active_move1 = moves["u-turn"]
    active_move2 = moves["roost"]
    active_move3 = moves["brave bird"]
    active_move4 = moves["return"]
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
    active_move1 = moves["facade"]
    active_move2 = moves["sucker punch"]
    active_move3 = moves["u-turn"]
    active_move4 = moves["crunch"]
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
    active_move1 = moves["stealth rock"]
    active_move2 = moves["earth power"]
    active_move3 = moves["sludge wave"]
    active_move4 = moves["toxic"]
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
    active_move1 = moves["sludge wave"]
    active_move2 = moves["earth power"]
    active_move3 = moves["ice beam"]
    active_move4 = moves["substitute"]
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
    active_move1 = moves["moonblast"]
    active_move2 = moves["recover"]
    active_move3 = moves["protect"]
    active_move4 = moves["flamethrower"]
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
    active_move1 = moves["scald"]
    active_move2 = moves["freeze dry"]
    active_move3 = moves["protect"]
    active_move4 = moves["perish song"]
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
    active_move1 = moves["scald"]
    active_move2 = moves["haze"]
    active_move3 = moves["wish"]
    active_move4 = moves["protect"]
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
    active_move1 = moves["calm mind"]
    active_move2 = moves["thunderbolt"]
    active_move3 = moves["volt switch"]
    active_move4 = moves["alluring voice"]
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
    active_move1 = moves["flare blitz"]
    active_move2 = moves["facade"]
    active_move3 = moves["protect"]
    active_move4 = moves["copycat"]
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
    active_move1 = moves["tri attack"]
    active_move2 = moves["ice beam"]
    active_move3 = moves["recover"]
    active_move4 = moves["agility"]
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
    active_move1 = moves["shell smash"]
    active_move2 = moves["hydro pump"]
    active_move3 = moves["endure"]
    active_move4 = moves["power gem"]
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
    active_move1 = moves["rapid spin"]
    active_move2 = moves["knock off"]
    active_move3 = moves["stone edge"]
    active_move4 = moves["liquidation"]
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
    active_move1 = moves["roost"]
    active_move2 = moves["stealth rock"]
    active_move3 = moves["stone edge"]
    active_move4 = moves["earthquake"]
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
    active_move1 = moves["yawn"]
    active_move2 = moves["protect"]
    active_move3 = moves["earthquake"]
    active_move4 = moves["body slam"]
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
    active_move1 = moves["freeze dry"]
    active_move2 = moves["roost"]
    active_move3 = moves["substitute"]
    active_move4 = moves["haze"]
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
    active_move1 = moves["hurricane"]
    active_move2 = moves["volt switch"]
    active_move3 = moves["thunder wave"]
    active_move4 = moves["roost"]
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
    active_move1 = moves["flamethrower"]
    active_move2 = moves["will-o-wisp"]
    active_move3 = moves["air slash"]
    active_move4 = moves["roost"]
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
    active_move1 = moves["outrage"]
    active_move2 = moves["extreme speed"]
    active_move3 = moves["stomping tantrum"]
    active_move4 = moves["aerial ace"]
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
    active_move1 = moves["nasty plot"]
    active_move2 = moves["psystrike"]
    active_move3 = moves["thunderbolt"]
    active_move4 = moves["ice beam"]
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
    active2_move1 = moves["sludge bomb"]
    active2_move2 = moves["leaf storm"]
    active2_move3 = moves["poison powder"]
    active2_move4 = moves["protect"]
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
    active2_move1 = moves["blast burn"]
    active2_move2 = moves["heat wave"]
    active2_move3 = moves["air slash"]
    active2_move4 = moves["scorching sands"]
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
    active2_move1 = moves["water pledge"]
    active2_move2 = moves["shell smash"]
    active2_move3 = moves["flash cannon"]
    active2_move4 = moves["water spout"]
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
    active2_move1 = moves["substitute"]
    active2_move2 = moves["bug buzz"]
    active2_move3 = moves["quiver dance"]
    active2_move4 = moves["sleep powder"]
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
    active2_move1 = moves["knock off"]
    active2_move2 = moves["poison jab"]
    active2_move3 = moves["drill run"]
    active2_move4 = moves["u-turn"]
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
    active2_move1 = moves["u-turn"]
    active2_move2 = moves["roost"]
    active2_move3 = moves["brave bird"]
    active2_move4 = moves["return"]
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
    active2_move1 = moves["facade"]
    active2_move2 = moves["sucker punch"]
    active2_move3 = moves["u-turn"]
    active2_move4 = moves["crunch"]
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
    active2_move1 = moves["stealth rock"]
    active2_move2 = moves["earth power"]
    active2_move3 = moves["sludge wave"]
    active2_move4 = moves["toxic"]
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
    active2_move1 = moves["sludge wave"]
    active2_move2 = moves["earth power"]
    active2_move3 = moves["ice beam"]
    active2_move4 = moves["substitute"]
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
    active2_move1 = moves["monnblast"]
    active2_move2 = moves["recover"]
    active2_move3 = moves["protect"]
    active2_move4 = moves["flamethrower"]
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
    active2_move1 = moves["scald"]
    active2_move2 = moves["freeze dry"]
    active2_move3 = moves["protect"]
    active2_move4 = moves["perish song"]
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
    active2_move1 = moves["scald"]
    active2_move2 = moves["haze"]
    active2_move3 = moves["wish"]
    active2_move4 = moves["protect"]
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
    active2_move1 = moves["calm mind"]
    active2_move2 = moves["thunderbolt"]
    active2_move3 = moves["volt switch"]
    active2_move4 = moves["alluring voice"]
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
    active2_move1 = moves["flare blitz"]
    active2_move2 = moves["facade"]
    active2_move3 = moves["protect"]
    active2_move4 = moves["copycat"]
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
    active2_move1 = moves["tri attack"]
    active2_move2 = moves["ice beam"]
    active2_move3 = moves["recover"]
    active2_move4 = moves["agility"]
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
    active2_move1 = moves["shell smash"]
    active2_move2 = moves["hydro pump"]
    active2_move3 = moves["endure"]
    active2_move4 = moves["power gem"]
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
    active2_move1 = moves["rapid spin"]
    active2_move2 = moves["knock off"]
    active2_move3 = moves["stone edge"]
    active2_move4 = moves["liquidation"]
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
    active2_move1 = moves["roost"]
    active2_move2 = moves["stealth rock"]
    active2_move3 = moves["stone edge"]
    active2_move4 = moves["earthquake"]
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
    active2_move1 = moves["yawn"]
    active2_move2 = moves["protect"]
    active2_move3 = moves["earthquake"]
    active2_move4 = moves["body slam"]
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
    active2_move1 = moves["freeze dry"]
    active2_move2 = moves["roost"]
    active2_move3 = moves["substitute"]
    active2_move4 = moves["haze"]
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
    active2_move1 = moves["hurricane"]
    active2_move2 = moves["volt switch"]
    active2_move3 = moves["thunder wave"]
    active2_move4 = moves["roost"]
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
    active2_move1 = moves["flamethrower"]
    active2_move2 = moves["will-o-wisp"]
    active2_move3 = moves["air slash"]
    active2_move4 = moves["roost"]
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
    active2_move1 = moves["outrage"]
    active2_move2 = moves["extreme speed"]
    active2_move3 = moves["stomping tantrum"]
    active2_move4 = moves["aerial ace"]
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
    active2_move1 = moves["nasty plot"]
    active2_move2 = moves["psystrike"]
    active2_move3 = moves["thunderbolt"]
    active2_move4 = moves["ice beam"]
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


stab = 1.0
effective = 1
role = random.uniform(0.85, 1.0)
print(round(role, 2))


#actual fight 
print("Battle Start")
print("Player 1 sent out,", active, ",", active_type1, ",", active_type2)
print("Player 2 sent out,", active2, ",", active2_type1, ",", active2_type2)
print(" ")
#Here we need to make a code that will loop to have infinite turns until someone types concede,
#or one side takes out all 6 pokemon. An input should be repeated, either fight, switch, or
#concede. If either fight or switch are chosen it will either display your switches or your active
#moves. After one input is done it should then ask another for player 2 which same rules apply.
#Every time something is KO'd add 1 point to either t1_points or t2_points dpending on which team
#got the KO. If all inputs are entered (and none are the cause the game to end) then the calculation
#will play out, change values and then repeat the code.

turn_num = 1
while t1_points != 6 and t2_points != 6:
    print("Turn",turn_num)
    print("[", active, "]", "is the active", ",", " Damaging ", active2)
    turn_p1 = input("Fight or switch: ")
    if turn_p1 == "switch":
        print("[", t1mon2,"]",  "[", t1mon3,"]", "[", t1mon4,"]", "[", t1mon5,"]", "[", t1mon6, "]")
        switch_p1 = input("Swap to, mon2, mon3, mon4, mon5, mon6: ")
        if switch_p1 == t1mon2:
            move_p1 = "switch2"
        elif switch_p1 == "mon2":
            move_p1 = "switch2"
        elif switch_p1 == t1mon3:
            move_p1 = "switch3"
        elif switch_p1 == "mon3":
            move_p1 = "switch3"
        elif switch_p1 == t1mon4:
            move_p1 = "switch4"
        elif switch_p1 == "mon4":
            move_p1 = "switch4"
        elif switch_p1 == t1mon5:
            move_p1 = "switch5"
        elif switch_p1 == "mon5":
            move_p1 = "switch5"
        elif switch_p1 == t1mon6:
            move_p1 = "switch6"
        elif switch_p1 == "mon6":
            move_p1 = "switch6"
        else:
            print("nope")
    elif turn_p1 == "Switch":
        print("[", t1mon2,"]",  "[", t1mon3,"]", "[", t1mon4,"]", "[", t1mon5,"]", "[", t1mon6, "]")
        switch_p1 = input("Swap to, mon2, mon3, mon4, mon5, mon6: ")
        if switch_p1 == t1mon2:
            move_p1 = "switch2"
        elif switch_p1 == "mon2":
            move_p1 = "switch2"
        elif switch_p1 == t1mon3:
            move_p1 = "switch3"
        elif switch_p1 == "mon3":
            move_p1 = "switch3"
        elif switch_p1 == t1mon4:
            move_p1 = "switch4"
        elif switch_p1 == "mon4":
            move_p1 = "switch4"
        elif switch_p1 == t1mon5:
            move_p1 = "switch5"
        elif switch_p1 == "mon5":
            move_p1 = "switch5"
        elif switch_p1 == t1mon6:
            move_p1 = "switch6"
        elif switch_p1 == "mon6":
            move_p1 = "switch6"
        else:
            print("nope")
    elif turn_p1 == "fight":
        print("[", active_move1,"]",  "[", active_move2,"]", "[", active_move3,"]", "[", active_move4,"]" )
        attack_p1 = input("Pick, move1, move2, move3, or move4: ")
        if attack_p1 == active_move1:
            move_p1 = "attack1"
        elif attack_p1 == "move1":
            move_p1 = "attack1"
        elif attack_p1 == active_move2:
            move_p1 = "attack2"
        elif attack_p1 == "move2":
            move_p1 = "attack2"
        elif attack_p1 == active_move3:
            move_p1 = "attack3"
        elif attack_p1 == "move3":
            move_p1 = "attack3"
        elif attack_p1 == active_move4:
            move_p1 = "attack4"
        elif attack_p1 == "move4":
            move_p1 = "attack4"
        else:
            print("nuh uh")
    elif turn_p1 == "Fight":
        print("[", active_move1,"]",  "[", active_move2,"]", "[", active_move3,"]", "[", active_move4,"]" )
        attack_p1 = input("Pick, move1, move2, move3, or move4: ")
        if attack_p1 == active_move1:
            move_p1 = "attack1"
        elif attack_p1 == "move1":
            move_p1 = "attack1"
        elif attack_p1 == active_move2:
            move_p1 = "attack2"
        elif attack_p1 == "move2":
            move_p1 = "attack2"
        elif attack_p1 == active_move3:
            move_p1 = "attack3"
        elif attack_p1 == "move3":
            move_p1 = "attack3"
        elif attack_p1 == active_move4:
            move_p1 = "attack4"
        elif attack_p1 == "move4":
            move_p1 = "attack4"
        else:
            print("nuh uh")
    else:
        print("nuh uh")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    next_player = input("Player 2 ready?: ")
    if next_player == "yes":
        print("[", active2, "]", "is the active", ",", " Damaging ", active)
        turn_p2 = input("Fight or switch: ")
        if turn_p2 == "switch":
            print("[", t2mon2,"]",  "[", t2mon3,"]", "[", t2mon4,"]", "[", t2mon5,"]", "[", t2mon6, "]")
            switch_p2 = input("Swap to, mon2, mon3, mon4, mon5, mon6: ")
            if switch_p2 == t2mon2:
                move_p2 = "switch2"
            elif switch_p2 == "mon2":
                move_p2 = "switch2"
            elif switch_p2 == t2mon3:
                move_p2 = "switch3"
            elif switch_p2 == "mon3":
                move_p2 = "switch3"
            elif switch_p2 == t2mon4:
                move_p2 = "switch4"
            elif switch_p2 == "mon4":
                move_p2 = "switch4"
            elif switch_p2 == t2mon5:
                move_p2 = "switch5"
            elif switch_p2 == "mon5":
                move_p2 = "switch5"
            elif switch_p2 == t2mon6:
                move_p2 = "switch6"
            elif switch_p2 == "mon6":
                move_p2 = "switch6"
            else:
                print("nope")
        elif turn_p2 == "Switch":
            print("[", t2mon2,"]",  "[", t2mon3,"]", "[", t2mon4,"]", "[", t2mon5,"]", "[", t2mon6, "]")
            switch_p2 = input("Swap to, mon2, mon3, mon4, mon5, mon6: ")
            if switch_p2 == t2mon2:
                move_p2 = "switch2"
            elif switch_p2 == "mon2":
                move_p2 = "switch2"
            elif switch_p2 == t2mon3:
                move_p2 = "switch3"
            elif switch_p2 == "mon3":
                move_p2 = "switch3"
            elif switch_p2 == t2mon4:
                move_p2 = "switch4"
            elif switch_p2 == "mon4":
                move_p2 = "switch4"
            elif switch_p2 == t2mon5:
                move_p2 = "switch5"
            elif switch_p2 == "mon5":
                move_p2 = "switch5"
            elif switch_p2 == t2mon6:
                move_p2 = "switch6"
            elif switch_p2 == "mon6":
                move_p2 = "switch6"
            else:
                print("nope")
        elif turn_p2 == "fight":
            print("[", active2_move1,"]",  "[", active2_move2,"]", "[", active2_move3,"]", "[", active2_move4,"]" )
            attack_p2 = input("Pick, move1, move2, move3, or move4: ")
            if attack_p2 == active2_move1:
                move_p2 = "attack1"
            elif attack_p2 == "move1":
                move_p2 = "attack1"
            elif attack_p2 == active2_move2:
                move_p2 = "attack2"
            elif attack_p2 == "move2":
                move_p2 = "attack2"
            elif attack_p2 == active_move3:
                move_p2 = "attack3"
            elif attack_p2 == "move3":
                move_p2 = "attack3"
            elif attack_p2 == active_move4:
                move_p2 = "attack4"
            elif attack_p2 == "move4":
                move_p2 = "attack4"
            else:
                print("nuh uh")
        elif turn_p2 == "Fight":
            print("[", active2_move1,"]",  "[", active2_move2,"]", "[", active2_move3,"]", "[", active2_move4,"]" )
            attack_p2 = input("Pick, move1, move2, move3, or move4: ")
            if attack_p2 == active2_move1:
                move_p2 = "attack1"
            elif attack_p2 == "move1":
                move_p2 = "attack1"
            elif attack_p2 == active2_move2:
                move_p2 = "attack2"
            elif attack_p2 == "move2":
                move_p2 = "attack2"
            elif attack_p2 == active2_move3:
                move_p2 = "attack3"
            elif attack_p2 == "move3":
                move_p2 = "attack3"
            elif attack_p2 == active2_move4:
                move_p2 = "attack4"
            elif attack_p2 == "move4":
                move_p2 = "attack4"
            else:
                print("nuh uh")
        else:
            print("nuh uh")
    else:
        ("worng answer")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")


    # moves play out
    spe_tie = (1, 2)
    if active_spe_stats >= active2_spe_stats:
        faster_mon = 1
    elif active_spe_stats <= active2_spe_stats:
        faster_mon = 2
    elif active_spe_stats == active2_spe_stats:
        faster_mon = random.choice(spe_tie)
    else:
        print("nuh uh")


# this the outcome if the active on team 1 i faster so it checks for if either team switched, if team 1 attacked,
# and if active for team 2 survived and attacked 

    
   
   
   
   
   
   
   
    if faster_mon == 1:
        if move_p1 == "switch2":
            active, t1mon2 == t1mon2, active
            print("Player 1 withdrew,", active, ", Go,", t1mon2)
        elif move_p1 == "switch3":
            active, t1mon3 == t1mon3, active
            print("Player 1 withdrew,", active, ", Go,", t1mon3)
        elif move_p1 == "switch4":
            active, t1mon4 == t1mon4, active
            print("Player 1 withdrew,", active, ", Go,", t1mon4)
        elif move_p1 == "switch5":
            active, t1mon5 == t1mon5, active
            print("Player 1 withdrew,", active, ", Go,", t1mon5)
        elif move_p1 == "switch6":
            active, t1mon6 == t1mon6, active
            print("Player 1 withdrew,", active, ", Go,", t1mon6)
        
        if move_p2 == "switch2":
            active2, t2mon2 == t2mon2, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon2)
        elif move_p2 == "switch3":
            active2, t2mon3 == t2mon3, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon3)
        elif move_p2 == "switch4":
            active2, t2mon4 == t2mon4, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon4)
        elif move_p2 == "switch5":
            active2, t2mon5 == t2mon5, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon5)
        elif move_p2 == "switch6":
            active2, t2mon6 == t2mon6, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon6)
        
        if move_p1 == "attack1":
            if active_move1["move_type"] == active_type1:
                stab= 1.5
            elif active_move1["move_type"] == active_type2:
                stab = 1.5
            else:
                stab = 1
            

            if active_move1["move_type"] == "grass":
                if active2_type1 == "grass":
                    effective/2
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective*2
                elif active2_type1 == "electric":
                    effective * 1
                elif active2_type1 == "ice":
                    effective * 1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective/2
                elif active2_type1 == "ground":
                    effective*2
                elif active2_type1 == "flying":
                    effective/2
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective/2
                elif active2_type1 == "rock":
                    effective*2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective/2
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1
            
            elif active_move1["move_type"] == "fire":
                if active2_type1 == "grass":
                    effective*2
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective/2
                elif active2_type1 == "electric":
                    effective * 1
                elif active2_type1 == "ice":
                    effective * 2
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective*1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*2
                elif active2_type1 == "rock":
                    effective/2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective/2
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective*2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "water":
                if active2_type1 == "grass":
                    effective/2
                elif active2_type1 == "fire":
                    effective*2
                elif active2_type1 == "water":
                    effective/2
                elif active2_type1 == "electric":
                    effective * 1
                elif active2_type1 == "ice":
                    effective * 1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective*2
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective/2
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective*1
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "electric":
                if active2_type1 == "grass":
                    effective/2
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*2
                elif active2_type1 == "electric":
                    effective/2
                elif active2_type1 == "ice":
                    effective * 1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective*0
                elif active2_type1 == "flying":
                    effective*2
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective/2
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective*1
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ice":
                if active2_type1 == "grass":
                    effective*2
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective/2
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective/2
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 2
                elif active2_type1 == "flying":
                    effective*2
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1
            
            elif active_move1["move_type"] == "fighting":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*2
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective/2
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective/2
                elif active2_type1 == "psychic":
                    effective/2
                elif active2_type1 == "bug":
                    effective/2
                elif active2_type1 == "rock":
                    effective*2
                elif active2_type1 == "ghost":
                    effective * 0
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 2
                elif active2_type1 == "steel":
                    effective*2
                elif active2_type1 == "fairy":
                    effective/2
                elif active2_type1 == "normal":
                    effective *2

            elif active_move1["move_type"] == "poison":
                if active2_type1 == "grass":
                    effective*2
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective/2
                elif active2_type1 == "ground":
                    effective/2
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective/2
                elif active2_type1 == "ghost":
                    effective/2
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective*0
                elif active2_type1 == "fairy":
                    effective * 2
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ground":
                if active2_type1 == "grass":
                    effective/2
                elif active2_type1 == "fire":
                    effective*2
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*2
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*2
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*0
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective/2
                elif active2_type1 == "rock":
                    effective*2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective*2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "flying":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective/2
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 2
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*2
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*2
                elif active2_type1 == "rock":
                    effective/2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "psychic":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 2
                elif active2_type1 == "poison":
                    effective*2
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective/2
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 0
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "bug":
                if active2_type1 == "grass":
                    effective*2
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective/2
                elif active2_type1 == "poison":
                    effective/2
                elif active2_type1 == "ground":
                    effective*1
                elif active2_type1 == "flying":
                    effective/2
                elif active2_type1 == "psychic":
                    effective * 2
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective /2
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 2
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective /2
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "rock":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective /2
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective/2
                elif active2_type1 == "flying":
                    effective*2
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*2
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ghost":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 2
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 2
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective/2
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *0

            elif active_move1["move_type"] == "dragon":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*2
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 0
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "dark":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective/2
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 2
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 2
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective /2
                elif active2_type1 == "steel":
                    effective*1
                elif active2_type1 == "fairy":
                    effective /2
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "steel":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective/2
                elif active2_type1 == "electric":
                    effective/2
                elif active2_type1 == "ice":
                    effective*2
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*2
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 2
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "fairy":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective/2
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 2
                elif active2_type1 == "poison":
                    effective/2
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective*1
                elif active2_type1 == "ghost":
                    effective * 1
                elif active2_type1 == "dragon":
                    effective*2
                elif active2_type1 == "dark":
                    effective * 2
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            elif active_move1["move_type"] == "normal":
                if active2_type1 == "grass":
                    effective*1
                elif active2_type1 == "fire":
                    effective*1
                elif active2_type1 == "water":
                    effective*1
                elif active2_type1 == "electric":
                    effective*1
                elif active2_type1 == "ice":
                    effective*1
                elif active2_type1 == "fighting":
                    effective * 1
                elif active2_type1 == "poison":
                    effective*1
                elif active2_type1 == "ground":
                    effective* 1
                elif active2_type1 == "flying":
                    effective*1
                elif active2_type1 == "psychic":
                    effective * 1
                elif active2_type1 == "bug":
                    effective*1
                elif active2_type1 == "rock":
                    effective/2
                elif active2_type1 == "ghost":
                    effective * 0
                elif active2_type1 == "dragon":
                    effective*1
                elif active2_type1 == "dark":
                    effective * 1
                elif active2_type1 == "steel":
                    effective/2
                elif active2_type1 == "fairy":
                    effective * 1
                elif active2_type1 == "normal":
                    effective *1

            




            
            
            
            if active_move1["move_type"] == "grass":
                if active2_type2 == "grass":
                    effective/2
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective*2
                elif active2_type2 == "electric":
                    effective * 1
                elif active2_type2 == "ice":
                    effective * 1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective/2
                elif active2_type2 == "ground":
                    effective*2
                elif active2_type2 == "flying":
                    effective/2
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective/2
                elif active2_type2 == "rock":
                    effective*2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective/2
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1
            
            elif active_move1["move_type"] == "fire":
                if active2_type2 == "grass":
                    effective*2
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective/2
                elif active2_type2 == "electric":
                    effective * 1
                elif active2_type2 == "ice":
                    effective * 2
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective*1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*2
                elif active2_type2 == "rock":
                    effective/2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective/2
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective*2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "water":
                if active2_type2 == "grass":
                    effective/2
                elif active2_type2 == "fire":
                    effective*2
                elif active2_type2 == "water":
                    effective/2
                elif active2_type2 == "electric":
                    effective * 1
                elif active2_type2 == "ice":
                    effective * 1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective*2
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective/2
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective*1
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "electric":
                if active2_type2 == "grass":
                    effective/2
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*2
                elif active2_type2 == "electric":
                    effective/2
                elif active2_type2 == "ice":
                    effective * 1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective*0
                elif active2_type2 == "flying":
                    effective*2
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective/2
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective*1
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ice":
                if active2_type2 == "grass":
                    effective*2
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective/2
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective/2
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 2
                elif active2_type2 == "flying":
                    effective*2
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1
            
            elif active_move1["move_type"] == "fighting":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*2
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective/2
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective/2
                elif active2_type2 == "psychic":
                    effective/2
                elif active2_type2 == "bug":
                    effective/2
                elif active2_type2 == "rock":
                    effective*2
                elif active2_type2 == "ghost":
                    effective * 0
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 2
                elif active2_type2 == "steel":
                    effective*2
                elif active2_type2 == "fairy":
                    effective/2
                elif active2_type2 == "normal":
                    effective *2

            elif active_move1["move_type"] == "poison":
                if active2_type2 == "grass":
                    effective*2
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective/2
                elif active2_type2 == "ground":
                    effective/2
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective/2
                elif active2_type2 == "ghost":
                    effective/2
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective*0
                elif active2_type2 == "fairy":
                    effective * 2
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ground":
                if active2_type2 == "grass":
                    effective/2
                elif active2_type2 == "fire":
                    effective*2
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*2
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*2
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*0
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective/2
                elif active2_type2 == "rock":
                    effective*2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective*2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "flying":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective/2
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 2
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*2
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*2
                elif active2_type2 == "rock":
                    effective/2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "psychic":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 2
                elif active2_type2 == "poison":
                    effective*2
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective/2
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 0
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "bug":
                if active2_type2 == "grass":
                    effective*2
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective/2
                elif active2_type2 == "poison":
                    effective/2
                elif active2_type2 == "ground":
                    effective*1
                elif active2_type2 == "flying":
                    effective/2
                elif active2_type2 == "psychic":
                    effective * 2
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective /2
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 2
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective /2
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "rock":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective /2
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective/2
                elif active2_type2 == "flying":
                    effective*2
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*2
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "ghost":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 2
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 2
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective/2
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *0

            elif active_move1["move_type"] == "dragon":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*2
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 0
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "dark":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective/2
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 2
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 2
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective /2
                elif active2_type2 == "steel":
                    effective*1
                elif active2_type2 == "fairy":
                    effective /2
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "steel":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective/2
                elif active2_type2 == "electric":
                    effective/2
                elif active2_type2 == "ice":
                    effective*2
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*2
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 2
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "fairy":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective/2
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 2
                elif active2_type2 == "poison":
                    effective/2
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective*1
                elif active2_type2 == "ghost":
                    effective * 1
                elif active2_type2 == "dragon":
                    effective*2
                elif active2_type2 == "dark":
                    effective * 2
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1

            elif active_move1["move_type"] == "normal":
                if active2_type2 == "grass":
                    effective*1
                elif active2_type2 == "fire":
                    effective*1
                elif active2_type2 == "water":
                    effective*1
                elif active2_type2 == "electric":
                    effective*1
                elif active2_type2 == "ice":
                    effective*1
                elif active2_type2 == "fighting":
                    effective * 1
                elif active2_type2 == "poison":
                    effective*1
                elif active2_type2 == "ground":
                    effective* 1
                elif active2_type2 == "flying":
                    effective*1
                elif active2_type2 == "psychic":
                    effective * 1
                elif active2_type2 == "bug":
                    effective*1
                elif active2_type2 == "rock":
                    effective/2
                elif active2_type2 == "ghost":
                    effective * 0
                elif active2_type2 == "dragon":
                    effective*1
                elif active2_type2 == "dark":
                    effective * 1
                elif active2_type2 == "steel":
                    effective/2
                elif active2_type2 == "fairy":
                    effective * 1
                elif active2_type2 == "normal":
                    effective *1
            
            
            
            
            
            
            
            
            
            if active_move1["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                print(active, "used", active_move1)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move1["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                print(active, "used", active_move1)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move1["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                print(active, "used", active_move1)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            else:
                print("somethings silly")
        elif move_p1 == "attack2":
            if active_move2["move_type"] == active_type1:
                stab= 1.5
            elif active_move2["move_type"] == active_type2:
                stab = 1.5
            else:
                stab = 1
            if active_move2["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                print(active, "used", active_move2)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move2["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                print(active, "used", active_move2)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move2["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                print(active, "used", active_move2)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            else:
                print("somethings silly")
        elif move_p1 == "attack3":
            if active_move3["move_type"] == active_type1:
                stab= 1.5
            elif active_move3["move_type"] == active_type2:
                stab = 1.5
            else:
                stab = 1
            if active_move3["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                
                print(active, "used", active_move3)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move3["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                print(active, "used", active_move3)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move3["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                print(active, "used", active_move3)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            else:
                print("somethings silly")
        elif move_p1 == "attack4":
            if active_move4["move_type"] == active_type1:
                stab= 1.5
            elif active_move4["move_type"] == active_type2:
                stab = 1.5
            else:
                stab = 1
            if active_move4["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                
                print(active, "used", active_move4)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move4["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move4["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                print(active, "used", active_move4)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            elif active_move4["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move4["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                print(active, "used", active_move4)
                print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                active2_hp_stats -= calculation
            else:
                print("somethings silly")
        
        
        if active2_hp_stats >= 0:
            if move_p2 == "attack1":
                if active2_move1["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move1)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move1["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move1)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move1["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                    print(active2, "used", active2_move1)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                else:
                    print("somethings silly")
            elif move_p2 == "attack2":
                if active2_move2["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move2)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move2["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move2)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move2["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                    print(active2, "used", active_move2)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                else:
                    print("somethings silly")
            elif move_p2 == "attack3":
                if active2_move3["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move3)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat*100)), "% to,", active))
                    active_hp_stat -= calculation
                elif active2_move3["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move3)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move3["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                    print(active2, "used", active2_move3)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                else:
                    print("somethings silly")
            elif move_p2 == "attack4":
                if active2_move4["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move4)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                elif active2_move4["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move4["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                    print(active2, "used", active2_move4)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active2)
                    active_hp_stat -= calculation
                elif active2_move4["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move4["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                    print(active2, "used", active2_move4)
                    print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                    active_hp_stat -= calculation
                else:
                    print("somethings silly")
            else:
                print("silly billy")
        
        elif active2_hp_stats <= 0:
            print(active2, "has fainted")
            t1_points += 1
            print("[", t2mon2,"]",  "[", t2mon3,"]", "[", t2mon4,"]", "[", t2mon5,"]", "[", t2mon6, "]")
            faint_p2 = input("Active fainted, Swap to, mon2, mon3, mon4, mon5, mon6")
            if faint_p2 == t2mon2:
                print("Player 2 sent out, ", t2mon2)
                active2, t2mon2 == t2mon2, "*Fainted*" 
            elif faint_p2 == "mon2":
                print("Player 2 sent out, ", t2mon2)
                active2, t2mon2 == t2mon2, "*Fainted*"
            elif faint_p2 == t1mon3:
                print("Player 2 sent out, ", t2mon3)
                active2, t2mon3 == t2mon3, "*Fainted*"
            elif faint_p2 == "mon3":
                print("Player 2 sent out, ", t2mon3)
                active2, t2mon3 == t2mon3, "*Fainted*"
            elif faint_p2 == t1mon4:
                print("Player 2 sent out, ", t2mon4)
                active2, t2mon4 == t2mon4, "*Fainted*"
            elif faint_p2 == "mon4":
                print("Player 2 sent out, ", t2mon4)
                active2, t2mon4 == t2mon4, "*Fainted*"
            elif faint_p2 == t1mon5:
                print("Player 2 sent out, ", t2mon5)
                active2, t2mon5 == t2mon5, "*Fainted*"
            elif faint_p2 == "mon5":
                print("Player 2 sent out, ", t2mon5)               
                active2, t2mon5 == t2mon5, "*Fainted*"
            elif faint_p2 == t1mon6:
                print("Player 2 sent out, ", t2mon6)
                active2, t2mon6 == t2mon6, "*Fainted*"
            elif faint_p2 == "mon6":
                print("Player 2 sent out, ", t2mon6)
                active2, t2mon6 == t2mon6, "*Fainted*"
            else:
                print("nope")
        
        if active_hp_stat <= 0:
            print(active, "has fainted")
            t2_points += 1
            print("[", t1mon2,"]",  "[", t1mon3,"]", "[", t1mon4,"]", "[", t1mon5,"]", "[", t1mon6, "]")
            faint_p1 = input("Active fainted, Swap to, mon2, mon3, mon4, mon5, mon6")
            if faint_p1 == t1mon2:
                print("Player 1 sent out, ", t1mon2)
                active, t1mon2 == t1mon2, "*Fainted*" 
            elif faint_p1 == "mon2":
                print("Player 1 sent out, ", t1mon2)
                active, t1mon2 == t1mon2, "*Fainted*"
            elif faint_p1 == t1mon3:
                print("Player 1 sent out, ", t1mon3)
                active, t1mon3 == t1mon3, "*Fainted*"
            elif faint_p1 == "mon3":
                print("Player 1 sent out, ", t1mon3)
                active, t1mon3 == t1mon3, "*Fainted*"
            elif faint_p1 == t1mon4:
                print("Player 1 sent out, ", t1mon4)
                active, t1mon4 == t1mon4, "*Fainted*"
            elif faint_p1 == "mon4":
                print("Player 1 sent out, ", t1mon4)
                active, t1mon4 == t1mon4, "*Fainted*"
            elif faint_p1 == t1mon5:
                print("Player 1 sent out, ", t1mon5)
                active, t1mon5 == t1mon5, "*Fainted*"
            elif faint_p1 == "mon5":
                print("Player 1 sent out, ", t1mon5)               
                active, t1mon5 == t1mon5, "*Fainted*"
            elif faint_p1 == t1mon6:
                print("Player 1 sent out, ", t1mon6)
                active, t1mon6 == t1mon6, "*Fainted*"
            elif faint_p1 == "mon6":
                print("Player 1 sent out, ", t1mon6)
                active, t2mon6 == t1mon6, "*Fainted*"
            else:
                print("nope")

    

    elif faster_mon == 2:
        
        if move_p2 == "switch2":
            active2, t2mon2 == t2mon2, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon2)
        elif move_p2 == "switch3":
            active2, t2mon3 == t2mon3, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon3)
        elif move_p2 == "switch4":
            active2, t2mon4 == t2mon4, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon4)
        elif move_p2 == "switch5":
            active2, t2mon5 == t2mon5, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon5)
        elif move_p2 == "switch6":
            active2, t2mon6 == t2mon6, active2
            print("Player 2 withdrew,", active2, ", Go,", t2mon6)

        if move_p1 == "switch2":
            active, t1mon2 == t1mon2, active
            print("Player 1 withdrew,", active, ", Go,", t1mon2)
        elif move_p1 == "switch3":
            active, t1mon3 == t1mon3, active
            print("Player 1 withdrew,", active, ", Go,", t1mon3)
        elif move_p1 == "switch4":
            active, t1mon4 == t1mon4, active
            print("Player 1 withdrew,", active, ", Go,", t1mon4)
        elif move_p1 == "switch5":
            active, t1mon5 == t1mon5, active
            print("Player 1 withdrew,", active, ", Go,", t1mon5)
        elif move_p1 == "switch6":
            active, t1mon6 == t1mon6, active
            print("Player 1 withdrew,", active, ", Go,", t1mon6)

        if move_p2 == "attack1":
            if active2_move1["move_type"] == active2_type1:
                stab= 1.5
            elif active2_move1["move_type"] == active2_type2:
                stab = 1.5
            else:
                stab = 1
            if active2_move1["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move1)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move1["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move1)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move1["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                print(active2, "used", active2_move1)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            else:
                    print("somethings silly")
        elif move_p2 == "attack2":
            if active2_move2["move_type"] == active2_type1:
                stab= 1.5
            elif active2_move2["move_type"] == active2_type2:
                stab = 1.5
            else:
                stab = 1
            if active2_move2["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move2)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move2["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move2)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move2["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move2["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                print(active2, "used", active_move2)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            else:
                print("somethings silly")
        elif move_p2 == "attack3":
            if active2_move3["move_type"] == active2_type1:
                stab= 1.5
            elif active2_move3["move_type"] == active2_type2:
                stab = 1.5
            else:
                stab = 1
            if active2_move3["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move3)
                print(active2, "does,",(math.floor((calculation/active_hp_stat*100)), "% to,", active))
                active_hp_stat -= calculation
            elif active2_move3["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move3)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move3["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move3["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                print(active2, "used", active2_move3)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            else:
                print("somethings silly")
        elif move_p2 == "attack4":
            if active2_move4["move_type"] == active2_type1:
                stab= 1.5
            elif active2_move4["move_type"] == active2_type2:
                stab = 1.5
            else:
                stab = 1
            if active2_move4["dmg_type"] == "physical":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move1["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move4)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            elif active2_move4["dmg_type"] == "special":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move4["power"]*(float(active2_spa_stats)/float(active_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    
                print(active2, "used", active2_move4)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active2)
                active_hp_stat -= calculation
            elif active2_move4["dmg_type"] == "status":
                calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active2_move4["power"]*(float(active2_atk_stats)/float(active_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    
                print(active2, "used", active2_move4)
                print(active2, "does,",(math.floor((calculation/active_hp_stat)*100)), "% to,", active)
                active_hp_stat -= calculation
            else:
                print("somethings silly")
        

        if active2_hp_stats >= 0:
            if move_p1 == "attack1":
                if active_move1["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                    print(active, "used", active_move1)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move1["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                    print(active, "used", active_move1)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move1["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                    print(active, "used", active_move1)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                else:
                    print("somethings silly")
            elif move_p1 == "attack2":
                if active_move2["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                    print(active, "used", active_move2)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move2["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                    print(active, "used", active_move2)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move2["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move2["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                    print(active, "used", active_move2)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                else:
                    print("somethings silly")
            elif move_p1 == "attack3":
                if active_move3["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                
                    print(active, "used", active_move3)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move3["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                    print(active, "used", active_move3)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move3["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move3["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                    print(active, "used", active_move3)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                else:
                    print("somethings silly")
            elif move_p1 == "attack4":
                if active_move4["dmg_type"] == "physical":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move1["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective))
                
                    print(active, "used", active_move4)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move4["dmg_type"] == "special":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move4["power"]*(float(active_spa_stats)/float(active2_spd_stats))/50.0)+2.0)*role*stab)*effective))
                
                    print(active, "used", active_move4)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                elif active_move4["dmg_type"] == "status":
                    calculation = ((math.floor(math.floor(((((2.0*50.0)/5.0)+2.0)*active_move4["power"]*(float(active_atk_stats)/float(active2_def_stats))/50.0)+2.0)*role*stab)*effective)*0)
                
                    print(active, "used", active_move4)
                    print(active, "does,",(math.floor((calculation/active2_hp_stats)*100)), "% to,", active2)
                    active2_hp_stats -= calculation
                else:
                    print("somethings silly")
            else:
                print("silly billy")

        elif active2_hp_stats <= 0:
            print(active, "has fainted")
            t2_points += 1
            print("[", t1mon2,"]",  "[", t1mon3,"]", "[", t1mon4,"]", "[", t1mon5,"]", "[", t1mon6, "]")
            faint_p1 = input("Active fainted, Swap to, mon2, mon3, mon4, mon5, mon6")
            if faint_p1 == t1mon2:
                print("Player 1 sent out, ", t1mon2)
                active, t1mon2 == t1mon2, "*Fainted*" 
            elif faint_p1 == "mon2":
                print("Player 1 sent out, ", t1mon2)
                active, t1mon2 == t1mon2, "*Fainted*"
            elif faint_p1 == t1mon3:
                print("Player 1 sent out, ", t1mon3)
                active, t1mon3 == t1mon3, "*Fainted*"
            elif faint_p1 == "mon3":
                print("Player 1 sent out, ", t1mon3)
                active, t1mon3 == t1mon3, "*Fainted*"
            elif faint_p1 == t1mon4:
                print("Player 1 sent out, ", t1mon4)
                active, t1mon4 == t1mon4, "*Fainted*"
            elif faint_p1 == "mon4":
                print("Player 1 sent out, ", t1mon4)
                active, t1mon4 == t1mon4, "*Fainted*"
            elif faint_p1 == t1mon5:
                print("Player 1 sent out, ", t1mon5)
                active, t1mon5 == t1mon5, "*Fainted*"
            elif faint_p1 == "mon5":
                print("Player 1 sent out, ", t1mon5)               
                active, t1mon5 == t1mon5, "*Fainted*"
            elif faint_p1 == t1mon6:
                print("Player 1 sent out, ", t1mon6)
                active, t1mon6 == t1mon6, "*Fainted*"
            elif faint_p1 == "mon6":
                print("Player 1 sent out, ", t1mon6)
                active, t2mon6 == t1mon6, "*Fainted*"
            else:
                print("nope")
        
        if active_hp_stat <= 0:
            print(active2, "has fainted")
            t1_points += 1
            print("[", t2mon2,"]",  "[", t2mon3,"]", "[", t2mon4,"]", "[", t2mon5,"]", "[", t2mon6, "]")
            faint_p2 = input("Active fainted, Swap to, mon2, mon3, mon4, mon5, mon6")
            if faint_p2 == t2mon2:
                print("Player 2 sent out, ", t2mon2)
                active2, t2mon2 == t2mon2, "*Fainted*" 
            elif faint_p2 == "mon2":
                print("Player 2 sent out, ", t2mon2)
                active2, t2mon2 == t2mon2, "*Fainted*"
            elif faint_p2 == t1mon3:
                print("Player 2 sent out, ", t2mon3)
                active2, t2mon3 == t2mon3, "*Fainted*"
            elif faint_p2 == "mon3":
                print("Player 2 sent out, ", t2mon3)
                active2, t2mon3 == t2mon3, "*Fainted*"
            elif faint_p2 == t1mon4:
                print("Player 2 sent out, ", t2mon4)
                active2, t2mon4 == t2mon4, "*Fainted*"
            elif faint_p2 == "mon4":
                print("Player 2 sent out, ", t2mon4)
                active2, t2mon4 == t2mon4, "*Fainted*"
            elif faint_p2 == t1mon5:
                print("Player 2 sent out, ", t2mon5)
                active2, t2mon5 == t2mon5, "*Fainted*"
            elif faint_p2 == "mon5":
                print("Player 2 sent out, ", t2mon5)               
                active2, t2mon5 == t2mon5, "*Fainted*"
            elif faint_p2 == t1mon6:
                print("Player 2 sent out, ", t2mon6)
                active2, t2mon6 == t2mon6, "*Fainted*"
            elif faint_p2 == "mon6":
                print("Player 2 sent out, ", t2mon6)
                active2, t2mon6 == t2mon6, "*Fainted*"
            else:
                print("nope")
    
    print(' ')
    print(' ')
    print(' ')
    turn_num += 1













