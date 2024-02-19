import cv2, time
from tkinter import messagebox as MessageBox

cam = cv2.VideoCapture(0)
contFotos, maxFotos, retardoFotos = 0, 100, 0.5

if not cam.isOpened(): print("Error. No hay camara"), exit()

# MessageBox.askquestion("Preparate","Acercate a la camara viendo hacia enfrente\n"
#                                    "Gira tu cabeza derecha, izquierda, arriba y abajo")

while True:
    result, image = cam.read()
    cv2.imshow("Camara", image)
    cv2.imwrite(f"./Fotos/foto_{contFotos+1}.png", image)
    contFotos +=1
    time.sleep(retardoFotos)
    if cv2.waitKey(1) and 0xFF == ord("q") or contFotos==maxFotos: break

cam.release()
cv2.destroyAllWindows()