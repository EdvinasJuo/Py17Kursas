# Sukurkite programą, kuri, gavusi nuorodą į katalogą, praiteruos visus jame esančius failus, išrinks nuotraukas,
# pakeis dydį pagal jūsų nurodytą aukštį išlaikant proporcijas, ir kiekvienos nuotraukos apatiniame dešiniajame
# kampe įdės logotipą, tą kurį išsisaugojote pirmoje užduotyje.
# Naudokite .resize, kadangi nuotrauką galbūt reikės padidinti, nebūtinai tik sumažinti.

from PIL import Image
import os


def opening_folder_and_collecting_photos(folder_directory):
    image_list = []
    for images in os.listdir(folder_directory):
        if (images.endswith('.png')):
            image_list.append(os.path.join(folder_directory, images))
    return image_list


def changing_height(image_list, new_widht, new_height):
    resized_images = []
    for image_path in image_list:
        image = Image.open(image_path)
        resized_image = image.resize((new_widht, new_height))
        resized_images.append(resized_image)
    return resized_images


def adding_logo(images, logo_path):
    logo = Image.open(logo_path)
    for image in images:
        widht, height = image.size
        logo_widht, logo_height = logo.size
        logo_location = (widht - logo_widht, height - logo_height)
        image.paste(logo, logo_location, logo)


folder_directory = 'C:\\Users\\edvin\\PycharmProjects\\Paskaita18_pillow\\Photos'
logo_path = 'cropped_logo.png'
image_list = opening_folder_and_collecting_photos(folder_directory)

# pakeicia nuotrauku dydi
resized_images = changing_height(image_list, new_height=500, new_widht=500)

adding_logo(resized_images, logo_path)
for image in resized_images:
    image.show()
