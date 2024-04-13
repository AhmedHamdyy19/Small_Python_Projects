import json


# python string (valid json)
company ='''
{
    "people": [
        {
           "name": "John Smith",
           "phone": "615-555-7164",
           "emails": ["john.smith@gmail.com", "js@hotmail.com"],
           "has_license": false
            
        },
        {
            "name": "Michael Biden",
            "phone": "777-612-9162",
            "emails": ["michael.biden@gmail.com", "mb@hotmail.com"],
            "has_license": true
        }
    ],
    "money":
        {
            "amount": "10M",
            "isCash": false
        }
}
'''
#----------------------------------------------------------------------------

data = json.loads(company)     # load string
for person in data["people"]:
    print("name is {}, phone is {}".format(person["name"], person["phone"]))

for person in data["people"]:
    del person["has_license"]
    
new_str = json.dumps(data, indent=2, sort_keys=True)  # dump string

#----------------------------------------------------------------------------

data["Factory"] = [{"name": "EGY_iron", "location": "Giza"}, \
                    {"name": "EGI", "location": "Cairo"}]

# write json file
with open("new_json.json", "w") as f:
    json.dump(data, f, indent=2)
    
with open("new_json.json") as f:
    mod_company = json.load(f)
    
#----------------------------------------------------------------------------
#-----------------------------   summary   ----------------------------------
#----------------------------------------------------------------------------
# each {} declare a new json object (json obj --> python dict)
# use loads and dumps when dealing with strings
# use load and dump when dealing with json files
