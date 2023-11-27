import numpy as np

#----------------------------------------------------------------------------------
# SUKURIAMAS VEKTORIUS
# listas = [1, 2, 3, 4, 5]
#
# vector = np.array(listas)
# print(vector)
# print(type(vector))
#
# #NumPy turi ir integruotus, paprastus būdus susikurti masyvą. Skliausteliuose reikia įrašyti start, stop ir step(nebūtina) reikšmes:
# vector2 = np.arange(0, 30, 3)
# print(vector2)
#
# #Sukuria nulini vektoriu kuris sudarytas is 0
# vector3 = np.zeros(10)
# print(vector3)
#
# #Sukuriamas random vectorius
# random_vector = np.random.rand(10)
# print(random_vector)
# #----------------------------------------------------------------------------------
# # SUKURIAMA MATRCIA
#
# listai = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = np.array(listai)
# print(matrix)
#
# #sukurs nuline matrica
# matrix2 = np.zeros((5,5))
# print(matrix2)
#
# #sukurs matrica 6x6 tik per viduri eis po vieneta istryzai.
# matrix3 = np.eye(6)
# print(matrix3)
#
# #sukuriama lygiom dalim vektorius
# vector4 = np.linspace(0,20,16)
# print(vector4)
#
# #Sukuriama random matrica
# random_matrix = np.random.rand(3, 3)
# print(random_matrix)

#----------------------------------------------------------------------------------
# IS VECTORIAUS PASIDAROM I MATRICA
#Sugeneruoja visada tuos pacius skaicius naudojant seed. Jo nenurodzius kiekviena karta automatiskai ima nauja seeda
# np.random.seed(1)
#
# random_vector1 = np.random.randint(100, 200, 64)
# print(random_vector1)
# matrix_from_vector = random_vector1.reshape(8,8)
# print(matrix_from_vector)
#
# print(matrix_from_vector.max()) # MAX REIKSME
# print(matrix_from_vector.min()) # MIN REIKSME
# print(matrix_from_vector.argmax()) # GAUNAME KELINTAS ELEMENTAS YRA MAX
# print(matrix_from_vector.argmin())  # GAUNAME KELINTAS ELEMENTAS YRA MIN
#
#
# # VEKTORIAI
# print(random_vector1[5]) #ISTRAUKIAM SKAICIU PAGAL INDEXA
#
# random_vector1[2:5] = 0 # PAKEICIAM NUO 2 iki 5 REIKSMES = 0
# print(random_vector1)
#
# # MATRCIJOS
# print(matrix_from_vector[1, 4]) # pirmas skaicius - eilute. Antras skaicius = stulpelis
# print(matrix_from_vector[1:3, 4:6])  #

#----------------------------------------------------------------------------------
# MATEMATINES FUNKCIJOS

random_vector = np.random.randint(100, 200, 64)
random_vector2 = random_vector.copy()

print(random_vector)
print("---------------------")
print(random_vector2)
print("---------------------")
print(random_vector + random_vector2)
# print(random_vector - random_vector2)
# print(random_vector * random_vector2)
# print(random_vector / random_vector2)
# print(random_vector / 0)
# print(random_vector + 100) # Prideda 100 prie kiekvieno elemento
print(np.sin(random_vector)) # GRAZINA SINUSA

