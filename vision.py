# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:56:02 2020

@author: Javier Cortes
"""
import cv2
import numpy as np
 
imagen = cv2.imread('f2c2.png')
hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
 
#Rango de colores detectados:
    
#Grupo de primarios de luz    
#Amarillo:
amarillo_bajos = np.array([20,25,230], dtype=np.uint8)
amarillo_altos = np.array([32,255,255], dtype=np.uint8)
#Rojos:
rojo_bajos1 = np.array([0,25,82], dtype=np.uint8)
rojo_altos1 = np.array([5,255,255], dtype=np.uint8)
rojo_bajos2 = np.array([170,25,135], dtype=np.uint8)
rojo_altos2 = np.array([179,255,255], dtype=np.uint8)
#Cian:
cian_bajos = np.array([78,25,127], dtype=np.uint8)
cian_altos = np.array([86,255,255], dtype=np.uint8)
#Verdes:
verde_bajos = np.array([33,63,51], dtype=np.uint8)
verde_altos = np.array([77,255,255], dtype=np.uint8)

#Grupo de secundarios de luz
#Café:
cafe_bajos = np.array([8,30,76], dtype=np.uint8)
cafe_altos = np.array([30,211,179], dtype=np.uint8)
#Rosa:
rosa_bajos = np.array([145,25,204], dtype=np.uint8)
rosa_altos = np.array([169,255,255], dtype=np.uint8)
#Violeta:
violeta_bajos = np.array([131,25,76], dtype=np.uint8)
violeta_altos = np.array([144,255,255], dtype=np.uint8)
#Anaranjado:
naranja_bajos = np.array([6,25,178], dtype=np.uint8)
naranja_altos = np.array([19,255,255], dtype=np.uint8) 
#Azules:
azul_bajos = np.array([87,25,178], dtype=np.uint8)
azul_altos = np.array([130,255,255], dtype=np.uint8)

#Grupo de Neutros
#Blanco:
blanco_bajos = np.array([0,0,209], dtype=np.uint8)
blanco_altos = np.array([179,25,255], dtype=np.uint8)
#Negro:
negro_bajos = np.array([0,0,0], dtype=np.uint8)
negro_altos = np.array([159,63,51], dtype=np.uint8)
#gris:
grises_bajos = np.array([0,0,40], dtype=np.uint8)
grises_altos = np.array([179,38,217], dtype=np.uint8)


#Crear las mascaras
mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)
mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
mascara_azul = cv2.inRange(hsv, azul_bajos, azul_altos)
mascara_cian = cv2.inRange(hsv, cian_bajos, cian_altos)
mascara_anaranjado = cv2.inRange(hsv, naranja_bajos, naranja_altos)
mascara_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
mascara_violeta = cv2.inRange(hsv, violeta_bajos, violeta_altos)
mascara_rosa = cv2.inRange(hsv, rosa_bajos, rosa_altos)

#Crear mascaras 2
mascara_negro = cv2.inRange(hsv, negro_bajos, negro_altos)
mascara_gris = cv2.inRange(hsv, grises_bajos, grises_altos)
mascara_blancos = cv2.inRange(hsv, blanco_bajos, blanco_altos)
mascara_cafe = cv2.inRange(hsv, cafe_bajos, cafe_altos)
 
#Juntar todas las mascaras
#mask = cv2.add(mascara_rojo1, mascara_rojo2)
#mask = cv2.add( mask,mascara_verde)
#mask = cv2.add(mask, mascara_azul)
 #Juntar todas las mascaras
maska = cv2.add(mascara_rojo1, mascara_rojo2)
#mask1 = cv2.add(verde_bajos, verde_altos)
#mask2 = cv2.add(azul_bajos, azul_altos)
#Mostrar la mascara final y la imagen
#cv2.imshow('Final rojo', maska)
#cv2.imshow('Final verde', mascara_verde)
#cv2.imshow('Final azul', mascara_azul)
#cv2.imshow('Final cian', mascara_cian)
#cv2.imshow('Final anaranjado', mascara_anaranjado)
#cv2.imshow('Final amarillo', mascara_amarillo)
#cv2.imshow('Final violeta', mascara_violeta)
#cv2.imshow('Final rosa', mascara_rosa)
#cv2.imshow('Final negro', mascara_negro)
#cv2.imshow('Final gris', mascara_gris)
#cv2.imshow('Final Blanco', mascara_blancos)
#cv2.imshow('Final Café', mascara_cafe)
cv2.imshow('Imagen', imagen)
prue = maska + mascara_verde + mascara_azul + mascara_cian + mascara_anaranjado + mascara_amarillo + mascara_violeta + mascara_rosa

col1 = cv2.bitwise_and(imagen,imagen, mask= mascara_verde)
col2 = cv2.bitwise_and(imagen,imagen, mask= mascara_anaranjado)
col3 = cv2.bitwise_and(imagen,imagen, mask= maska)
col4 = cv2.bitwise_and(imagen,imagen, mask= mascara_azul)
col5 = cv2.bitwise_and(imagen,imagen, mask= mascara_cian)
col6 = cv2.bitwise_and(imagen,imagen, mask= mascara_amarillo)
col7 = cv2.bitwise_and(imagen,imagen, mask= mascara_rosa)
col8 = cv2.bitwise_and(imagen,imagen, mask= mascara_violeta)
col9 = cv2.bitwise_and(imagen,imagen, mask= mascara_cafe)
col10 = cv2.bitwise_and(imagen,imagen, mask= mascara_gris)
col11 = cv2.bitwise_and(imagen,imagen, mask= mascara_blancos)

"""
#Kernel:
kernel = np.ones((2,2),np.uint8) #Matriz de 6x6 llena de '1'

