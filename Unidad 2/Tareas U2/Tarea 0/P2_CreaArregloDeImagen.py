from keras.utils import load_img, img_to_array

largo, alto = 1000, 1000
#file = './FIT V.jpg'
file = './3.jpg'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )
# img.show()

imagen_en_array = img_to_array(img)  #filas, columnas, canales de colores
print(imagen_en_array.shape)

archivo_imagen = open("./kirbi.csv", "w")
for i in imagen_en_array:
    for pixel in i:
        archivo_imagen.write(str(int(pixel[0])) + ",")
    archivo_imagen.write("\n")
archivo_imagen.flush()
archivo_imagen.close()

#Mona 250
#Paisaje 500
#Kirbi 1000