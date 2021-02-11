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
    url = 'https://gdbrowser.com/api/search/*?diff=-2&page=' + str(i)
    # setup for url
    leveldata = requests.get(url) # request from website
    leveltext = leveldata.text
    # obtained data is not human-readable so need to convert
    # I chose to use a new var to store the original data
    if leveltext == '-1': # if gdbrowser go wonky
        print('\ngdl> Bad response from gdbrowser detected.')
        print('gdl> Exiting loop.')
        break # stop requesting new data
    # * edit string to suit JSON format*
    leveltext = leveltext[1:-2] # slice string which removes the []s
    if i != pageend: leveltext = leveltext + ',' # adds the missing comma
    # * write into file *
    fileedit.write(leveltext)
    print('\r', end='')

fileedit.write('\n]') # same thing as the [ but at the end
fileedit.close()

############# end of get serious backdoor moment #############

# End of requesting prompt
if leveltext != '-1': print('\ngdl> Requests finished.')
print('gdl> Check levels.json for output.')
print('gdl> Ending program.')
