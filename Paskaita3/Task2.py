# Parašyti programą, kuri:
# • Atspausdintų dabartinę datą ir laiką
# • Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# • Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# • Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

import datetime

datetime_now = datetime.datetime.today()
print(datetime_now)

minus_five_days = datetime_now - datetime.timedelta(days=5)
print(minus_five_days)

add_eight_days = datetime_now + datetime.timedelta(days=8)
print(add_eight_days)

new_date_format = datetime_now.strftime("%Y %m %d, %H:%M:%S")
print(new_date_format)