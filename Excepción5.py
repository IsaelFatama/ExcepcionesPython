#Excepción 5: FileNotFoundError
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError as e:
        print("Error:", str(e))
        print("Se produjo un FileNotFoundError. No se puede encontrar el archivo especificado.")
        return None

file_path = 'nonexistent_file.txt'
file_content = read_file(file_path)
if file_content is not None:
    print("El contenido del archivo es:\n", file_content)
