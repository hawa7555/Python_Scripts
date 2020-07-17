import json

#person = { "364721f8": {"name": "Bob", "inTime": 1563256000, "outTime": 1673284000 }, "76d72af3": {"name": "Harshal", "inTime": 1563256010, "outTime": 1763284020 } }
#print(person)
#json_data = json.dumps(person)
#print(json_data)

#person_dict = json.loads(person_json)
#print(person_dict['364721f8'])

file = open('data.json', 'r')
#file.write(json_data)
dataRead = json.load(file)
print( dataRead['364721f8']['outTime'] )
file.close()
      

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
#print( person_dict)

# Output: ['English', 'French']
#print(person_dict['languages'])

