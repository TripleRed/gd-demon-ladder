# Written for GD Demon Ladder
# by RFMX (c) 2021

# This code is to obtain data from the gdbrowser.com API
# Colon exports data in the APi as beautiful JSON
#   so we can have fun dealing with stuff
# [ - ] wrote a code before for the same purpose
# but they use C++ and don't add any comment whatsoever :(
# I cannot decipher what is going on and the program is quite easy
# so I do this myself with my limited Python knowledge

# Setup
import json, csv, requests

# Ask for which pages to copy
print('gdl> Starting page: (0 is first page)', end=' ')
pagestart = int(input())
print('gdl> Ending page:', end=' ')
pageend = int(input())
# This is made so that I manually enter the pages
#   without painstakingly obtain info from the JSON file
#   through the program

# Prompt to delete existing levels.json
print('gdl> Would you wish to delete the current JSON file?')
print('(Y/N, Y if any other response is given)', end=' ')
boolstr = input()
if boolstr != 'N': # initiates deletion unless N is given
    fileedit = open("levels.json","w",encoding="utf-8")
    fileedit.write('')
    fileedit.close()

# Response
print('gdl> Obtaining data from page ' + str(pagestart) + ' to ' + str(pageend))

# Obtain data from page pagestart to page pageend
fileedit = open("levels.json","a",encoding="utf-8")
for i in range(pagestart, pageend + 1):
    print('gdl> Requesting for page ' + str(i), end='')
    url = 'https://gdbrowser.com/api/search/*?diff=-2&page=' + str(i)
    leveldata = requests.get(url)
    leveltext = leveldata.text
    if leveltext == '-1':
        print('\ngdl> Bad response from gdbrowser detected.')
        print('gdl> Exiting loop.')
        break
    fileedit.write(leveltext)
    print('\r', end='')
fileedit.close()

# End of requesting prompt
if leveltext != '-1': print('\ngdl> Requests finished.')