#Eliminamos el ruido con un CLOSE seguido de un OPEN:
col1 = cv2.morphologyEx(col1, cv2.MORPH_CLOSE, kernel)
col1 = cv2.morphologyEx(col1, cv2.MORPH_OPEN, kernel)
col2 = cv2.morphologyEx(col2, cv2.MORPH_CLOSE, kernel)
col2 = cv2.morphologyEx(col2, cv2.MORPH_OPEN, kernel)
col3 = cv2.morphologyEx(col3, cv2.MORPH_CLOSE, kernel)
col3 = cv2.morphologyEx(col3, cv2.MORPH_OPEN, kernel)
col4 = cv2.morphologyEx(col4, cv2.MORPH_CLOSE, kernel)
col4 = cv2.morphologyEx(col4, cv2.MORPH_OPEN, kernel)
col5 = cv2.morphologyEx(col5, cv2.MORPH_CLOSE, kernel)
col5 = cv2.morphologyEx(col5, cv2.MORPH_OPEN, kernel)
col6 = cv2.morphologyEx(col6, cv2.MORPH_CLOSE, kernel)
col6 = cv2.morphologyEx(col6, cv2.MORPH_OPEN, kernel)
col7 = cv2.morphologyEx(col7, cv2.MORPH_CLOSE, kernel)
col7 = cv2.morphologyEx(col7, cv2.MORPH_OPEN, kernel)
col8 = cv2.morphologyEx(col8, cv2.MORPH_CLOSE, kernel)
col8 = cv2.morphologyEx(col8, cv2.MORPH_OPEN, kernel)
"""

prueba = col1 + col3 + col2 + col4 + col5 +col6 +col7 + col8 + col9 + col10 + col11
"""cv2.imshow('color',prueba)
cv2.imshow('color byn',prue)
cv2.imwrite('color.png',prueba)
cv2.imwrite('byn.png',prue)"""

cv2.imshow('color verde',col1)
cv2.imshow('color anaranjado',col2)
cv2.imshow('color rojo',col3)
cv2.imshow('color azul',col4)
cv2.imshow('color cian',col5)
cv2.imshow('color amarillo',col6)
cv2.imshow('color rosa',col7)
cv2.imshow('color violeta',col8)
cv2.imshow('color cafe',col9)
cv2.imshow('color gris en blanco',mascara_gris)
cv2.imshow('color color gris',col10)
cv2.imshow('color blanco',col11)
cv2.imshow('color negro',mascara_negro)
cv2.imshow('conjunto',prueba)

#guardarla imagen procesada
#cv2.imwrite('Rojos.png',maska)
#cv2.imwrite('Verdes.png',mascara_verde)
#cv2.imwrite('Azules.png',mascara_azul)
#cv2.imwrite('Cianes.png',mascara_cian)
#cv2.imwrite('Anaranjados.png',mascara_anaranjado) 
#cv2.imwrite('Amarillo.png',mascara_amarillo)
#cv2.imwrite('Violetas.png',mascara_violeta)
#cv2.imwrite('Rosas.png',mascara_rosa)

cv2.imwrite('Color Verde.png',col1)
cv2.imwrite('Color Naranja.png',col2)
cv2.imwrite('Color Rojo.png',col3)
cv2.imwrite('Color Azul.png',col4)
cv2.imwrite('Color Cian.png',col5)
cv2.imwrite('Color Amarillo.png',col6)
cv2.imwrite('Color Rosa.png',col7)
cv2.imwrite('Color Violeta.png',col8)
cv2.imwrite('Color cafe.png',col9)
cv2.imwrite('Color gris en blanco.png',mascara_gris)
cv2.imwrite('Color gris.png',col10)
cv2.imwrite('Color blanco.png',col11)
cv2.imwrite('Color negro.png',mascara_negro)
cv2.imwrite('Conjunto.png', prueba)
#Salir con ESC
while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
 
cv2.destroyAllWindows()
