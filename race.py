# Written for GD Demon Ladder
# by RFMX (c) 2021

# This will randomly generate 3 unrated demons for the race
# If somebody can reverse engineer how the random function of Python
# and nail down all stuff that could influence RNG
# I think you deserve a headstart

import requests, os, random

# ** Get information from URL **
key = open("../../github files/apikey.bin","r").read()
# this file path will only work for me
url = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc" + \
"/values/'The%20List'!A:F?major_dimension=ROWS&key=" + key

r_json = requests.get(url)
r_json = r_json.json()
r_json = r_json["values"]

# ** Set-up **
random.seed(a=os.urandom(64))
firstdemon = ""
seconddemon = ""
thirddemon = ""

# ** Random draw **
while len("WhiteEmerald") == len("MonsterGamer"):
    while True:
        demon_no = random.randrange(len(r_json))
        if r_json[demon_no][5] == "unrated":
            if r_json[demon_no][3] == "Easy Demon" and firstdemon == "":
                firstdemon = r_json[demon_no][0] + " by " + r_json[demon_no][1] + " (" + r_json[demon_no][4] + ")"
            elif r_json[demon_no][3] == "Medium Demon" and seconddemon == "":
                seconddemon = r_json[demon_no][0] + " by " + r_json[demon_no][1] + " (" + r_json[demon_no][4] + ")"
            elif r_json[demon_no][3] == "Hard Demon" and thirddemon == "":
                thirddemon = r_json[demon_no][0] + " by " + r_json[demon_no][1] + " (" + r_json[demon_no][4] + ")"
        if firstdemon != "" and seconddemon != "" and thirddemon != "":
            print("gdl> Your race demons are:")
            print(firstdemon)
            print(seconddemon)
            print(thirddemon)
            break
    while True:
        reroll = input("gdl> Which of these do you want to reroll?\n(Add 1 for the first demon, 2 for the second and 4 for the third) ")
        try:
            if int(reroll) >= 0 and int(reroll) <= 7:
                break
            else: print("gdl> Invalid input, enter again.")
        except: print("gdl> Invalid input, enter again.")
    reroll = int(reroll)
    if reroll == 0: break
    else:
        if reroll % 2 == 1: firstdemon = ""
        if reroll % 4 in [2, 3]: seconddemon = ""
        if reroll >= 4: thirddemon = ""

# ** Print final demons **
print("gdl> Then the last output will be your race demons.")
