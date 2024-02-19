from datetime import datetime
import pyautogui
from keras.utils import  load_img, img_to_array, array_to_img, save_img
def elegirKernel(num):
    print('ok')
    kernel = []
    if num == 1:
        kernel = kernelIdentity = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
    elif num == 2:
        kernel = kernelRidge = [
            [0, -1, 0],
            [-1, 4, -1],
            [0, -1, 0]
        ]
    elif num == 3:
        kernel = kernelEdgeDetection = [
            [-1, -1, -1],
            [-1, 8, -1],
            [-1, -1, -1]
        ]
    elif num == 4:
        kernel = kernelSharpen = [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]
    elif num == 5:
        kernel = kernelBoxBlur = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]  # multiplicar por 1/9
    elif num == 6:
        kernel = kernelGaussianBlur = [
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]
        ]  # multiplicar por 1/16
    return kernel

def duplicar_primero_ultimo(array_imagen):
    array_imagen.insert(0, array_imagen[0])
    array_imagen.append(array_imagen[len(array_imagen) - 1])

    img_completa = []
    for i in range(len(array_imagen)):
        add = []
        if i == 0:
            # print(array_imagen[i], i, 'Zero')
            add.append(0)
            for dato in array_imagen[i]:
                add.append(dato)
            add.append(0)
        elif i == len(array_imagen) - 1:
            # print(array_imagen[i], i, 'End')
            add.append(0)
            for dato in array_imagen[i]:
                add.append(dato)
            add.append(0)
        else:
            # print(array_imagen[i], i, 'Middle')
            add.append(array_imagen[i][0])
            for dato in array_imagen[i]:
                add.append(dato)
            add.append(array_imagen[i][len(array_imagen[i]) - 1])
        img_completa.append(add)
    return img_completa

def convulucionar(kernel, file, largo, alto, numElegido):
    img_original = load_img(file, target_size=(largo, alto), color_mode='grayscale')

    img_a_convolucionar = img_to_array(img_original)

    print(img_a_convolucionar.shape)

    img_a_convolucionar = list(img_a_convolucionar)
    img_a_convolucionar = duplicar_primero_ultimo(img_a_convolucionar)

    img_convulucionada = []

    for filas in range(1, alto + 1):
        new_fila = []
        for columnas in range(1, largo + 1):
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):
                for c_kernel in range(len(kernel)):
                    pixelConvulucionado += (kernel[f_kernel][c_kernel]
                                            * img_a_convolucionar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)])
            if numElegido == 5:
                pixelConvulucionado = pixelConvulucionado * (1 / 9)
            if numElegido == 6:
                pixelConvulucionado = pixelConvulucionado * (1 / 16)
            new_fila.append(pixelConvulucionado)
        img_convulucionada.append(new_fila)
    img = array_to_img(img_convulucionada)
    print(img.size)

    import matplotlib.pyplot as plt
    plt.figure(figsize=(20, 10))

    plt.subplot(1, 2, 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img_original, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap='gray')

    # fig, axs = plt.subplots(1, 2, figsize=(20, 10))
    #
    # axs[0].set_xticks([])
    # axs[0].set_yticks([])
    # axs[0].imshow(img_original, cmap='gray')
    #
    # axs[1].set_xticks([])
    # axs[1].set_yticks([])
    # axs[1].imshow(img, cmap='gray')
    plt.show()
    # guardar_grafico(plt, numElegido)

def guardar_grafico(plt, num, nombre_archivo=None):
    """
    Guarda automáticamente un gráfico matplotlib.

    Parámetros:
    - plt: Objeto matplotlib que contiene el gráfico.
    - nombre_archivo (opcional): Nombre del archivo de imagen. Si no se proporciona, se genera uno automáticamente con la fecha y hora actual.
    """
    nombres = ['Identity','Ridge','EdgeDetection','Sharpen','BoxBlur','GaussianBlur']
    if nombre_archivo is None:
        nombre_archivo = datetime.now().strftime("%Y%m%d_%H%M%S") + '_imagen_' + nombres[num] +'.png'

    plt.savefig(nombre_archivo)
    print(f"Gráfico guardado como '{nombre_archivo}'.")

import pyautogui

def tomar_captura_ventana(nombre_ventana, num):
    nombres = ['Identity', 'Ridge', 'EdgeDetection', 'Sharpen', 'BoxBlur', 'GaussianBlur']
    ruta_guardado = nombres[num-1]
    ventana = pyautogui.getWindowsWithTitle(nombre_ventana)
    if len(ventana) > 0:
        ventana[0].activate()
        region = (ventana[0].left, ventana[0].top, ventana[0].width, ventana[0].height)
        captura = pyautogui.screenshot(region=region)
        captura.save(ruta_guardado)
        print(f"Captura de la ventana '{nombre_ventana}' guardada en '{ruta_guardado}'.")
    else:
        print(f"No se encontró la ventana '{nombre_ventana}'.")
