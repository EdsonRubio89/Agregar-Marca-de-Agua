import os

ruta = "./imagenes_read"
# Lista todos los archivos en la carpeta
archivos = os.listdir(ruta)
# Inicializa un contador
j = 1
# Itera sobre cada archivo y cambia su nombre
for nombre_archivo in archivos:
    # Construye el camino completo al archivo antiguo y al nuevo
    ruta_inicial = os.path.join(ruta, nombre_archivo)
    nuevo_nombre = f"Imagen_{j}.jpg"
    ruta_final = os.path.join(ruta, nuevo_nombre)
    # Cambia el nombre del archivo
    os.rename(ruta_inicial, ruta_final)
    print(f"Se cambió el nombre de {nombre_archivo} a {nuevo_nombre}")
    # Incrementa el contador
    j += 1

print("Proceso completado")