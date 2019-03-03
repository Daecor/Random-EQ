import clr
import sys
import json
import os
import ctypes
import codecs

#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Random EQ"
Website = "https://www.twitch.tv/daecor"
Description = "Rolls Random EQ character in chat."
Creator = "Daecor"
Version = "1.0.0.0"


#---------------------------
#   Define Global Variables
#---------------------------
configFile = "config.json"
settings = {}

def ScriptToggled(state):
	return
#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"liveOnly": False,
			"command": "!eqchar",
			"permission": "Everyone",
		}

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):
    if data.IsChatMessage() and data.GetParam(0).lower() == settings["command"] and Parent.HasPermission(data.User, settings["permission"], "") and ((settings["liveOnly"] and Parent.IsLive()) or (not settings["liveOnly"])):
        eqRace = Parent.GetRandom(1, 14)
        eqClass = "FixMe"
        stats = "fix stats"
        username = data.UserName
        if eqRace == 1:
            eqRace = "Barbarian"
            eqClass = Parent.GetRandom(1, 4)
            if eqClass == 1:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Shaman"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 2:
            eqRace = "Dark Elf"
            eqClass = Parent.GetRandom(1, 9)
            if eqClass == 1:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass ="Enchanter"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Magician"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Necromancer"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 6:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 7:
                eqClass = "Warrior"
                stats = RollStats(25)
            elif eqClass == 8:
                eqClass = "Wizard"
                stats = RollStats(30)
        elif eqRace == 3:
            eqRace = "Dwarf"
            eqClass= Parent.GetRandom(1, 5)
            if eqClass == 1:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Paladin"
                stats = RollStats(20)
            elif eqClass == 3:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 4:
            eqRace = "Erudite"
            eqClass = Parent.GetRandom(1, 8)
            if eqClass == 1:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Enchanter"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Magician"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Necromancer"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Paladin"
                stats = RollStats(20)
            elif eqClass == 6:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 7:
                eqClass = "Wizard"
                stats = RollStats(30)
        elif eqRace == 5:
            eqRace = "Gnome"
            eqClass = Parent.GetRandom(1, 8)
            if eqClass == 1:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Enchanter"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Magician"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Necromancer"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 6:
                eqClass = "Warrior"
                stats = RollStats(25)
            elif eqClass == 7:
                eqClass = "Wizard"
                stats = RollStats(30)
        elif eqRace == 6:
            eqRace = "Half-Elf"
            eqClass= Parent.GetRandom(1, 7)
            if eqClass == 1:
                eqClass = "Bard"
                stats = RollStats(25)
            elif eqClass == 2:
                eqClass = "Druid"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Paladin"
                stats = RollStats(20)
            elif eqClass == 4:
                eqClass = "Ranger"
                stats = RollStats(20)
            elif eqClass == 5:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 6:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 7:
            eqRace = "Halfling"
            eqClass = Parent.GetRandom(1, 5)
            if eqClass == 1:
                eqClass = "Druid"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 8:
            eqRace = "High Elf"
            eqClass = Parent.GetRandom(1, 6)
            if eqClass == 1:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 2:
                eqClass = "Enchanter"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Magician"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Paladin"
                stats = RollStats(20)
            elif eqClass == 5:
                eqClass = "Wizard"
                stats = RollStats(30)
        elif eqRace == 9:
            eqRace = "Human"
            eqClass = Parent.GetRandom(1, 14)
            if eqClass == 1:
                eqClass = "Bard"
                stats = RollStats(25)
            elif eqClass == 2:
                eqClass = "Cleric"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Druid"
                stats = RollStats(30)
            elif eqClass == 4:
                eqClass = "Enchanter"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Magician"
                stats = RollStats(30)
            elif eqClass == 6:
                eqClass = "Monk"
                stats = RollStats(20)
            elif eqClass == 7:
                eqClass = "Necromancer"
                stats = RollStats(30)
            elif eqClass == 8:
                eqClass = "Paladin"
                stats = RollStats(20)
            elif eqClass == 9:
                eqClass = "Ranger"
                stats = RollStats(20)
            elif eqClass == 10:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 11:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 12:
                eqClass = "Warrior"
                stats = RollStats(25)
            elif eqClass == 13:
                eqClass = "Wizard"
                stats = RollStats(30)
        elif eqRace == 10:
            eqRace = "Iksar"
            eqClass = Parent.GetRandom(1, 6)
            if eqClass == 1:
                eqClass = "Monk"
                stats = RollStats(20)
            elif eqClass == 2:
                eqClass = "Necromancer"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 4:
                eqClass = "Shaman"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 11:
            eqRace = "Ogre"
            eqClass = Parent.GetRandom(1, 4)
            if eqClass == 1:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 2:
                eqClass = "Shaman"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 12:
            eqRace = "Troll"
            eqClass = Parent.GetRandom(1, 4)
            if eqClass == 1:
                eqClass = "Shadow Knight"
                stats = RollStats(20)
            elif eqClass == 2:
                eqClass = "Shaman"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Warrior"
                stats = RollStats(25)
        elif eqRace == 13:
            eqRace = "Wood Elf"
            eqClass = Parent.GetRandom(1, 6)
            if eqClass == 1:
                eqClass = "Bard"
                stats = RollStats(25)
            elif eqClass == 2:
                eqClass = "Druid"
                stats = RollStats(30)
            elif eqClass == 3:
                eqClass = "Ranger"
                stats = RollStats(20)
            elif eqClass == 4:
                eqClass = "Rogue"
                stats = RollStats(30)
            elif eqClass == 5:
                eqClass = "Warrior"
                stats = RollStats(25)
        outputMessage = "@" + str(username) + " rolled a " + " " + str(eqRace) + ", " + str(eqClass) + ". " + "With the stat distribution of" + " " + str(stats)
        Parent.SendStreamMessage(outputMessage)
    return

