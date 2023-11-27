import numpy as np

# 1. Sukurkite vektorių su skaičiais nuo 1 iki 9
print("-------------1----------------")
vector = np.arange(0,10)
print(vector)

#2. Sukurkite vektorių iš 10 nulių
print("-------------2----------------")
vector2 = np.zeros(10)
print(vector2)

#3. Sukurkite vektorių iš 10 vienetų
print("-------------3----------------")
vector3 = np.ones(10)
print(vector3)

#4. Sukurkite vektorių iš 10 ketvertų
print("-------------4----------------")
vector4 = np.random.randint(4, 5, 10)
print(vector4)

#5. Sukurkite vektorių iš lyginių skaičių nuo 0 iki 100
print("-------------5----------------")
vector5 = np.arange(0, 102, 2)
print(vector5)

#6. Sukurkite matricą iš 25 narių, pradedant 1, baigiant 25. Priskirkite ją kintamąjam
print("-------------6----------------")
listai = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
matrix = np.array(listai)
print(matrix)

#7. Iš matricos ištraukite skaičių 12
print("-------------7----------------")
print(matrix[2,1])

# 8. Iš matricos ištraukite paskutinę eilutę.
print("-------------8----------------")
print(matrix[4, 0:])

# 9. Iš matricos ištraukite submatricą
print("-------------9----------------")
print(matrix[0:3, 0:3])

#10. Iš matricos ištraukite submatricą
print("-------------10----------------")
print(matrix[1:4, 1:5])

# 11. Iš matricos ištraukite submatricą
print("-------------11----------------")
print(matrix[3:5, 0:3])

# 12. Sukurkite vektorių iš 20 atsitiktinių reikšmių nuo 0 iki 1. Priskirkite kintamąjam.
print("-------------12----------------")
vector6 = np.random.rand(20)
print(vector6)

#13. Suraskite didžiausią reikšmę masyve ir jos indeksą.
print("-------------13----------------")
print(vector6.max())
print(vector6.argmax())

#14. Suraskite mažiausią reikšmę ir jos indeksą
print("-------------14----------------")
print(vector6.min())
print(vector6.argmin())

#15. Atspausdinkite šio vektoriaus duomenų tipą
print("-------------15----------------")
print(vector6.dtype)

#16.Sukurkite vektorių iš integer reikšmių nuo 1 iki 100. Priskirkite kintamąjam.
# Iš jo ištraukite visus skaičius, didesnius už 90
print("-------------16----------------")
vector7 = np.arange(1, 101)
print(vector7[vector7 > 90])

#17. Ištraukite iš vektoriaus visus skaičiaus 7 kartotinius
print("-------------17----------------")
sevens = vector7[vector7 % 7 == 0]
print(sevens)

# 18. Sukurkite tokią matricą:
# array([[0.025, 0.05 , 0.075, 0.1  , 0.125, 0.15 , 0.175, 0.2  ],
#        [0.225, 0.25 , 0.275, 0.3  , 0.325, 0.35 , 0.375, 0.4  ],
#        [0.425, 0.45 , 0.475, 0.5  , 0.525, 0.55 , 0.575, 0.6  ],
#        [0.625, 0.65 , 0.675, 0.7  , 0.725, 0.75 , 0.775, 0.8  ],
#        [0.825, 0.85 , 0.875, 0.9  , 0.925, 0.95 , 0.975, 1.   ]])
print("-------------18----------------")
matrix2 = np.arange(0.025, 1.025, 0.025).reshape(5,8)
print(matrix2)


# 19. sukurkite tokią matricą (sveiki sk. nuo 2 iki 1000 iš kurių traukiasi sveika šaknis):
print("-------------19----------------")
matrix3 = np.arange(2, 1000)
result = matrix3[(matrix3 ** 0.5) % 1 == 0].reshape(6,5)
print(result)

#20 BONUS
print("-------------20----------------")
#Sukurkite vektorių iš sveikų sk. nuo 1 iki 100. Priskirkite kintamąjam.
bonus_vector = np.arange(1, 101)

#Sukurkite Python funkciją, kuri tikrina ar parametruose įvestas sk. yra pirminis.
# Jeigu pirminis, grąžina True, jei ne, False.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

vektorize = np.vectorize(is_prime)
pirminiai_skaiciai = bonus_vector[vektorize(bonus_vector)]
print(pirminiai_skaiciai)