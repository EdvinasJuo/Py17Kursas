# import datetime
#
# dateTime = datetime.datetime.today()        # Visa data
# print(dateTime)
#
# time = datetime.datetime.today().time()     # LAIKAS
# print(time)
#
# x = datetime.datetime(2020, 7, 21, 20, 33, 20) # NUrodomoa sava data
# print(x)
#
# new_format = x.strftime("%A, %d. %B %Y %I:%M%p") # FORMATAVIMAS
# print(new_format)
#
# now = datetime.datetime.now()
# print(now)
#
# minus_5_days = now - datetime.timedelta(days=5) # ATIMAMOS DIENOS
# print(minus_5_days)
#
# minus_5_hours = now - datetime.timedelta(hours=5) #Atimamos valandos
# print(minus_5_hours)
#
# minus = now - datetime.timedelta(days=20, hours=6)
# print(minus)
#
# # UZDUOTELE
# #
# # input_date = input("Iveskite data (yyyy-MM-dd 20:30:50): ")
# # date = datetime.datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")                 #strptime is string pavercia i datetime
# #
# # # now = datetime.datetime.now()
# # #difference = now - date
# # # print(difference)
# # #
# # # print(difference.days)                         # SKIRTUMAS TARP DIENU, SEKUNDZIU IR TOTAL SEKUNDZIU
# # # print(difference.seconds)
# # # print(difference.total_seconds())
#
# now = datetime.datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
# print(now.weekday())
