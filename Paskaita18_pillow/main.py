from PIL  import Image, ImageFilter, ImageEnhance

# im = Image.open("tuscia.jpg")
# im.save("ToDoList.jpg")         # ISSAUGO KAIP NAUJA FOTO SU PAVADINMU
# print(im.format, im.mode, im.size)
# ----------------------------------------------------------------------------
# size = 128, 128         # PAMAZINAMAS NUOTRAUKOS DYDIS!
# im.thumbnail(size)
# im.show()
# im.save("ToDoList_thumbnail.png")
# ----------------------------------------------------------------------------
# size = 128, 128
# box = (100, 100, 300, 300)   # ISKERPAMA DALIS IS NUOTRAUKOS
# region = im.crop(box)
# region.show()
# region.save("crop.png")
# ----------------------------------------------------------------------------
# resized = im.resize((1000, 1000)) #RESIZINA
# resized.show()


# # -------------- sumazint pagal kofecienta jeigu nuotrauka yra nelygi
# # PVZ NUOTRAUKOS DYDIS 590 x 428
# koef = 200 * 428 / 590           # 200 galima pakeisti i kita dydi. pvz 800, kad padidinti
# resized = im.resize((200, int(koef))) # taip pat ir cia pakeisti 200
# resized.show()

# ----------------------------------------------------------------------------
# UZDETI VIENA NUOTRAUKA ANT KITOS
# toDoList = Image.open('tuscia.jpg')
# heart = Image.open('DSC_0370.jpg')
# heart_location = (0, 0, heart.size[0], heart.size[1])
# toDoList.paste(heart, heart_location, heart)
# toDoList.show()

# ----------------------------------------------------------------------------
# UZDEDADA BLURO EFEKTAS
# dog = Image.open('dog_logo.png')
# img = dog.filter(ImageFilter.BLUR)
# img.show()

# UZDEDADA KONTURO EFEKTA
# dog = Image.open('dog_logo.png')
# img = dog.filter(ImageFilter.CONTOUR)
# img.show()


# -----------------------------------GET DATA-------------------------------
# dog = Image.open('dog_logo.png')
# data = dog.getdata()
#
# print(data[0]) # DUODA RGB CHANELIO SPALVAS
#
# for pixel in range(5):
#     print(data[pixel])


# # UZDEDA ANT NUOTRAUKOS 10000 tukst PIXELIU
# dog = Image.open('dog_logo.png')
#
# nex_pixel = (100, 100, 100)
# new_data = []
# for i in range(10000):
#     new_data.append(nex_pixel)
# dog.putdata(new_data)
# dog.show()

#----- PAKEICIAM NUOTRAUKOS MODE I JUODAI BALTA-----------------------------
# dog = Image.open('dog_logo.png')
#
# dog_bw = dog.convert("L")    # "L" VERCIA I JUODAI BALTA
# dog_bw.show()
# print(dog_bw.mode)


# ----------------IMAGE ENHANCE---------------------------------------------

# dog = Image.open('dog_logo.png')
#
# enh = ImageEnhance.Contrast(dog)
# enh.enhance(1.3).show()
# #NORINT ISAUGOTI
# # enh.enhance(1.3).save('dog_enhance.png')
#
# enh2 = ImageEnhance.Color(dog)
# enh2.enhance(1.5).show()