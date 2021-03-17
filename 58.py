#Question: Please download the json file in the attachment and use Python to add a new employee to the file's content so that the file looks like in the expected output below.

import json
from os import truncate
from pprint import pprint

with open('company1.json', 'r+') as json_file:
    data = json.load(json_file)
    data['employees'].append(dict(firstName = 'Albert', lastName = 'Bert' ))
    # put the cursor to the begining of the file. Curson after reading a file is in the end of the file
    json_file.seek(0)
    json.dump(data,json_file , indent = 4, sort_keys = True) 
    # after writing new dict, cursor is at it's end and simultaneously on the old dict start. Truncate deletes everything after the cursor
    json_file.truncate()