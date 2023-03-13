import os
import shutil
import variables as var

def mover_directorio():
    
    directorio_deseado = input('Seleccione directorio a organizar: ')
    os.chdir(directorio_deseado)

def crear_carpetas():

    for i in var.lista_carpetas:
        os.makedirs(i, exist_ok=True)

def mover_archivos_carpeta():

    for i in os.listdir():
        if i.endswith(var.doc_types):
            shutil.move(i, 'documentos')
        elif i.endswith(var.img_types):
            shutil.move(i, 'imagenes')
        elif i.endswith(var.software_types):
            shutil.move(i, 'software')
        else:
            if not os.path.isdir(i):
                shutil.move(i, 'otros')