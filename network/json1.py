# JSON code example using nested dictionaries

import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 740 303 542"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
# print(info)
print('Name: ',info["name"])
