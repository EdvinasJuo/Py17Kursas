from PIL import Image, ImageEnhance

def file_saving(filename, file_save = False):
    logo = Image.open(filename)

    file_format = filename.split('.')

    if file_save:
        new_file_name = filename.replace('.' + file_format[-1], '_modified.png')
        logo.save(new_file_name)

def changing_contrast(filename, contrast, file_save = False):
    logo = Image.open(filename)

    contrast_effect = ImageEnhance.Contrast(logo)
    logo = contrast_effect.enhance(contrast)

    logo.show()

    if file_save:
        file_saving(filename, file_save)

def changing_colourful(filename, colourful, file_save = False):
    logo = Image.open(filename)

    colourful_effect = ImageEnhance.Color(logo)
    logo = colourful_effect.enhance(colourful)

    logo.show()

    if file_save:
        file_saving(filename, file_save)


def changing_sharpness(filename, sharpness, file_save=False):
    logo = Image.open(filename)

    sharpness_effect = ImageEnhance.Sharpness(logo)
    logo = sharpness_effect.enhance(sharpness)

    logo.show()

    if file_save:
        file_saving(filename, file_save)


def changing_brightness(filename, brightness, file_save = False):
    logo = Image.open(filename)

    brightness_effect = ImageEnhance.Brightness(logo)
    logo = brightness_effect.enhance(brightness)

    logo.show()

    if file_save:
        file_saving(filename, file_save)


def working_with_logo(filename, contrast, colourful, sharpness, brightness, file_save = False):
    logo = Image.open(filename)

    #creating effects objects
    contrast_effect = ImageEnhance.Contrast(logo)
    colourful_effect = ImageEnhance.Color(logo)
    sharpness_effect = ImageEnhance.Sharpness(logo)
    brightness_effect = ImageEnhance.Brightness(logo)

    #applying effects
    logo = contrast_effect.enhance(contrast)
    logo = colourful_effect.enhance(colourful)
    logo = sharpness_effect.enhance(sharpness)
    logo = brightness_effect.enhance(brightness)

    logo.show()

    if file_save:
        file_saving(filename, file_save)


changing_contrast('DSC_0370.jpg', 1.5, True)
# changing_colourful('dog_logo.png', 1.9, False)
# changing_sharpness('dog_logo.png', 1.2, False)
# changing_brightness('dog_logo.png', 2.1, False)
# working_with_logo('dog_logo.png', 3, 1.2, 1.5, 1.5, False)

