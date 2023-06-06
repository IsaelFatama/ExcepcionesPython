#Excepción 5: FileNotFoundError
archivo = "mi_carpeta/archivo.txt"

try:
    with open(archivo, 'r') as f:
        contenido = f.read()
        print(contenido)
except FileNotFoundError:
    print("¡Error! El archivo no se encontró.")
