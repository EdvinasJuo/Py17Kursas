import requests

# r = requests.get('http://google.com')
# print(r.text)

#===================================================================================================


# r = requests.get('https://www.python.org/static/img/python-logo.png')
# print(r.content)
#
# with open('logo.png', 'wb') as f:
#     f.write(r.content)

#===================================================================================================

                # STATUS CODE          TIKRINAM AR PAVYKSTA PRISIJUNGTI PRIE PUSLAPIO PAGAL STATUS CODE
# r = requests.get('http://google.com/asfasdfava')
#
# if r.status_code not in range(400, 600):
#     print("Pavyko prisijungti!")
# else:
#     print(f"Kazkas nepavyko {r.status_code}")
#
# # KITAS SUPAPRASTINTAS VARIANTAS SU R.OK
# if r.ok:
#     print("Pavyko prisijungti!")
# else:
#     print(f"Kazkas nepavyko {r.status_code}")

#===================================================================================================
#                         # PAIMAMA SERVERIO INFORMACIJA SU R.HEADERS
# r = requests.get('http://python.org/')
#
# print(r.headers) # GRAZINA KAIP DICTIONARY IS KURIO GALIMA PASIIMTI KEY IR VALUES
# print(r.headers['Content-Length'])
# print(r.url)

#===================================================================================================
                          # GET METODAS imam ir naudojam 'params ='
                          # PRIDEDAMI NUORODU, URL PARAMETRAI
# payload = {'ieskoti': 'samsung'}
# r = requests.get('https://www.telia.lt/privatiems/paieska', params=payload)
# print(r.url)
# print(r.text)

#===================================================================================================
                          # POST METODAS imam ir naudojam 'data ='
# data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
# r = requests.post('https://httpbin.org/ip', data=data)
# print(r.text)
#===================================================================================================
