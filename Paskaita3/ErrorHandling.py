# 7/0
# number = int(input("Iveskite skaiciu: "))

# dalinys = 7
# daliklis = 0
# if daliklis == 0:
#     print("Dalyba is 0 negalima")
# else:
#     print(dalinys/daliklis)
#
# print("Toliau vykdoma programa")

#TRY EXECPT

dalinys = 7
daliklis = 1

try:
    print(dalinys/daliklis)
    open("failas.txt")
    skaicius = int(input("Iveskite skaiciu: "))
except ZeroDivisionError:
    print("Dalyba is 0 negalima")
except FileNotFoundError:
    print("Tokio failo nera")
except ValueError:
    print("Ivede ne skaiciu..")
finally:
    print("Tikrai ivyko")

print("Toliau vykdoma programa")

# try:
#     open("failas.txt")
# except:
#     print("Tokio failo nera")
#
# print("Toliau vykdoma programa")
#
# try:
#     skaicius = int(input("Iveskite skaiciu: "))
# except:
#     print("Ivede ne skaiciu..")
#
# print("Toliau vykdoma programa")

# UZDUOTELE  JEIGU IVESTAS NE SKAICIUS

while True:
    try:
        x = int(input("Iveskite skaiciu: "))
        break
    except ValueError:
        print("Ivedete ne skaiiciu. Bandykite dar karta")

print(f"Jusu ivestas skaicius: {x}")