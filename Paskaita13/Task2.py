while True:
    try:
        first_year = int(input("Iveskite pirmuosius metus: "))
        second_year = int(input("Iveskite antruosius metus: "))
        if second_year <= first_year:
            print("Antri metai negali buti lygus arba mazesni uz pirmuosius metus..")
        else:
            print("Keliamuju metu sarasas:")
            for years in range(first_year, second_year):
                if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
                    print(years)
        keep_going = input("Ar norite testi (Y/N): ").upper()
        if keep_going != "Y":
            print("Viso gero!")
            break
    except ValueError:
        print("Bloga ivestis.. bandykite dar karta..")