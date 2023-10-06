from PIL import Image

#Turime logo su peršviečiamu fonu, dydis 128*128. Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir apačios nusiimtų
# po 28 eilutes pikselių. Išsisaugokite, nes naudosime sekančioms užduotims.

logo = Image.open('logo.png')

box = (0, 28, logo.width, logo.height - 28)
region = logo.crop(box)

region.save('cropped_logo.png')

region.show()