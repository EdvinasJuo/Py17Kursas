# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:
# • Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# • Gražina, ar nurodytos sukakties metai buvo keliamieji
# • Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# • Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

import datetime

todays_date = datetime.datetime.today()
days_to_month = 0.03287671
days_to_week = 0.142857143
seconds_to_hours = 0.00027778
seconds_to_minutes = 0.01666667

programmer_birthday = datetime.datetime(2000,7,28, 5, 30, 00)

class Anniversary:
    def __init__(self, years, months, days, hours, minutes, seconds):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def years_differece_by_days(self):
        today = datetime.datetime.today()
        anniversary_date = datetime.datetime(self.years, self.months, self.days, self.hours, self.minutes, self.seconds)
        years_difference = today - anniversary_date
        return years_difference.days

    def years_differece_by_seconds(self):
        today = datetime.datetime.today()
        anniversary_date = datetime.datetime(self.years, self.months, self.days, self.hours, self.minutes, self.seconds)
        years_difference = today - anniversary_date
        return years_difference.total_seconds()

    def counting_years(self):
        years = self.years_differece_by_days() / 365
        print(f"Years since the anniversary : {int(years)}")

    def counting_months(self):
        months = self.years_differece_by_days() * days_to_month
        print(f"Months since the anniversary: {int(months)}")

    def counting_weeks(self):
        weeks = self.years_differece_by_days() * days_to_week
        print(f"Weeks since the anniversary: {int(weeks)}")
    def counting_days(self):
        days = self.years_differece_by_days()
        print(f"Days since the anniversary: {days}")

    def counting_hours(self):
        hours = self.years_differece_by_seconds() * seconds_to_hours
        print(f"Hours since the anniversary: {int(hours)}")

    def counting_minutes(self):
        minutes = self.years_differece_by_seconds() * seconds_to_minutes
        print(f"Minutes since the anniversary: {int(minutes)}")

    def counting_seconds(self):
        seconds = self.years_differece_by_seconds()
        print(f"Seconds since the anniversary: {int(seconds)}")

    def counting_leap_year(self):
        years = self.years
        if years % 4 == 0 and (years % 100 != 0 or years % 400 == 0):
            print(f"{years} is leap year")
        else:
            print(f"{years} is not leap year")

    def subtract_days(self):
        anniversary_date = datetime.datetime(self.years, self.months, self.days)
        new_subtracted_date = anniversary_date - datetime.timedelta(days=days_to_subtract)
        print(f"New date after division {new_subtracted_date}")

    def add_days(self):
        anniversary_date = datetime.datetime(self.years, self.months, self.days)
        new_add_date = anniversary_date + datetime.timedelta(days=days_to_add)
        print(f"New date after added days {new_add_date}")

while True:
    input_anniversary_date = input("Enter anniversary date (yyyy-MM-dd HH:MM:ss) : ")
    try:
        anniversary_date = datetime.datetime.strptime(input_anniversary_date, "%Y-%m-%d %H:%M:%S") \
            if input_anniversary_date \
            else programmer_birthday
        anniversary = Anniversary(anniversary_date.year, anniversary_date.month, anniversary_date.day, anniversary_date.hour,
                                  anniversary_date.minute, anniversary_date.second)

        anniversary.counting_years()
        anniversary.counting_months()
        anniversary.counting_weeks()
        anniversary.counting_days()
        anniversary.counting_hours()
        anniversary.counting_minutes()
        anniversary.counting_seconds()
        anniversary.counting_leap_year()

        days_to_subtract = int(input("Enter the number of days to subtract: "))
        anniversary.subtract_days()
        days_to_add = int(input("Enter the number of days to subtract: "))
        anniversary.add_days()
        break

    except ValueError:
        print("Bad input. Try Again..")


