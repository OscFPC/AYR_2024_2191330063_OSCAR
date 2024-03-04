from tkinter import messagebox as MessageBox
import P03_Metodos as metodo

terminar = "no"
while terminar != 'yes':
    numero = input("Elige el kernel para la imagen:\n"
                   "1. Identity\n"
                   "2. Ridge\n"
                   "3. Edge Detection\n"
                   "4. Sharpen\n"
                   "5. BoxBlur\n"
                   "6. GaussianBlur\n")
    numero = int(numero)
    kernel = metodo.elegirKernel(numero)
    file = '1.jpg'
    largo, alto = 500,500
    img_to_apply_maxPooling = metodo.convulucionar(kernel,file,largo,alto,numero)
    terminar = MessageBox.askquestion("Aplicar",
    "¿Desea aplicar Maxpooling el programa?")
    if terminar == "yes":
        metodo.max_pooling(img_to_apply_maxPooling,alto,largo)