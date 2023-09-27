# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
# • Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką
# (.now().time()).
# • Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
# • Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.
import datetime

todays_date = datetime.date.today()
todays_time = datetime.datetime.now().time()

# print(todays_date, todays_time)
