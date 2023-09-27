# Parašyti programą, kuri:
# • Leistų vartotojui įvesti pradžios ir pabaigos datą
# • Suskaičiuotų kiek praėjo sekundžių tarp datų
import datetime

while True:
    input_start_date = input("Iveskite pradzios data (yyyy-MM-dd): ")
    input_end_date = input("Iveskite pabaigos data (yyyy-MM-dd): ")
    try:
        start_date = datetime.datetime.strptime(input_start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(input_end_date, "%Y-%m-%d")

        difference = end_date - start_date
        print(f"Laiko skirtumas sekundemis yra: {difference.total_seconds()}")
        break
    except ValueError:
        print("Bloga ivestis. Bandykite dar karta.")
    except TypeError:
        print("Bloga ivestis. Bandykite dar karta.")
