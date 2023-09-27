# Parašyti programą, kuri atspausdintų norimą žodį, kas X sekundžių. Programa turi:
# • Gauti sekundes iš vartotojo
# • Spausdinti vartotojo įvesta žodį
# • Įvedus netinkamą sekundžių formatą, programa turi paprašyti įvesti sekundes iš naujo
import time

while True:
    input_seconds = input("Iveskite kas kiek laiko spausdinti jusu zodi arba 'q', kad uzdaryti programa: ")
    try:
        if input_seconds != "q".lower():
            seconds = float(input_seconds)

            input_word = input("Iveskite savo norima zodi: ")
            for i in range(5):
                print(input_word)
                time.sleep(seconds)
        else:
            print("Programa isjungiama")
            break
    except ValueError:
        print("Bloga ivestis. Bandykite dar karta.")
    except KeyboardInterrupt:
        print("Programa baige darba anksciau laiko.")