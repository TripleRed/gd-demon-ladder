# Written for GD Demon Ladder
# by RFMX (c) 2021

# This code aims to compile a list of demons which fit the filters
# and show it to the user
# Brython seems to only use Ajax call but IDC
# as long as I can make it work in normal Python, I can port it to Brython

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
import requests, sys
key = input('gdl> API Key? ')

# ** Ask for filters **
tiermin = input('gdl> Level tier minimum? ')
tiermax = input('gdl> Level tier maximum? ')
official_diff = input('gdl> Official difficulty? (0 to 5, 0 is official level, 5 is Extreme) ')
name = input('gdl> Level name? ')
recent = input('gdl> Invert list to make it sort by recent? (0/1) ')
page = input('gdl> Page number? ')
# Selecting a page does not makes much sense in a program
# but it will when it is ported to Brython

# ** URL request **
url = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/'The List'!A:G?majorDimension=COLUMNS&key=" + key
urlresponse = requests.get(url) # HTTP request
urlresponse = urlresponse.json() # convert to json
r_json = urlresponse['values']

# ** Filter for levels **
# * setup list *
result = []
i = 1
while i < len(r_json[4]):
    result.append(i)
    i += 1

# * Minimum tier *
if tiermin != '':
    try:
        tiermin = int(tiermin)
    except: tiermin = float(tiermin)
    list = []
    try:
        while True:
            check_list = result.pop(0)
            if isinstance(tiermin, int):
                try:
                    check_try = int(r_json[5][check_list])
                except: check_try = 0
            elif isinstance(tiermin, float):
                try:
                    check_try = float(r_json[6][check_list])
                except: check_try = 0.0
            if tiermin <= check_try: list.append(check_list) # comparison check
    except: pass
    try:
        while True:
            result.append(list.pop(0))
    except: pass

# * Maximum tier *
if tiermax != '':
    try:
        tiermax= int(tiermax)
    except: tiermax = float(tiermax)
    list = []
    try:
        while True:
            check_list = result.pop(0)
            if isinstance(tiermax, int):
                try:
                    check_try = int(r_json[5][check_list])
                except: check_try = 0
            elif isinstance(tiermax, float):
                try:
                    check_try = float(r_json[6][check_list])
                except: check_try = 0.0
            if tiermax >= check_try: list.append(check_list) # comparison check
    except: pass
    try:
        while True:
            result.append(list.pop(0))
    except: pass

# * Official difficulty *
if official_diff != '':
    official_diff = int(official_diff)
    list = []
    try:
        while True:
            check_list = result.pop(0)
            try:
                check_try = (r_json[3][check_list])
                if check_try == 'Official Level':
                    check_try = 0
                elif check_try == 'Easy Demon':
                    check_try = 1
                elif check_try == 'Medium Demon':
                    check_try = 2
                elif check_try == 'Hard Demon':
                    check_try = 3
                elif check_try == 'Insane Demon':
                    check_try = 4
                elif check_try == 'Extreme Demon':
                    check_try = 5
            except: check_try = -1
            if official_diff == check_try: list.append(check_list) # comparison check
    except: pass
    try:
        while True:
            result.append(list.pop(0))
    except: pass

# * Level name *
if name != '':
    name = name.lower()
    list = []
    try:
        while True:
            check_list = result.pop(0)
            try:
                check_try = r_json[0][check_list].lower()
            except: check_try = ''
            if name in check_try: list.append(check_list) # comparison check
    except: pass
    try:
        while True:
            result.append(list.pop(0))
    except: pass

# ** Listing results **

# * print stuff *
try:
    recent = -1 * int(recent)
except: recent = 0
try:
    i = -10 * int(page)
except: i = 0
noresults = True

print('gdl> Search results:')
try:
    while True:
        resultpop = result.pop(recent)
        if i >= 10:
            break
        elif i >= 0:
            noresults = False
            print(r_json[0][resultpop], end=' by ')
            print(r_json[1][resultpop], end=' (')
            print(r_json[4][resultpop], end=')\n')
        i += 1
except: pass

if noresults:
    print('No results.')
