# Importamos las librerias
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

ruta = "./imagenes_read/"
# Lista todos los archivos en la carpeta
archivos = os.listdir(ruta)
# Itera sobre cada archivo y cambia su nombre
for nombre_archivo in archivos:
    #Leer imagen a la cual se le agregara la marca de agua
    img = cv2.imread("./imagenes_read/"+nombre_archivo)#Lee las imagenes conforme va iterando i
    h_img = img.shape[0]
    w_img = img.shape[1]
    tam_img = img.shape
    print("\n"+nombre_archivo+"\n")
    print("Tamaño de Imagen --> "+str(tam_img)+" H:"+str(h_img)+"px x W:"+str(w_img)+"px")
    #cv2.imshow('Imagen', img) Muestra imagen original

    if w_img>(h_img*1.25):#Se calcula el tamaño de la imagen para ver si es rectangular
         print("Imagen Rectangular")
         img2 = cv2.imread("marca_agua_rectangular.png", cv2.IMREAD_UNCHANGED)#lee marca de agua rectangular

    if (w_img<(h_img*1.25) and w_img>(h_img*0.75)):#Se calcula el tamaño de la imagen para ver si es cuadrada
         print("Imagen Cuadrada")
         img2 = cv2.imread("marca_agua_cuadrada.png", cv2.IMREAD_UNCHANGED)#lee marca de agua cuadrada

    if h_img>(w_img*1.25):#Se calcula el tamaño de la imagen para ver si es vertical
         print("Imagen Vertical")
         img2 = cv2.imread("marca_agua_vertical.png", cv2.IMREAD_UNCHANGED)#lee marca de agua vertical

    #Lee ancho y alto de marca de agua
    h_ma = img2.shape[0]
    w_ma = img2.shape[1]
    tam_img2 = img2.shape
    print("Tamaño de Marca de Agua --> "+str(tam_img2)+" H:"+str(h_ma)+"px x W:"+str(w_ma)+"px")
    #cv2.imshow('Marca de agua', img2) Muestra marca de agua

    #Ajusta el tamaño de la marca de agua al tamaño de la imagen principal
    MA = cv2.resize(img2, (img.shape[1], img.shape[0]))
    height_img2_r = MA.shape[0]
    width_img2_r = MA.shape[1]
    print("Tamaño de Marca de Agua Redimensionada --> "+" H:"+str(height_img2_r)+"px x W:"+str(width_img2_r)+"px")
    #cv2.imshow('Marca de agua Redimensionada', MA) Muestra marca de agua redimensionada

    #Factor de Opacidad, ajusta de acuerdo a tu necesidad, recomiendo entre 0.2 y 0.3
    FO = 0.3
    #Fusiona la imagen y la marca de agua desde las coordenadas x=0 y y=0 de imagen original ya que ambas son del mismo tamaño
    img[0:0 + h_img, 0:0 + w_img] = img[0:0 + h_img, 0:0 + w_img] * (1-FO*MA[:,:,3:4]/255) + (FO*MA[:,:,0:3] * (MA[:,:,3:4]/255))
    #cv2.imshow('Imagen con Marca de Agua', img) Muestra imagen con marca de agua
    cv2.imwrite("./imagenes_ok/"+nombre_archivo, img)#Guarda la imagen con marca de agua en carpeta de salida

print("\nProceso completado\n")

