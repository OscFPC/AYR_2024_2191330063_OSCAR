from tkinter import messagebox as MessageBox

import pyautogui

import P02_Metodos as metodo

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
    file = '3.jpg'
    largo, alto = 500,500
    metodo.convulucionar(kernel,file,largo,alto,numero)
    # ventana_activa = pyautogui.getActiveWindowTitle()
    # print("El título de la ventana activa es:", ventana_activa)
    # metodo.tomar_captura_ventana("Figure 1", numero)
    terminar = MessageBox.askquestion("Salir",
    "¿Desea terminar el programa?")
