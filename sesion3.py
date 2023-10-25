# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 3 - Mejorando las imágenes
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow, noise
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:
paco = cv2.imread('./img/7.jpg')
imshow('Original', paco)

ruido = noise(paco)
imshow('Imagen Ruido', ruido)

size = 5
kernel = np.ones((size, size), np.float32) / (size*size)
desenfoque = cv2.filter2D(ruido, -1, kernel)
imshow('Desenfoque', desenfoque)

kernel = -1*np.ones((5,5), np.float32)
kernel[2,2] = 25
enfoque = cv2.filter2D(paco, -1, kernel)
imshow('Enfoque', enfoque)


contraste = 1.1
brillo = -20
nuevo = cv2.convertScaleAbs(paco, alpha=contraste, beta=brillo)
imshow('Nueva imagen', nuevo)



# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
