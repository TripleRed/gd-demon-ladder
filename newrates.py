# Written for GD Demon Ladder
# by RFMX (c) 2021

# This code will help me generate a JSON that only contains IDs that I need.
# This will be helpful for adding newly rated demons into the list,
# because I just have to lazily copy and paste.

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
import requests

# ** Prompt to delete existing levels.json **
print('gdl> Would you wish to delete the current JSON file?')
print('(Y/N, Y if any other response is given)', end=' ')
boolstr = input()
if boolstr != 'N': # initiates deletion unless N is given
    fileedit = open("levels.json","w",encoding="utf-8")
    fileedit.write('')
    fileedit.close()

# ** Obtain data from ID **

firstitem = True

# * open file for editing *
fileedit = open("levels.json","a",encoding="utf-8")
fileedit.write('[')
    # I'll be removing the first [ in the loop so I'll need to add that

# * The forever loop *
while True:
    # * url setup *
    id_in_question = str(input('gdl> Input ID number (enter nothing to end): '))
    if id_in_question == '':
        print('gdl> End input detected. Exiting.')
        break
    else: print('gdl> Attempting to obtain level data with ID ' + id_in_question)
    url = "https://gdbrowser.com/api/level/" + id_in_question
    leveldata = requests.get(url) # request from website
    leveltext = leveldata.text
    leveljson = leveldata.json()
        # obtained data is not human-readable so need to convert
        # I chose to use a new var to store the original data

    # * detect gdbrowser error *
    if leveltext == '-1':
        print('\ngdl> Bad response from gdbrowser detected.')
        print('gdl> Requests will now stop.')
        break # stop requesting new data

    # * writes the comma for second item onwards *
    if firstitem == False: fileedit.write(',')
    firstitem = False

    # * write into file *
    fileedit.write(leveltext)
    print('gdl> Successfully obtained data for ' + leveljson['name'] + ' by ' + leveljson['author'])

fileedit.write('\n]') # same thing as the [ but at the end
fileedit.close()

############# end of get serious backdoor moment #############

# ** End prompt **
print()
print('gdl> Check levels.json for output.')
print('gdl> Pasting the generated JSON file to https://csvjson.com/json2csv will yield a CSV file.')
print('gdl> This can be opened in Excel as a spreadsheet format.')
print('gdl> Ending program.', end=" ")
input()
