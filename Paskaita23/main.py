import json
# ------------------------------------------------------------------------------------------
# DUOMENU STRUKTURA KURI JSON DUOMENIS PRISKIRIA KINTAMAJAM
data = '''{
  "student": [ 

     { 
        "id":"01", 
        "name": "Tom", 
        "lastname": "Price" 
     }, 

     { 
        "id":"02", 
        "name": "Nick", 
        "lastname": "Thameson" 
     } 
  ]   
}'''

# data_dict = json.loads(data) # LOADS FUNKCIJA PAKEICIA IS STRING I PYTHON DICTIONARY
# print(data_dict)
# print(type(data_dict))

# ATLIEKAM VEIKSMUS KAIP SU PAPRASTU DICTIONARY
# data_dict['student'][1]['name'] = 'Kyle'
# for student in data_dict['student']:
#     student.update({'gender':'male'})
# print(data_dict)
#---------------------------------------------------------------------------------------
#           .dumps() KONVERTUOJAM I STRING BET JSON FORMATU
# new_json = json.dumps(data_dict, indent=2)
# print(new_json)
#---------------------------------------------------------------------------------------

#           .load() UZLOADINA JSON FAILA ir grazina kaip dictionary
with open('pvz.json', 'r') as file:
    data = json.load(file)

print(data)

#---------------------------------------------------------------------------------------

#           .dump() leidžia įrašyti python žodyną į failą:

with open('example2.json', 'w') as file:
    json.dump(data, file, indent=2, sort_keys=True)
#---------------------------------------------------------------------------------------
