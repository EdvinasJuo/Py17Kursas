# http://random.cat/ kas kartą užkrauna vis skirtingą katės nuotrauką.
# Parašykite funkciją, kuriai į parametrus įrašius,
# kiek norime nuotraukų, išsaugotų jas mūsų kompiuteryje.
import requests
import re
import os


def downloading_photo(number):
    for i in range(number):
        r = requests.get('http://random.cat/')
        if r.status_code == 200:
            web_text = r.text
            image_link = re.search(r'https([^"]+).jpg', web_text)

            if image_link:
                image_url = image_link.group(0)
                file_name = os.path.basename(image_url)

                with open(file_name, 'wb') as f:
                    f.write(requests.get(image_url).content)
                    print(f"Nuotrauka issaugota kaip: {file_name}")
        else:
            print(f"Nepavyko atidaryti puslapio. Statuso kodas: {r.status_code}")

downloading_photo(1)
