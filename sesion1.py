# -------------------------------------------------------------------------
# Crack the Code
# Diseño de filtros con Python
# Sesión 1 - Introducción a las imágenes digitales
# -------------------------------------------------------------------------
# Importar bibliotecas que se utilizarán - no modifiques esta sección
from imagenes import imshow
import cv2
import numpy as np

# -------------------------------------------------------------------------
# Escribe tu código aquí:

img = cv2.imread('./img/14.jpg')
imshow('titulo', img)

negro = np.zeros(img.shape, np.uint8)
imshow('tituloNegro',negro)

blanco = 255*np.ones(img.shape, np.uint8)
imshow('tituloBlanco',blanco)

gris = 200*np.ones(img.shape, np.uint8)
imshow('tituloGris',gris)

azul = np.zeros(img.shape, np.uint8)
azul [:,:,0] = img [:, :, 0]
imshow('azul',azul)

verde = np.zeros(img.shape, np.uint8)
verde [:,:,1] = img [:, :, 1]
imshow('verde',verde)

rojo = np.zeros(img.shape, np.uint8)
rojo [:,:,2] = img[:,:,2]
imshow('rojo',rojo)

#Guardar imagenes en la carpeta que se creo automaticamente
cv2.imwrite('./out/rojo.jpg', blanco)
cv2.imwrite('./out/negro.jpg', negro)
cv2.imwrite('./out/gris.jpg', gris)
cv2.imwrite('./out/azu;.jpg', azul)
cv2.imwrite('./out/rojo.jpg', rojo)
cv2.imwrite('./out/verde.jpg', verde)


# -------------------------------------------------------------------------
# Deja siempre este código hasta el final del archivo - no lo borres
# Este código sirve para mantener las ventas abiertas y
# cerrarlas cuando se presiona una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