def RollStats(bonus):
    remainder = int(bonus)
    temp = 0
    temp2 = 0
    rolledStats = "FixMe"
    tStr = 0
    tSta = 0
    tAgi = 0
    tDex = 0
    tWis = 0
    tInt = 0
    tCha = 0
    while remainder >= 1:
        temp = Parent.GetRandom(1, 8)
        temp2 = Parent.GetRandom(1, remainder)
        if temp == 1 and tStr < 25 and (temp2 + tStr) < 26:
            tStr = tStr + temp2
            remainder = remainder - temp2
        elif temp == 2 and tSta < 25 and (temp2 + tSta) < 26:
            tSta = tSta + temp2
            remainder = remainder - temp2
        elif temp == 3 and tAgi < 25 and (temp2 + tAgi) < 26:
            tAgi = tAgi + temp2
            remainder = remainder - temp2
        elif temp == 4 and tDex < 25 and (temp2 + tDex) < 26:
            tDex = tDex + temp2
            remainder = remainder - temp2
        elif temp == 5 and tWis < 25 and (temp2 + tWis) < 26:
            tWis = tWis + temp2
            remainder = remainder - temp2
        elif temp == 6 and tInt < 25 and (temp2 + tInt) < 26:
            tInt = tInt + temp2
            remainder = remainder - temp2
        elif temp == 7 and tCha < 25 and (temp2 + tCha) < 26:
            tCha = tCha + temp2
            remainder = remainder - temp2

    rolledStats = "Str:" + " " + str(tStr) + " " + "Sta:" + " " + str(tSta) + " " + "Agi:" + " " + str(tAgi) + " " + "Dex:" + " " + str(tDex) + " " + "Wis:" + " " + str(tWis) + " " + "Int:" + " " + str(tInt) + " " + "Cha:" + " " + str(tCha) 
   
    return str(rolledStats)




def ReloadSettings(jsonData):
	Init()
	return

def Tick():
    return