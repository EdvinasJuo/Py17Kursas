# Parašyti programą, kuri:
# • Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# • Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# • Metų
# • Mėnesių
# • Dienų
# • Valandų
# • Minučių
# • Sekundžių
# • Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
# Patarimas: naudoti datetime, .days, .total_seconds()
# Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):

import datetime
import math

todays_date = datetime.datetime.today()
days_to_month = 0.03287671
seconds_to_hours = 0.00027778
seconds_to_minutes = 0.01666667

while True:
    input_birthDay = input("Enter your birth day (yyyy-MM-dd HH:MM:ss) : ")
    try:
        birthDay = datetime.datetime.strptime(input_birthDay, "%Y-%m-%d %H:%M:%S")
        years_difference = todays_date - birthDay
        counting_years = years_difference.days / 365
        counting_months = years_difference.days * days_to_month
        counting_days = years_difference.days
        counting_hours = years_difference.total_seconds() * seconds_to_hours
        counting_minutes = years_difference.total_seconds() * seconds_to_minutes
        counting_seconds = years_difference.total_seconds()

        print(f"You are {math.floor(counting_years)} years old.")
        print(f"You are {math.floor(counting_months)} months old.")
        print(f"You are {counting_days} days old.")
        print(f"You are {math.floor(counting_hours)} hours old.")
        print(f"You are {math.floor(counting_minutes)} minutes old.")
        print(f"You are {math.floor(counting_seconds)} seconds old.")
    except ValueError:
        print("Bad input. Try again.")