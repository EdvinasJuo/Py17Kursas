amzius = {"Rokas": 20, "Andrius": 34, "Laura": 25}  #Pirma reiksme key antra reiksme Value

print(amzius)
print(amzius["Laura"])  #Spausdina pagal key reiksme

amzius["Paulius"] = 33 #Prideda nauja key ir value
print(amzius)

amzius["Paulius"] = 25 #Pakeiciama reiksme/Value issitraukus key
print(amzius)

del amzius["Rokas"] # del funkcija istrina pagal key reiksme
print(amzius)