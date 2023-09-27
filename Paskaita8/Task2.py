import statistics

# • Sukurtų sąrašą iš skaičių nuo 0 iki 50
sarasas = list(range(0,51))

# • Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
multiply_by_10 = [x * 10 for x in sarasas]
print(f"Padauginti skaiciai is 10: {multiply_by_10}")

# • Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
divided_by_7 = [x for x in sarasas if x % 7 == 0]
print(f"Skaiciai kurie dalinasi is 7: {divided_by_7}")

# • Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
raise_by_square = [x ** 2 for x in sarasas]
print(f"Skaiciai pakelti kvadratu: {raise_by_square}")

# • Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
print(f"Skaiciu pakeltu kvadratu suma: {sum(raise_by_square)}")
print(f"Skaiciu pakeltu kvadratu maziausias skaicius: {min(raise_by_square)}")
print(f"Skaiciu pakeltu kvadratu didziausias skaicius: {max(raise_by_square)}")
print(f"Skaiciu pakeltu kvadratu vidurkis: {statistics.mean(raise_by_square)}")
print(f"Skaiciu pakeltu kvadratu mediana: {statistics.median(raise_by_square)}")

# • Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
raise_by_square.sort(reverse=True)
print(f"Sarasa atbulai: {raise_by_square}")
