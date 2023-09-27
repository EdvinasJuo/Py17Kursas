# INTEGER
number1 = 5
number2 = float(10.4)

sum = number1 + number2

sum1 = number1 ** 2

print(f'Rezultatas yra : {sum}')
print(f'Rezultatas yra : {sum1}')

# BOOLEAN

x = True
y = False

result = 1 < 2 and 1 < 5

print(f'Boolean rezultatas yra : {result}')

# STRING/CHAR OPERATORS

name = "Edvinas Juodeika"

print(f'Vardas : {name[0]}') # [0] - nurodomas indexas kuria raide paimti
print(name[2:8]) # [2:8] nurodomos indexas nuo kurios iki kurios raides paimti, arba antro indexo nenurodzius paims viska iki pat galo

print(name[::-1]) # Spausdinama is kitos puses

print(name.split()) # Isskaido kiekviena zodi i List

print(name.upper()) # Lower - mazosios, Upper - didziosios

print(name.replace('E', 'P')) # Pakeicia is senos i nauja raide arba zodi

word1 = "Labas"
word2 = "Pasauli"

sentence = word1 + " " + word2
print(sentence)

input_number1 = int(input("Iveskite pirmaji skaiciu: "))
input_number2 = float(input("Iveskite antraji skaiciu: "))

print("Jusu skaiciu suma: ", input_number1 + input_number2)

word3 = "'Labas'"
print(word3)

multi_line_string = '''
Asdasdsad
asdsadas.
asdasdasd
asdsadasd.asdasdasd
asdsa
'''