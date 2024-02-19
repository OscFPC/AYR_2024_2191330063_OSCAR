import cv2  ##opencv
from tkinter import messagebox as MessageBox
cam = cv2.VideoCapture(0) ##videocamara ---
contFotos = 0
while True:
    result, image = cam.read()
    if result:
        cv2.imshow("Camara_Principal", image)
        res = cv2.waitKey(1) ## 1  = .. no detenga la ejecucion
        #print(res , "  ", ord("q"))
        if res == ord("q"):
            cam.release()
            cv2.destroyWindow("Camara_Principal")
            break
        elif res == ord(" "): ##space
            if contFotos>=0 and contFotos<=13:
                print("Acerque el rostro de frente a la camara.")
                if contFotos==0: terminar = MessageBox.askquestion("Sonrie","Acerquese a la camara")
                if contFotos == 13: terminar = MessageBox.askquestion("Sonrie", "Volte al lado derecho")
            elif contFotos>13 and contFotos<=26:
                print("Mire hacia el lado derecho cerca de la camara")
                if contFotos==26: terminar = MessageBox.askquestion("Sonrie","Volte al lado izquierdo")
            elif contFotos > 26 and contFotos <= 39:
                print("Mire hacia el lado izquierdo cerca de la camara")
                if contFotos==39: terminar = MessageBox.askquestion("Sonrie","Volte hacia arriba")
            elif contFotos > 39 and contFotos <= 52:
                print("Mire hacia arriba de frente cerca de la camara")
                if contFotos==52: terminar = MessageBox.askquestion("Sonrie","Alejese de la camara")
            elif contFotos > 52 and contFotos <= 65:
                print("Aleje el rostro de la camara viendo hacia enfrente")
                if contFotos==65: terminar = MessageBox.askquestion("Sonrie","Volte al lado derecho")
            elif contFotos > 65 and contFotos <= 78:
                print("Mire hacia el lado izquierdo lejos de la camara")
                if contFotos==78: terminar = MessageBox.askquestion("Sonrie","Volte al lado izquierdo")
            elif contFotos > 78 and contFotos <= 91:
                print("Mire hacia el lado derecho lejos de la camara")
                if contFotos==91: terminar = MessageBox.askquestion("Sonrie","Mire hai arriba")
            elif contFotos > 91 and contFotos <= 104:
                print("Mire hacia arriba de frente lejos de la camara")
                if contFotos==104: terminar = MessageBox.askquestion("Sonrie","BYE")
            cv2.imwrite("foto_" + str(contFotos) + ".png", image)
            contFotos += 1
    else:
        print("No image detected. Please! try again")
        break

