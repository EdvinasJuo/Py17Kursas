#Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių, kuris tikrins po viena kombinaciją,
# pradedant 0000, ir sustos, kai pin kodas bus teisingas. Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau.
# Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu,
# kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų
# 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu.
# Sugalvokite, kaip apeiti šią problemą :).#

def finding_pincode():
    count = 1
    while True:
        yield f'{count:04}'
        count += 1

generator = finding_pincode()

secret_pincode = '0549'

for x in range(9999):
    pincode = next(generator)
    print(pincode)
    if pincode == secret_pincode:
        print(f'PIN is: {pincode}')
        break