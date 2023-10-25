# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 2 - Imágenes en blanco y negro
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------
# Escribe tu código aquí:
img = cv2.imread('./img/22.jpg')
imshow('Original', img)

grises = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imshow('GRISES', grises)

plt.hist(grises.ravel(), 256, [0, 256])
plt.show()



# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
