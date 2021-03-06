# Written for GD Demon Ladder
# by RFMX (c) 2021

# This code aims to use Google Spreadsheets as a database
# rather than a front-end.
# This code will be copied to repl.it (with the print statements removed)
# and hope that Brython can run this without
# fiddling with too much stuff

# Comments refer to the previous line except for headers, marked with *

# ** Setup **
import requests, sys
key = "" # API key has been deleted for security purposes
wholelist = "'The List'!A:AU"
def url_request(a1notation):
    apiurl = "https://sheets.googleapis.com/v4/spreadsheets/1xaMERl70vzr8q9MqElr4YethnV15EOe8oL1UV9LLljc/values/" + a1notation + "?key=" + key
        # setup API URL
    urlresponse = requests.get(apiurl) # HTTP request
    urlresponse = urlresponse.json() # convert to json
    urlresponse = urlresponse['values']
    return urlresponse

# ** ask for ID **
print('gdl> Enter level ID:', end=' ')
id_search = input()

print('gdl> Printing demon info...')

# ** JSON shenanigans **
# * search for the specific ID *
r_json = url_request("'The List'!E:E")
demon_no = -1
id_array = []
id_array.append(id_search)
try:
    demon_no = r_json.index(id_array)
except:
    print('gdl> No demon with requested ID. Terminating.')
    sys.exit()

#for i in range(len(r_json)):
#    if r_json[i][0] == id_search: demon_no = i
#if demon_no == -1:

# * search for and prints demon information *
row_no = demon_no + 1
row_select = "'The List'!" + str(row_no) + ":" + str(row_no)
r_json = url_request(row_select)
r_json = r_json[0]

print()
print(r_json[0] + ' (' + r_json[4] + ')')
print('created by ' + r_json[1])
print('Song: ' + r_json[2])
print(r_json[3] + ' in-game')
if r_json[5] != "#DIV/0!":
    print('Rated as Tier ' + r_json[5] + ' (' + r_json[6] + ' corr to 2 d.p.)')
    print('Submitted ratings:')
    i = 7
    try:
        while r_json[i] != '':
            print('- Tier ' + r_json[i], end=' ')
            i += 1
            print('by ' + r_json[i])
            i += 1
    except: pass
else: print('Unrated')
print()
