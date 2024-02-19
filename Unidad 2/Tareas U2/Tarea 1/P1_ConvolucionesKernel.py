from keras.utils import load_img, img_to_array, array_to_img, save_img

def proceso(file,largo,alto,nombre,kernel):
    img_original = load_img(file, target_size=(largo, alto), color_mode="grayscale")

    img_a_convolucinar = img_to_array(img_original)  # filas, columnas, canales de colores

    print(img_a_convolucinar.shape)

    img_convolucionada = [] #nueva imagen

    for filas in range(1,alto-1): #ignora los pixeles de la primera y ultima fila
        new_fila = []
        for columnas in range(1, largo-1): #ignora los pixeles de la primera y ultima columna

            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)): # 0 1 2
                for c_kernel in range(len(kernel)): # 0 1 2
                    pixelConvulucionado += (kernel[f_kernel][c_kernel]
                                            * img_a_convolucinar[filas + (f_kernel-1)][columnas+(c_kernel-1)])

            if nombre=="BoxBlur":
                pixelConvulucionado = pixelConvulucionado * (1/9)
                new_fila.append(pixelConvulucionado)
            elif nombre=="GaussianBlur":
                pixelConvulucionado = pixelConvulucionado * (1 / 16)
                new_fila.append(pixelConvulucionado)
            else:
                new_fila.append(pixelConvulucionado)

        img_convolucionada.append(new_fila)

    img = array_to_img(img_convolucionada)
    print(img.size)


    #img.show()

    ##plot - 2 imagenes
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15,5))

    plt.subplot(1,2,1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img_original, cmap='gray')

    plt.subplot(1,2,2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap='gray')

    #plt.show()
    plt.savefig(f'Img_{nombre}.jpg')
    #save_img(f'Img_{nombre}.jpg', img_convolucionada)

Kernels = {
    'Identity': [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    'Ridge': [
        [0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]
    ],
    'Edge': [
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1]
    ],
    'Sharpen': [
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ],
    'BoxBlur': [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ],
    'GaussianBlur': [
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ]
}

# img=(input("Imagen--> "))
#
# file = f'../Practicas U2/{img}'
file = 'yo.jpeg'
# largo=(int(input("largo--> ")))
# alto=(int(input("alto--> ")))
largo = 500
alto = 500
nombre=input("Nombre del kernel--> ")

proceso(file,largo,alto,nombre,Kernels[nombre])

