# Written for GD Demon Ladder
# by RFMX (c) 2021

# This code is to obtain data from the gdbrowser.com API
# Colon exports data in the APi as beautiful JSON
#   so we can have fun dealing with stuff
# [ - ] wrote a code before for the same purpose
# but they use C++ and don't add any comment whatsoever :(
# I cannot decipher what is going on and the program is quite easy anyways
# so I do this myself with my limited Python knowledge

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
import requests
# requests is a very human-friendly HTTP library
# best for noobs like me

# ** Ask for obtaining demons data or insanes data **
print('gdl> Do you want to obtain data for demons or insanes?')
print('1 for demons, 2 for insanes:', end=' ')
while True:
    difficulty = int(input())
    if (difficulty == 1): # demon
        print('gdl> This program will obtain DEMON levels data.')
        break
    elif (difficulty == 2): # insane
        print('gdl> This program will obtain INSANE levels data.')
        break
    else:
        print('gdl> This is not a valid input. Enter again:', end=' ')

# ** Ask for which pages to copy **
print('gdl> Starting page: (0 is first page)', end=' ') # prompt
pagestart = int(input()) # ask for input and store as integer
print('gdl> Ending page:', end=' ')
pageend = int(input())
    # This is made so that I can manually enter the pages
    #   without painstakingly obtain info from the JSON file
    #   through the program

# ** Prompt to delete existing levels.json **
print('gdl> Would you wish to delete the current JSON file?')
print('(Y/N, Y if any other response is given)', end=' ')
boolstr = input()
if boolstr != 'N': # initiates deletion unless N is given
    fileedit = open("levels.json","w",encoding="utf-8")
    fileedit.write('')
    fileedit.close()

# ** Response for user input **
print('gdl> Obtaining data from page ' + str(pagestart) + ' to ' + str(pageend))

############# get serious backdoor moment #############

# ** Obtain data from page pagestart to page pageend **

# * open file for editing *
fileedit = open("levels.json","a",encoding="utf-8")
fileedit.write('[')
    # I'll be removing the first [ in the loop so I'll need to add that

for i in range(pagestart, pageend + 1):
    # * request from gdbrowser *
    print('gdl> Requesting for page ' + str(i), end='') # response

    # * setup for url *
    if difficulty == 1:
        url = 'https://gdbrowser.com/api/search/*?diff=-2&type=recent&page=' + str(i)
    elif difficulty == 2:
        url = 'https://gdbrowser.com/api/search/*?diff=5&starred=1&type=recent&page=' + str(i)
    else:
        print('gdl> Bad difficulty setting. Please contact author for this.')
        print('gdl> Requests will now stop.')
        break

    leveldata = requests.get(url) # request from website
    leveltext = leveldata.text
        # obtained data is not human-readable so need to convert
        # I chose to use a new var to store the original data

    # * detect gdbrowser error *
    if leveltext == '-1':
        print('\ngdl> Bad response from gdbrowser detected.')
        print('gdl> Requests will now stop.')
        break # stop requesting new data

    # * edit string to suit JSON format *
    leveltext = leveltext[1:-2] # slice string which removes the []s
    if i != pageend: leveltext = leveltext + ',' # adds the missing comma

    # * write into file *
    fileedit.write(leveltext)
    print('\r', end='')

fileedit.write('\n]') # same thing as the [ but at the end
fileedit.close()
if leveltext != '-1': print('\ngdl> Requests finished.')

############# end of get serious backdoor moment #############

# ** End prompt **
print('gdl> Check levels.json for output.')
print('gdl> Ending program.')
