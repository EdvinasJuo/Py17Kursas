# Parašykite programą, kuriai padavus nuotrauką,
# ir nurodžius pikselio R G B reikšmes, visi pikseliai, kurių nors viena
# reikšmė viršija jūsų nurodytą ribą, būtų pakeisti juodais, o likusieji baltais.

from PIL import Image

image = Image.open('plaustas.png').convert('RGB')
new_pixel = (155, 155, 250)
data = image.getdata()
new_data = []

riba = 20

def restriction(rgb):
    return max(0, min(255, rgb))

for pixel in data:
    r, g, b = pixel

    if r > riba or g > riba or b > riba:
        r, g, b = 0, 0, 0
    else:
        r, g, b = 255, 255, 255

    new_data.append((r, g, b))

new_image = Image.new('RGB', image.size)
new_image.putdata(new_data)
new_image.show()