# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 4 - Crea tu propio filtro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow, noise
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('TITULO', frame)

    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imshow('GRISES', grises)

    ruido = noise(frame)
    imshow('Imagen Ruido', ruido)

    contraste = 2.1
    brillo =  20
    nuevo = cv2.convertScaleAbs(frame,  alpha=contraste, beta=brillo)
    imshow('Nueva imagen', nuevo)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla

cv2.destroyAllWindows()
