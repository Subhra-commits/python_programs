#JSON code example using nested Lists

import json

data= ''' [
    {
        "id" : "001",
        "name" : "Chuck"
    },
    {
        "id" : "002",
        "name" : "Brent"
    }
]'''

info=json.loads(data)
print(info)
