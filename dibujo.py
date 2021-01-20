#Aprender a dibujar  ,cuadriculando un dibujo y su hoja en blanco 
#Antonio Villanueva Segura
#!/usr/bin/python
# -*- coding: latin-1 -*-
# pip install opencv-python
#
import cv2
import numpy as np
import os
from os import listdir

#Crea lineas en X
def creaLineasX(imagen,alto,ancho,cuadricula=100):
    #Crea lineas x
    for x in range(0,ancho,cuadricula):
        cv2.line(imagen,(x,0),(x,alto),(255,0,0),1)   

#Crea lineas en Y        
def creaLineasY(imagen,alto,ancho,cuadricula=100):       
    for y in range(0,alto,cuadricula):
        cv2.line(imagen,(0,y),(ancho,y),(255,0,0),1)            

#Crea cuadricula X e Y en un dibujos
def creaCuadricula(imagen,alto,ancho,cuadricula=100):
    creaLineasX(imagen,alto,ancho,cuadricula)
    creaLineasY(imagen,alto,ancho,cuadricula)    
    
#Lista y filtra ficheros de un directorio a tratar
def listaDeFicheros(directorio ):
    extensiones=['jpg','jpeg','gif','png','bmp']
    ficheros = listdir( directorio)
    tmp=[] #Fichero temporal 
    
    #Anade los ficheros graficos validos
    for fichero in ficheros:
        for ext in extensiones:
            
            #Es una externsion grafica y no es ya una copia nuestra
            if ext in fichero and not 'CUAD.jpg'==fichero[-8:]:
                tmp.append(fichero)
                
    return tmp    
    
# main code
if __name__ == "__main__" :
    
    directorio=os.getcwd()+'/'    
    
    cuadricula=int (input("Tamano del cuadriculado (50 =1 cm )? "))
    
    #print (listaDeFicheros (directorio))
    for nombre in listaDeFicheros(directorio):
        
        #Abre la imagen
        imagen = cv2.imread(os.path.expanduser(directorio+nombre))
        
        #Tamano de la imagen height, width, and color.
        alto=imagen.shape[0]
        ancho=imagen.shape[1]
            
        # Crea una imagen de alto x ancho  vacia
        copia = 255 * np.ones(shape=[alto, ancho, 3], dtype=np.uint8) 
                
        #Cuadricula las dos imagenes
        creaCuadricula(imagen,alto,ancho,cuadricula)
        creaCuadricula(copia,alto,ancho,cuadricula)   
        
        #Muestra la imagen con la cuadricula por pantalla
        cv2.imshow('Imagen cuadriculada',imagen)
        #cv2.imshow('Para dibujar ',copia)        
        
        
        #Guarda imagen y copia con cuadricula
        cv2.imwrite(directorio+nombre+"CUAD.jpg",imagen)
        cv2.imwrite(directorio+nombre+"VCUAD.jpg",copia)  
        
        cv2.waitKey(1000)  
    
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

